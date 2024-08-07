$(document).ready(function() {
  $('#btn_translate').click(function() {
    var langCode = $('#language_code').val();
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;
    
    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  });
});

