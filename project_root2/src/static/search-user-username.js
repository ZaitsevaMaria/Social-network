$('.search-byusername-user-form').submit(function(e){
    $.post('photo/form_search_user_username/', $(this).serialize(), function(data){
       $('.users').html(data);
    });
    e.preventDefault();
});



