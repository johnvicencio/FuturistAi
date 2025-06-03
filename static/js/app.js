document.addEventListener('DOMContentLoaded', function () {
  var modalEl = document.getElementById('predictionModal');
  if (modalEl) {
    var predictionModal = new mdb.Modal(modalEl);
    predictionModal.show();

    var doneButtons = document.querySelectorAll('.done-button');
    doneButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        window.location.href = '/';
      });
    });
  }
});