var image_sidebar = $('#image-sidebar');

var image_content = "";

$(document).ready(function() {
$('.single-image').click(function(){
var image_to_be_edited = $(this).find('img').attr('src');
$('#img-effect').find('img').attr('src', image_to_be_edited);
});



    $('#file_upload').fileupload({
    url: 'php/index.php',
    done: function (e, data) {
        $.each(data.result, function (index, file) {
            $('<p/>').text(file.name).appendTo('body');
        });
    }
});




});
