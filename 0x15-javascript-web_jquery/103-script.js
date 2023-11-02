$(document).ready(function() {
    function translateHello() {
        const languageCode = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;
        
        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translateHello);

    $('#language_code').keypress(function(event) {
        if (event.keyCode === 13) {
            translateHello();
        }
    });
});