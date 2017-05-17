$(document).ready(function(){
    $('#toggle').click(function(){
         toggle();
    });
    $('select').material_select();
    $('.collapsible').collapsible();
    var raceDetails = document.getElementById('race-details');
    var userDetails = document.getElementById('user-details');
    var submitBtn = document.getElementById('submitBtn');
    if (raceDetails.style.display != 'none') {
        userDetails.style.display = 'none';
        submitBtn.style.display = 'none';

    } else {
        raceDetails.style.display = 'none';
        userDetails.style.display = 'block';
        submitBtn.style.display = 'block';
    }
});

$('.datepicker').pickadate({
    min: true,
    max: 168,
    closeOnSelect: true,
    closeOnClear: true
});

$('.timepicker').pickatime({
    default: 'now',
    twelvehour: false,
    donetext: 'OK',
    autoclose: false,
    vibrate: true // vibrate the device when dragging clock hand
});

function toggle() {
      $('#race-details').toggle();
      $('#user-details').toggle();
      $('#submitBtn').toggle();
};
