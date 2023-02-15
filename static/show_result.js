$(document).ready(function() {
  $("#psychology-test-form").submit(function(event) {
    event.preventDefault();

    var formData = $(this).serialize();

    $.ajax({
      type: "POST",
      url: "/show_result",
      data: formData,
      success: function(result) {
	$("#result").html(result);
      }
    });
  });
});
