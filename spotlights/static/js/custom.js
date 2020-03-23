(function ($) {
    $(document).ready(function () {
        let selected_site;
        $('#id_site').change(function() {
            let me = $(this);
            if (selected_site != undefined) {
                $('#id_page').empty();
                $('#id_editorials').empty();
                $('#id_panel').empty();
                $('#id_layout').empty();
                $('#id_supersede').empty();
            }
            selected_site = me.children('option:selected').val();
        });

        let selected_page;
        $('#id_page').change(function() {
            let me = $(this);
            if (selected_page != undefined) {
                $('#id_editorials').empty();
            }
            selected_page = me.children('option:selected').val();
        });

        let selected_panel;
        $('#id_panel').change(function() {
            let me = $(this);
            if (selected_panel != undefined) {
                $('#id_layout').empty();
                $('#id_supersede').empty();
            }
            selected_panel = me.children('option:selected').val();
        });

        let image_field = $('.form-row.field-image>div>p>a');
        let thumbnail_field = $('.form-row.field-thumbnail');
        if (thumbnail_field.length > 0 && image_field.length < 1) {
            thumbnail_field.hide();
        }
    });
})(jQuery);
