function navigateVersion(folder) {
  var parts = window.location.pathname.replace(/\/$/, '').split('/');
  parts[2] = folder;
  window.location.pathname = parts.join('/') + '/';
}
