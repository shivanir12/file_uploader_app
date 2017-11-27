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

                },
                error : function(error) {
                    console.log(error)
                }
    });
});
