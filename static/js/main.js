$(document).ready(function(){
    $('select').material_select();
    $('.collapsible').collapsible();
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

function toggle(showRaceDetails) {
    var raceDetails = document.getElementById('race-details');
    var userDetails = document.getElementById('user-details');
    if (showRaceDetails) {
        raceDetails.style.display = 'block';
        userDetails.style.display = 'none';
    } else {
        raceDetails.style.display = 'none';
        userDetails.style.display = 'block';
    }
};
