(function () {
  var container = document.querySelector('.quiz');
  if (!container) return;

  var ref = container.getAttribute('data-ref') || '';
  var storageKey = 'quiz-' + ref;
  var cards = container.querySelectorAll('.quiz__card');
  var resultEl = container.querySelector('.quiz__result');
  var total = cards.length;
  var answered = 0;
  var correct = 0;

  // Already completed
  var prev = localStorage.getItem(storageKey);
  if (prev) {
    var alreadyEl = container.querySelector('.quiz__already');
    if (alreadyEl) {
      alreadyEl.style.display = 'block';
      alreadyEl.textContent = prev;
    }
  }

  cards.forEach(function (card) {
    var answerIdx = parseInt(card.getAttribute('data-answer'), 10);
    var choices = card.querySelectorAll('.quiz__choice');

    choices.forEach(function (choice, idx) {
      choice.addEventListener('click', function () {
        if (card.classList.contains('is-answered')) return;

        card.classList.add('is-answered');
        answered++;

        if (idx === answerIdx) {
          correct++;
          card.classList.add('is-correct');
          choice.classList.add('is-selected-correct');
        } else {
          card.classList.add('is-wrong');
          choice.classList.add('is-selected-wrong');
          choices[answerIdx].classList.add('is-actual-answer');
        }

        if (answered === total) showResult();
      });
    });
  });

  function showResult() {
    if (!resultEl) return;
    resultEl.classList.add('is-visible');

    var scoreEl = resultEl.querySelector('.quiz__score');
    var starsEl = resultEl.querySelector('.quiz__stars');
    var msgEl = resultEl.querySelector('.quiz__message');

    if (scoreEl) scoreEl.textContent = correct + ' / ' + total;

    if (starsEl) {
      var stars = '';
      for (var i = 0; i < total; i++) {
        stars += i < correct ? '\u2B50' : '\u2606';
      }
      starsEl.textContent = stars;
    }

    if (msgEl) {
      var messages = {
        0: ['Keep reading!', '\uB2E4\uC2DC \uC77D\uC5B4\uBCF4\uC138\uC694!'],
        1: ['Good start!', '\uC88B\uC740 \uC2DC\uC791\uC774\uC5D0\uC694!'],
        2: ['Well done!', '\uC798\ud558\uc168\uc5b4\uc694!'],
        3: ['Perfect!', '\uC644\ubcbd\ud574\uc694!']
      };
      var pair = messages[correct] || messages[0];
      msgEl.textContent = pair[0];
    }

    localStorage.setItem(storageKey, correct + '/' + total);
  }
})();
