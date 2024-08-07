$(document).ready(function() {
  function fetchTranslation() {
    var langCode = $('#language_code').val();
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  }

  // Click event for the button
  $('#btn_translate').click(function() {
    fetchTranslation();
  });

  // Keypress event for the input field
  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // 13 is the Enter key
      fetchTranslation();
    }
  });
});

