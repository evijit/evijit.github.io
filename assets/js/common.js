function adjustMobileNewsHeight() {
    if ($(window).width() > 576) return;
    var $container = $('#news-scroll');
    if (!$container.length) return;
    var $rows = $container.find('tr');
    if ($rows.length < 4) return;

    var height = 0;
    $rows.slice(0, 3).each(function() {
        height += $(this).outerHeight(true); // includes margins
    });
    // Half the 4th row peeks out to signal more content below
    height += $rows.eq(3).outerHeight() * 0.5;

    $container.css('max-height', height + 'px');
}

$(document).ready(function() {
    $('a.abstract').click(function() {
        $(this).parent().parent().find(".abstract.hidden").toggleClass('open');
        $(this).parent().parent().find(".bibtex.hidden.open").toggleClass('open');
    });
    $('a.bibtex').click(function() {
        $(this).parent().parent().find(".bibtex.hidden").toggleClass('open');
        $(this).parent().parent().find(".abstract.hidden.open").toggleClass('open');
    });
    $('a').removeClass('waves-effect waves-light');

    adjustMobileNewsHeight();
});

var newsResizeTimer;
$(window).on('resize', function() {
    clearTimeout(newsResizeTimer);
    newsResizeTimer = setTimeout(adjustMobileNewsHeight, 150);
});
