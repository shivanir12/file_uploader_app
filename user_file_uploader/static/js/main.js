$('#search-form').on('submit', function(event) {
    event.preventDefault();

    $.ajax({
        url:'/user/search/',
                method: 'GET',
                data : { search : $('#search-text').val() },
                success : function(json) {
                    var element
                    element = $('#result-list')
                    element.empty()
                    var len = json && json.result && json.result.length
                    if(len > 0) {
                        for ( var i = 0; i < len; i++ ){
                               user = json.result[i]
                               element.append('<a href="/user/profile/' + user + '">' + user + '</a>')
                          }
                    }
                    else {
                        element.append('<div>No Search results found</div>')
                    }

                }
    });
});

$('#input_file').on('change', function() {
    if ($('#input_file').val() != "") {
        $('#file_upload_btn').removeAttr('disabled');
    }
});

var file_id;

$('.share').on('click', function (e) {
   e.preventDefault();
   file_id = $(this).data('fileId');
   user_name = $('#user_name').val()
   $.ajax({
           url:'/user/all/',
                   method: 'GET',
                   data : { 'username': user_name },
                   success : function(json) {
                       var element
                       element = $('#user-list');
                       element.empty();
                       $('#user-list-title').empty().append('Please select a user to share the file');
                       element.append('<option value="select">Select</option>')
                       var len = json && json.result && json.result.length
                       if(len > 0) {
                           for ( var i = 0; i < len; i++ ) {
                                user = json.result[i]
                                element.append('<option value="'+user+'">'+user+'</option>')
                            }
                            element.attr("style", "visibility: visible")
                            $('#file-share-btn').removeAttr('hidden')
                       }
                       else {
                           element.append('<div>No Search users found</div>')
                       }

                   }
       });
});

$('#file-share-btn').on('click', function(event) {
    event.preventDefault();

    if($('#user-list').val() == 'select') {
        return;
    }
    $.ajax({
        method: 'POST',
        url: '/user/file/share/',
        data: { 'file_id': file_id, 'file_shared_with': $('#user-list').val() },
        success: function(response) {
            var resultElement;
            resultElement = $('#file-share-response').empty().append('<p>File Successfully shared with user<p/>')
        },
        error: function(error) {
            console.log('in error');
        }
    });
});

function getCookie(name) {
    var cookieValue = null;
    if(document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for(var i=0; i<cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if(cookie.substring(0, name.length+1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length+1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken')

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
