(function ($) {
    $(document).ready(function () {
        let selected_site;
        $('#id_site').change(function() {
            let me = $(this);
            if (selected_site != undefined) {
                $('#id_page').empty();
                $('#id_panel').empty();
            }
            selected_site = me.children('option:selected').val();
        });

        let selected_page;
        $('#id_page').change(function() {
            let me = $(this);
            if (selected_page != undefined) {
                $('#id_panel').empty();
            }
            selected_page = me.children('option:selected').val();
        });
    });
})(jQuery);
