document.addEventListener('DOMContentLoaded', function () {
  var predictionModal = new mdb.Modal(document.getElementById('predictionModal'));
  predictionModal.show();

  var doneButtons = document.querySelectorAll('.done-button');
  doneButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      window.location.href = '/';
    });
  });
});
