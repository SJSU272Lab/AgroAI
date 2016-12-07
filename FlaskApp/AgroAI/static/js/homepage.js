/**
 * Created by ajay on 11/20/16.
 */

function answerQuery() {
  var response;
  $.ajax({
    async: false,
    type:'POST',
    url: 'loadIt',
    data: {"Hey":"Whatsup"},
    timeout: 4000,
    success: function(result) {
      response = result;
      alert(response);
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      response = "err--" + XMLHttpRequest.status + " -- " + XMLHttpRequest.statusText;
      alert(response);
    }
  });
}