$(document).ready(function () {
    var links = $('.item-nav ul li a');
    $.each(links, function (key, va) {
        if (va.href == document.URL) {
            $(this).addClass('active');
        }
    });
});



