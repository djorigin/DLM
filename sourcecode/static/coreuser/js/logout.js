document.addEventListener('DOMContentLoaded', function() {
    var logoutButton = document.getElementById('logout-button');
    logoutButton.addEventListener('click', function() {
      var confirmation = confirm('Are you sure you want to log out?');
      if (confirmation) {
        window.location.href = '/logout';
      }
    });
  });
  