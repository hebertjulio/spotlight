(function ($) {
    $(document).ready(function () {
        let selected_site;
        $('#id_site').change(function() {
            let me = $(this);
            if (selected_site != undefined) {
                $('#id_editorials').empty();
                $('#newspage_set-group').find('select').empty();
            }
            selected_site = me.children('option:selected').val();
        });

        let image_field = $('.form-row.field-image>div>p>a');
        let thumbnail_field = $('.form-row.field-thumbnail');
        if (thumbnail_field.length > 0 && image_field.length < 1) {
            thumbnail_field.hide();
        }
    });
})(jQuery);
