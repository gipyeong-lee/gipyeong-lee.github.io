(function () {
  var bar = document.querySelector('.audio-player');
  if (!bar) return;

  var src = bar.getAttribute('data-src');
  if (!src) return;

  var ref = bar.getAttribute('data-ref') || '';
  // No src until the first play. With new Audio(src) the browser downloaded
  // the whole mp3 on every view of a post with narration, played or not
  // (preload defaults to auto). Contract: scripts/tests/test_audio_player.mjs
  var audio = new Audio();
  audio.preload = 'none';
  var loaded = false;
  var attempt = 0;
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

  // Position from the last visit; restored once the metadata has loaded.
  var saved = parseFloat(localStorage.getItem('audio-pos-' + ref)) || 0;

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
      if (!loaded) {
        loaded = true;
        audio.src = src;
      }
      setIcon('pause');
      var mine = ++attempt;
      var playing = audio.play();
      // A missing file rejects here and leaves paused false; reset so the
      // next click plays again. A rejection from an older attempt (pause
      // pressed before playback began) must not stop a newer one.
      if (playing && playing.catch) {
        playing.catch(function () {
          if (mine !== attempt) return;
          audio.pause();
          setIcon('play');
        });
      }
    } else {
      audio.pause();
      setIcon('play');
    }
  });

  audio.addEventListener('timeupdate', function () {
    updateTime();
    if (saved) return; // still at 0 until the saved position is restored
    localStorage.setItem('audio-pos-' + ref, audio.currentTime);
  });

  audio.addEventListener('loadedmetadata', function () {
    if (saved > 0 && saved < audio.duration) audio.currentTime = saved;
    saved = 0;
    updateTime();
  });

  audio.addEventListener('ended', function () {
    setIcon('play');
    localStorage.removeItem('audio-pos-' + ref);
  });

  progress.addEventListener('click', function (e) {
    if (!audio.duration) return; // nothing loaded yet, so nothing to seek in
    var rect = progress.getBoundingClientRect();
    var pct = (e.clientX - rect.left) / rect.width;
    audio.currentTime = pct * audio.duration;
  });

  speedBtn.addEventListener('click', function () {
    speedIdx = (speedIdx + 1) % speeds.length;
    // defaultPlaybackRate too: assigning src on the first play resets
    // playbackRate to it, which would drop a speed picked before playing.
    audio.playbackRate = audio.defaultPlaybackRate = speeds[speedIdx];
    speedBtn.textContent = speeds[speedIdx] + 'x';
  });

  closeBtn.addEventListener('click', function () {
    audio.pause();
    bar.classList.remove('is-visible');
    document.body.classList.remove('audio-active');
  });
})();
