function navigateVersion(folder) {
  var parts = window.location.pathname.replace(/\/$/, '').split('/');
  parts[1] = folder;
  window.location.pathname = parts.join('/') + '/';
}
