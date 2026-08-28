(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (root) root.LearnProgress = api;
})(typeof window !== "undefined" ? window : null, function () {
  "use strict";

  function initialState(courseSlug, curriculumVersion) {
    return {
      schemaVersion: 2,
      courseSlug: courseSlug,
      curriculumVersion: curriculumVersion,
      completedModuleIds: [],
      assignmentChecks: {},
      quizScores: {},
      capstoneChecks: [],
      capstoneCompleted: false,
      sponsorshipDismissed: { start: false, complete: false },
    };
  }

  function completeModule(state, moduleId) {
    var ids = state.completedModuleIds.slice();
    if (!ids.includes(moduleId)) ids.push(moduleId);
    return Object.assign({}, state, { completedModuleIds: ids });
  }

  function setAssignmentCheck(state, moduleId, itemIndex, checked) {
    var assignments = Object.assign({}, state.assignmentChecks);
    var checkedItems = (assignments[moduleId] || []).slice();
    var position = checkedItems.indexOf(itemIndex);
    if (checked && position === -1) checkedItems.push(itemIndex);
    if (!checked && position !== -1) checkedItems.splice(position, 1);
    checkedItems.sort(function (left, right) { return left - right; });
    assignments[moduleId] = checkedItems;
    return Object.assign({}, state, { assignmentChecks: assignments });
  }

  function setQuizScore(state, moduleId, score) {
    return Object.assign({}, state, {
      quizScores: Object.assign({}, state.quizScores, { [moduleId]: score }),
    });
  }

  function canCompleteModule(state, moduleId, assignmentCount, quizThreshold) {
    var threshold = quizThreshold == null ? 80 : quizThreshold;
    var checked = new Set(state.assignmentChecks[moduleId] || []);
    var allAssignments = assignmentCount > 0 && checked.size === assignmentCount;
    return allAssignments && Number(state.quizScores[moduleId] || 0) >= threshold;
  }

  function setCapstoneCheck(state, itemIndex, checked) {
    var checks = (state.capstoneChecks || []).slice();
    var position = checks.indexOf(itemIndex);
    if (checked && position === -1) checks.push(itemIndex);
    if (!checked && position !== -1) checks.splice(position, 1);
    checks.sort(function (left, right) { return left - right; });
    return Object.assign({}, state, { capstoneChecks: checks, capstoneCompleted: false });
  }

  function canCompleteCapstone(state, moduleIds, capstoneCount) {
    return moduleIds.every(function (moduleId) {
      return state.completedModuleIds.includes(moduleId);
    }) && capstoneCount > 0 && new Set(state.capstoneChecks || []).size === capstoneCount;
  }

  function completeCapstone(state) {
    return Object.assign({}, state, { capstoneCompleted: true });
  }

  function progressPercent(state, moduleIds) {
    var total = moduleIds.length + 1;
    var completed = state.completedModuleIds.length + (state.capstoneCompleted ? 1 : 0);
    return total ? Math.round((completed / total) * 100) : 0;
  }

  function storageKey(courseSlug, curriculumVersion) {
    return "learn-progress:" + courseSlug + ":" + curriculumVersion;
  }

  function importState(raw, contract) {
    var parsed;
    try {
      parsed = typeof raw === "string" ? JSON.parse(raw) : raw;
    } catch (_error) {
      throw new Error("Invalid progress JSON");
    }
    if (!parsed || parsed.schemaVersion !== 2) throw new Error("Unsupported schema version");
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
    var assignments = {};
    var importedAssignments = parsed.assignmentChecks || {};
    if (typeof importedAssignments !== "object" || Array.isArray(importedAssignments)) {
      throw new Error("Invalid assignment data");
    }
    Object.keys(importedAssignments).forEach(function (moduleId) {
      var indices = importedAssignments[moduleId];
      if (!allowed.has(moduleId)) throw new Error("Unknown module assignment");
      if (!Array.isArray(indices) || indices.some(function (index) { return !Number.isInteger(index) || index < 0; })) {
        throw new Error("Invalid assignment data");
      }
      assignments[moduleId] = Array.from(new Set(indices)).sort(function (left, right) { return left - right; });
    });
    var dismissed = parsed.sponsorshipDismissed || {};
    var capstoneChecks = parsed.capstoneChecks || [];
    var capstoneCount = Number(contract.capstoneCount || 0);
    if (!Array.isArray(capstoneChecks) || capstoneChecks.some(function (index) {
      return !Number.isInteger(index) || index < 0 || index >= capstoneCount;
    })) {
      throw new Error("Invalid capstone data");
    }
    return {
      schemaVersion: 2,
      courseSlug: contract.courseSlug,
      curriculumVersion: contract.curriculumVersion,
      completedModuleIds: completed,
      assignmentChecks: assignments,
      quizScores: scores,
      capstoneChecks: Array.from(new Set(capstoneChecks)).sort(function (left, right) { return left - right; }),
      capstoneCompleted: parsed.capstoneCompleted === true,
      sponsorshipDismissed: {
        start: dismissed.start === true,
        complete: dismissed.complete === true,
      },
    };
  }

  function sponsorshipUrl(base, moment, language) {
    if (!base) return "";
    var url = new URL(base);
    var stripeLocales = { "zh-cn": "zh", "zh-tw": "zh-TW" };
    url.searchParams.set("locale", stripeLocales[language] || language || "ko");
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
      capstoneCount: Number(shell.dataset.capstoneCount || 0),
    };
    var currentModule = shell.dataset.currentModule || "";
    var courseLocale = shell.dataset.courseLocale || "ko";
    var courseStorageKey = storageKey(contract.courseSlug, contract.curriculumVersion);
    var state = initialState(contract.courseSlug, contract.curriculumVersion);

    function message(name, replacements) {
      var value = shell.dataset[name] || "";
      Object.keys(replacements || {}).forEach(function (key) {
        value = value.split("%{" + key + "}").join(String(replacements[key]));
      });
      return value;
    }

    function announce(message) {
      document.querySelectorAll("[data-learn-status]").forEach(function (element) {
        element.textContent = message;
      });
    }
    function save() {
      try { localStorage.setItem(courseStorageKey, JSON.stringify(state)); } catch (_error) { announce(message("uiStorageUnavailable")); }
    }
    try {
      var saved = localStorage.getItem(courseStorageKey);
      if (saved) state = importState(saved, contract);
    } catch (_error) {
      state = initialState(contract.courseSlug, contract.curriculumVersion);
      announce(message("uiProgressReset"));
    }

    function render() {
      var percent = progressPercent(state, contract.moduleIds);
      document.querySelectorAll("[data-learn-progress-bar]").forEach(function (bar) { bar.style.width = percent + "%"; });
      document.querySelectorAll(".learn-progress[role='progressbar']").forEach(function (bar) { bar.setAttribute("aria-valuenow", String(percent)); });
      document.querySelectorAll("[data-learn-progress-text]").forEach(function (text) { text.textContent = message("uiProgressComplete", { percent: percent }); });
      document.querySelectorAll("[data-learn-module-row]").forEach(function (row) {
        row.classList.toggle("is-complete", state.completedModuleIds.includes(row.dataset.learnModuleRow));
      });
      document.querySelectorAll("[data-assignment-check]").forEach(function (checkbox, index) {
        checkbox.checked = (state.assignmentChecks[currentModule] || []).includes(index);
      });
      var completeButton = document.querySelector("[data-complete-module]");
      if (completeButton) {
        var completed = state.completedModuleIds.includes(currentModule);
        var assignmentCount = document.querySelectorAll("[data-assignment-check]").length;
        completeButton.textContent = completed ? message("uiModuleCompleted") : message("uiModuleComplete");
        completeButton.disabled = completed || !canCompleteModule(state, currentModule, assignmentCount, 80);
      }
      document.querySelectorAll("[data-capstone-check]").forEach(function (checkbox, index) {
        checkbox.checked = (state.capstoneChecks || []).includes(index);
      });
      var capstoneButton = document.querySelector("[data-complete-capstone]");
      if (capstoneButton) {
        capstoneButton.textContent = state.capstoneCompleted ? message("uiCapstoneCompleted") : message("uiCapstoneComplete");
        capstoneButton.disabled = state.capstoneCompleted || !canCompleteCapstone(state, contract.moduleIds, contract.capstoneCount);
      }
      var startCard = document.querySelector("[data-sponsorship='start']");
      if (startCard) startCard.hidden = state.sponsorshipDismissed.start || state.completedModuleIds.length > 0;
      var completeCard = document.querySelector("[data-sponsorship='complete']");
      if (completeCard) completeCard.hidden = percent !== 100 || state.sponsorshipDismissed.complete;
    }

    document.querySelectorAll("[data-sponsorship-link]").forEach(function (link) {
      link.href = sponsorshipUrl(link.href, link.dataset.moment, courseLocale);
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
      var assignmentCount = document.querySelectorAll("[data-assignment-check]").length;
      if (!canCompleteModule(state, currentModule, assignmentCount, 80)) {
        announce(message("uiModuleRequirements"));
        return;
      }
      state = completeModule(state, currentModule);
      save();
      render();
      announce(message("uiModuleSaved"));
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
        if (status) status.textContent = message("uiQuizAnswerAll");
        return;
      }
      var score = questions.length ? Math.round((correct / questions.length) * 100) : 0;
      state = setQuizScore(state, currentModule, score);
      save();
      if (status) status.textContent = message("uiQuizCorrect", { correct: correct, total: questions.length, score: score });
      render();
    });

    document.querySelectorAll("[data-assignment-check]").forEach(function (checkbox, index) {
      checkbox.checked = (state.assignmentChecks[currentModule] || []).includes(index);
      checkbox.addEventListener("change", function () {
        state = setAssignmentCheck(state, currentModule, index, checkbox.checked);
        save();
        render();
      });
    });

    document.querySelectorAll("[data-capstone-check]").forEach(function (checkbox, index) {
      checkbox.addEventListener("change", function () {
        state = setCapstoneCheck(state, index, checkbox.checked);
        save();
        render();
      });
    });
    var capstoneButton = document.querySelector("[data-complete-capstone]");
    if (capstoneButton) capstoneButton.addEventListener("click", function () {
      if (!canCompleteCapstone(state, contract.moduleIds, contract.capstoneCount)) {
        announce(message("uiCapstoneRequirements"));
        return;
      }
      state = completeCapstone(state);
      save();
      render();
      announce(message("uiCapstoneSaved"));
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
          announce(message("uiImportSuccess"));
        } catch (error) {
          announce(message("uiImportFailure", { error: error.message }));
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

  return {
    initialState: initialState,
    completeModule: completeModule,
    setAssignmentCheck: setAssignmentCheck,
    setQuizScore: setQuizScore,
    canCompleteModule: canCompleteModule,
    setCapstoneCheck: setCapstoneCheck,
    canCompleteCapstone: canCompleteCapstone,
    completeCapstone: completeCapstone,
    progressPercent: progressPercent,
    storageKey: storageKey,
    importState: importState,
    sponsorshipUrl: sponsorshipUrl,
  };
});
