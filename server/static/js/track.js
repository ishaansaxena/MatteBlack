$(document).ready(function() {
    $('#track').click(function() {
        console.log(trackURL);
        $.get(trackURL, function(data) {
            $('#track-outer').addClass('hide');
            $('#untrack-outer').removeClass('hide');
        });
    });
    $('#untrack').click(function() {
        console.log(untrackURL);
        $.get(untrackURL, function(data) {
            $('#untrack-outer').addClass('hide');
            $('#track-outer').removeClass('hide');
        });
    });
});
