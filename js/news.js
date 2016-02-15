    $(function () {
        $('#js-news').ticker({
            htmlFeed: false,
            ajaxFeed: true,
            feedUrl: 'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
            feedType: 'xml'
        });
    });