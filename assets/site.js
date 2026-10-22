(function () {
  var copyBtn = document.getElementById('copy-btn');
  var field = document.getElementById('edge-url');
  var status = document.getElementById('copy-status');
  copyBtn.addEventListener('click', function () {
    var done = function () { status.textContent = 'Copied. Paste it into the Edge address bar.'; };
    var fallback = function () {
      field.focus(); field.select();
      status.textContent = 'Selected. Press Ctrl+C (or Cmd+C on a Mac) to copy.';
    };
    try { navigator.clipboard.writeText(field.value).then(done, fallback); } catch (e) { fallback(); }
  });
})();
