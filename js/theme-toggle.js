(function () {
  var toggle = document.querySelector('.theme-toggle');
  if (!toggle) return;

  toggle.addEventListener('click', function () {
    var current = document.documentElement.getAttribute('data-theme');
    var next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateIcon(next);
  });

  function updateIcon(theme) {
    var icon = toggle.querySelector('i');
    if (!icon) return;
    icon.className = theme === 'dark'
      ? 'ion ion-ios-sunny'
      : 'ion ion-ios-moon';
  }

  var saved = localStorage.getItem('theme');
  if (saved) {
    updateIcon(saved);
  } else {
    var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    updateIcon(prefersDark ? 'dark' : 'light');
  }
})();
