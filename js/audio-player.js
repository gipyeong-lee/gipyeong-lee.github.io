(function () {
  var bar = document.querySelector('.audio-player');
  if (!bar) return;

  var src = bar.getAttribute('data-src');
  if (!src) return;

  var ref = bar.getAttribute('data-ref') || '';
  var audio = new Audio(src);
  var btn = bar.querySelector('.audio-player__btn');
  var btnIcon = btn.querySelector('i');
  var fill = bar.querySelector('.audio-player__progress-fill');
  var progress = bar.querySelector('.audio-player__progress');
  var speedBtn = bar.querySelector('.audio-player__speed');
  var timeEl = bar.querySelector('.audio-player__time');
  var closeBtn = bar.querySelector('.audio-player__close');
  var speeds = [1, 1.5, 2];
  var speedIdx = 0;

  bar.classList.add('is-visible');
  document.body.classList.add('audio-active');

  // Restore position
  var saved = localStorage.getItem('audio-pos-' + ref);
  if (saved) audio.currentTime = parseFloat(saved);

  function fmt(s) {
    var m = Math.floor(s / 60);
    var sec = Math.floor(s % 60);
    return m + ':' + (sec < 10 ? '0' : '') + sec;
  }

  function setIcon(name) {
    btnIcon.className = 'ion ion-ios-' + name;
  }

  function updateTime() {
    if (audio.duration) {
      fill.style.width = (audio.currentTime / audio.duration * 100) + '%';
      timeEl.textContent = fmt(audio.currentTime) + ' / ' + fmt(audio.duration);
    }
  }

  btn.addEventListener('click', function () {
    if (audio.paused) {
      audio.play();
      setIcon('pause');
    } else {
      audio.pause();
      setIcon('play');
    }
  });

  audio.addEventListener('timeupdate', function () {
    updateTime();
    localStorage.setItem('audio-pos-' + ref, audio.currentTime);
  });

  audio.addEventListener('loadedmetadata', updateTime);

  audio.addEventListener('ended', function () {
    setIcon('play');
    localStorage.removeItem('audio-pos-' + ref);
  });

  progress.addEventListener('click', function (e) {
    var rect = progress.getBoundingClientRect();
    var pct = (e.clientX - rect.left) / rect.width;
    audio.currentTime = pct * audio.duration;
  });

  speedBtn.addEventListener('click', function () {
    speedIdx = (speedIdx + 1) % speeds.length;
    audio.playbackRate = speeds[speedIdx];
    speedBtn.textContent = speeds[speedIdx] + 'x';
  });

  closeBtn.addEventListener('click', function () {
    audio.pause();
    bar.classList.remove('is-visible');
    document.body.classList.remove('audio-active');
  });
})();
