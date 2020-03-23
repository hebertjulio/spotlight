(function ($) {
    $(document).ready(function () {
        let selected_site;
        $('#id_site').change(function() {
            let me = $(this);
            if (selected_site != undefined) {
                $('#id_editorial').empty();
                $('#id_section').empty();
                $('#id_layout').empty();
                $('#id_override').empty();
            }
            selected_site = me.children('option:selected').val();
        });

        let selected_section;
        $('#id_section').change(function() {
            let me = $(this);
            if (selected_section != undefined) {
                $('#id_layout').empty();
                $('#id_override').empty();
            }
            selected_section = me.children('option:selected').val();
        });
    });
})(jQuery);
