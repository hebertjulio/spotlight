(function ($) {
    $(document).ready(function () {
        let selected_site;
        $('#id_site').change(function() {
            let me = $(this);
            if (selected_site != undefined) {
                $('#id_page').empty();
            }
            selected_site = me.children('option:selected').val();
        });
    });
})(jQuery);
