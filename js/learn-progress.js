(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (root) root.LearnProgress = api;
})(typeof window !== "undefined" ? window : null, function () {
  "use strict";

  function initialState(courseSlug, curriculumVersion) {
    return {
      schemaVersion: 1,
      courseSlug: courseSlug,
      curriculumVersion: curriculumVersion,
      completedModuleIds: [],
      quizScores: {},
      sponsorshipDismissed: { start: false, complete: false },
    };
  }

  function completeModule(state, moduleId) {
    var ids = state.completedModuleIds.slice();
    if (!ids.includes(moduleId)) ids.push(moduleId);
    return Object.assign({}, state, { completedModuleIds: ids });
  }

  function importState(raw, contract) {
    var parsed;
    try {
      parsed = typeof raw === "string" ? JSON.parse(raw) : raw;
    } catch (_error) {
      throw new Error("Invalid progress JSON");
    }
    if (!parsed || parsed.schemaVersion !== 1) throw new Error("Unsupported schema version");
    if (parsed.courseSlug !== contract.courseSlug || parsed.curriculumVersion !== contract.curriculumVersion) {
      throw new Error("Progress belongs to another curriculum");
    }
    if (!Array.isArray(parsed.completedModuleIds)) throw new Error("Invalid module list");
    var allowed = new Set(contract.moduleIds);
    var completed = [];
    parsed.completedModuleIds.forEach(function (moduleId) {
      if (typeof moduleId !== "string" || !allowed.has(moduleId)) throw new Error("Unknown module in progress");
      if (!completed.includes(moduleId)) completed.push(moduleId);
    });
    var scores = {};
    if (!parsed.quizScores || typeof parsed.quizScores !== "object" || Array.isArray(parsed.quizScores)) {
      throw new Error("Invalid score data");
    }
    Object.keys(parsed.quizScores).forEach(function (moduleId) {
      var score = parsed.quizScores[moduleId];
      if (!allowed.has(moduleId)) throw new Error("Unknown module score");
      if (typeof score !== "number" || !Number.isFinite(score) || score < 0 || score > 100) {
        throw new Error("Invalid score");
      }
      scores[moduleId] = score;
    });
    var dismissed = parsed.sponsorshipDismissed || {};
    return {
      schemaVersion: 1,
      courseSlug: contract.courseSlug,
      curriculumVersion: contract.curriculumVersion,
      completedModuleIds: completed,
      quizScores: scores,
      sponsorshipDismissed: {
        start: dismissed.start === true,
        complete: dismissed.complete === true,
      },
    };
  }

  function sponsorshipUrl(base, moment) {
    if (!base) return "";
    var url = new URL(base);
    url.searchParams.set("utm_source", "learn");
    url.searchParams.set("utm_medium", "sponsorship");
    url.searchParams.set("utm_campaign", moment === "complete" ? "learn_complete" : "learn_start");
    return url.toString();
  }

  function initBrowser() {
    var shell = document.querySelector("[data-learn-course]");
    if (!shell) return;
    var contract = {
      courseSlug: shell.dataset.courseSlug,
      curriculumVersion: shell.dataset.curriculumVersion,
      moduleIds: (shell.dataset.moduleIds || "").split(",").filter(Boolean),
    };
    var currentModule = shell.dataset.currentModule || "";
    var storageKey = "learn-progress:" + contract.courseSlug + ":" + contract.curriculumVersion;
    var state = initialState(contract.courseSlug, contract.curriculumVersion);

    function announce(message) {
      document.querySelectorAll("[data-learn-status]").forEach(function (element) {
        element.textContent = message;
      });
    }
    function save() {
      try { localStorage.setItem(storageKey, JSON.stringify(state)); } catch (_error) { announce("이 브라우저에서는 진도를 저장할 수 없습니다."); }
    }
    try {
      var saved = localStorage.getItem(storageKey);
      if (saved) state = importState(saved, contract);
    } catch (_error) {
      state = initialState(contract.courseSlug, contract.curriculumVersion);
      announce("저장된 진도가 현재 교과과정과 맞지 않아 새로 시작합니다.");
    }

    function render() {
      var total = contract.moduleIds.length;
      var percent = total ? Math.round((state.completedModuleIds.length / total) * 100) : 0;
      document.querySelectorAll("[data-learn-progress-bar]").forEach(function (bar) { bar.style.width = percent + "%"; });
      document.querySelectorAll(".learn-progress[role='progressbar']").forEach(function (bar) { bar.setAttribute("aria-valuenow", String(percent)); });
      document.querySelectorAll("[data-learn-progress-text]").forEach(function (text) { text.textContent = percent + "% 완료"; });
      document.querySelectorAll("[data-learn-module-row]").forEach(function (row) {
        row.classList.toggle("is-complete", state.completedModuleIds.includes(row.dataset.learnModuleRow));
      });
      var completeButton = document.querySelector("[data-complete-module]");
      if (completeButton && state.completedModuleIds.includes(currentModule)) {
        completeButton.textContent = "완료됨";
        completeButton.disabled = true;
      }
      var startCard = document.querySelector("[data-sponsorship='start']");
      if (startCard) startCard.hidden = state.sponsorshipDismissed.start || state.completedModuleIds.length > 0;
      var completeCard = document.querySelector("[data-sponsorship='complete']");
      if (completeCard) completeCard.hidden = percent !== 100 || state.sponsorshipDismissed.complete;
    }

    document.querySelectorAll("[data-sponsorship-link]").forEach(function (link) {
      link.href = sponsorshipUrl(link.href, link.dataset.moment);
      link.addEventListener("click", function () {
        state.sponsorshipDismissed[link.dataset.moment] = true;
        save();
      });
    });
    document.querySelectorAll("[data-sponsorship-skip]").forEach(function (button) {
      button.addEventListener("click", function () {
        var card = button.closest("[data-sponsorship]");
        state.sponsorshipDismissed[card.dataset.sponsorship] = true;
        save();
        render();
      });
    });
    var completeButton = document.querySelector("[data-complete-module]");
    if (completeButton) completeButton.addEventListener("click", function () {
      state = completeModule(state, currentModule);
      save();
      render();
      announce("모듈 완료 기록을 이 브라우저에 저장했습니다.");
    });

    var quizButton = document.querySelector("[data-quiz-check]");
    if (quizButton) quizButton.addEventListener("click", function () {
      var questions = Array.from(document.querySelectorAll("[data-quiz-question]"));
      var correct = 0;
      var answered = 0;
      questions.forEach(function (question) {
        var selected = question.querySelector("input:checked");
        var explanation = question.querySelector("[data-quiz-explanation]");
        if (selected) {
          answered += 1;
          if (Number(selected.value) === Number(question.dataset.answerIndex)) correct += 1;
          if (explanation) explanation.hidden = false;
        }
      });
      var status = document.querySelector("[data-quiz-status]");
      if (answered !== questions.length) {
        if (status) status.textContent = "모든 문항에 답해주세요.";
        return;
      }
      var score = questions.length ? Math.round((correct / questions.length) * 100) : 0;
      state = Object.assign({}, state, { quizScores: Object.assign({}, state.quizScores, { [currentModule]: score }) });
      save();
      if (status) status.textContent = correct + "/" + questions.length + " 정답 · " + score + "점";
    });

    var exportButton = document.querySelector("[data-learn-export]");
    if (exportButton) exportButton.addEventListener("click", function () {
      var blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
      var url = URL.createObjectURL(blob);
      var anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = contract.courseSlug + "-progress.json";
      anchor.click();
      URL.revokeObjectURL(url);
    });
    var importInput = document.querySelector("[data-learn-import]");
    if (importInput) importInput.addEventListener("change", function () {
      var file = importInput.files && importInput.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        try {
          state = importState(String(reader.result), contract);
          save();
          render();
          announce("진도 파일을 가져왔습니다.");
        } catch (error) {
          announce("진도 파일을 가져올 수 없습니다: " + error.message);
        }
      };
      reader.readAsText(file);
    });
    render();
  }

  if (typeof document !== "undefined") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initBrowser);
    else initBrowser();
  }

  return { initialState: initialState, completeModule: completeModule, importState: importState, sponsorshipUrl: sponsorshipUrl };
});
