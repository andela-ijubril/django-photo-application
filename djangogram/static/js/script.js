$.ajaxSetup({
  headers: {
    'X-CSRFToken': $("meta[name='csrf-token']").attr('content'),
  },
});

/**
 * @param {string} effectName
 * @param {string} imageUrl
 * @param {int} imageId
 */
function sendEffect(effectName, imageUrl, imageId) {
  $.notify('<strong>Applying effect...</strong>', {
    type: 'info',
    allow_dismiss: true,
    delay: 1000,
    timer: 700,
    placement: {
      from: 'top',
      align: 'center',
    },
  });
  $.ajax({
    url: imageUrl,
    type: 'POST',
    data: {
      effect_name: effectName,
      image_id: imageId,
    },
    success: function (data) {
      var imgSrc = data.applied_effect + '?' + new Date().getTime();
      $('#img').attr('src', imgSrc);
      $('#savebtn').attr('href', imgSrc);
      console.log('I returned success');
    },

    error: function () {

    },
  });
}

function applyEffects(imageId) {
  var effectClass = $('.effects > button');
  effectClass.off('click');

  effectClass.click(function () {
    $(this).siblings().removeClass('active');
    var effect = $(this).data('effect');

    console.log(imageId);
    var imageUrl = '/effect/';
    sendEffect(effect, imageUrl, imageId);
    $(this).addClass('active');

  });
};

var deletebtn = $('#delete');
var deleteImage = function () {
  deletebtn.click(function (e) {
    e.preventDefault();
    var result = confirm('Are you sure you want to delete');
    console.log(result);
    if (result) {
      var image_to_be_deleted = $('#img').attr('src');
      console.log(image_to_be_deleted);
      var image_id = $('#img').data('id');
      console.log(image_id);

      $.notify('<strong>Deleting image...</strong>', {
        type: 'info',
        allow_dismiss: true,
        delay: 1000,
        timer: 700,
        placement: {
          from: 'top',
          align: 'center',
        },
      });

      $.ajax({
        url: '/delete/',
        type: 'POST',
        data: {
          image_id: image_id,
        },
        success: function () {
          window.location.reload();

        },

        error: function () {

        },
      });
    }

  });
};

var fbShare = $('#share');
fbShare.click(function () {
  var img_src = $('#img').attr('src');
  $(this).attr('href', img_src);
  console.log(img_src);
  facebook.share(img_src);
});

var initUploadPlugin = function () {

  var ul = $('#upload ul');

  $('#drop a').click(function () {
    // Simulate a click on the file input button
    // to show the file browser dialog
    $(this).parent().find('input').click();

  });

  // Initialize the jQuery File Upload plugin

  $('#upload').fileupload({
    // This element will accept file drag/drop uploading
    dropZone: $('#drop'),

    // This function is called when a file is added to the queue;
    // either via the browse button, or via drag/drop:
    add: function (e, data) {

      var tpl = $('<li class="working"><input type="text" value="0" data-width="48" data-height="48"' +
        ' data-fgColor="#0788a5" data-readOnly="1" data-bgColor="#3e4043" /><p></p><span></span></li>');

      // Append the file name and file size
      tpl.find('p').text(data.files[0].name)
        .append('<i>' + formatFileSize(data.files[0].size) + '</i>');

      // Add the HTML to the UL element
      data.context = tpl.appendTo(ul);

      // Listen for clicks on the cancel icon
      tpl.find('span').click(function () {

        if (tpl.hasClass('working')) {
          jqXHR.abort();
        }

        tpl.fadeOut(function () {
          tpl.remove();
        });

      });

      // Automatically upload the file once it is added to the queue

      var jqXHR = data.submit();
    },

    progress: function (e, data) {

      // Calculate the completion percentage of the upload
      var progress = parseInt(data.loaded / data.total * 100, 10);

      // Update the hidden input field and trigger a change
      // so that the jQuery knob plugin knows to update the dial
      data.context.find('input').val(progress).change();

      if (progress == 100) {
        data.context.removeClass('working');
      }
    },

    done: function (e, data) {

      if (data.textStatus == 'success') {
        console.log('I worked and uploaded successfully');
      }

      window.location.reload();
    },

    fail: function (e, data) {
      // Something has gone wrong!
      console.log('I failed to upload');
      data.context.addClass('error');
    },
  });

};

var facebook = {
  init: function () {
    // Load FB JS SDK asynchronously
    $.getScript('//connect.facebook.net/en_US/sdk.js', function () {
      FB.init({
        appId: '1530581673929955',
        version: 'v2.5',
      });
    });
  },

  share: function (img_src) {
    console.log('http://' + location.host + img_src);
    FB.ui({
      method: 'feed',
      link: window.location.href,
      caption: 'I just edited my picture with djangogram',
      picture: 'http://' + location.host + img_src,
      description: 'Djangogram is awesome... Kindly check it out',
    }, function (response) {
    });
  },
};

// Helper function that formats the file sizes
function formatFileSize(bytes) {
  if (typeof bytes !== 'number') {
    return '';
  }

  if (bytes >= 1000000000) {
    return (bytes / 1000000000).toFixed(2) + ' GB';
  }

  if (bytes >= 1000000) {
    return (bytes / 1000000).toFixed(2) + ' MB';
  }

  return (bytes / 1000).toFixed(2) + ' KB';
}

$(document).ready(function () {
  $('.single-image').click(function () {
    var image_to_be_edited = $(this).find('img').attr('src');
    var image_id = $(this).find('img').data('id');
    $('#img-effect').find('img').attr('src', image_to_be_edited + '?' + new Date().getTime());
    $('#img-effect').find('img').attr('data-id', image_id);
    $('#savebtn').attr('href', image_to_be_edited);

    applyEffects(image_id);

  });

  initUploadPlugin();
  facebook.init();
  deleteImage();

});
