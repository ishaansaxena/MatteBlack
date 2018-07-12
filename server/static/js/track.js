$(document).ready(function() {
    $('#track').click(function() {
        console.log(trackURL);
        $.get(trackURL, function(data) {
            console.log(data);
        });
    });
});
