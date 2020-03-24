(function ($) {
    $(document).ready(function () {
        let selected_page = [];
        $('#newspage_set-group .field-page select').change(function() {
            let me = $(this);
            let id = me.attr('id');
            if (selected_page[id] != undefined) {
                let parent_id = me.attr('id').replace('id_', '').replace('-page', '');
                $('#'+parent_id).find('select').each(function(_, e) {
                    let parent = $(e);
                    if (parent.attr('id') != id) {
                        parent.empty();
                    }
                });
            }
            selected_page[id] = me.children('option:selected').val();
        });

        let selected_panel = [];
        $('#newspage_set-group .field-panel select').change(function() {
            let me = $(this);
            let id = me.attr('id');
            if (selected_panel[id] != undefined) {
                let parent_id = me.attr('id').replace('id_', '').replace('-panel', '');
                $('#'+parent_id).find('select').each(function(_, e) {
                    let parent = $(e);
                    if (parent.attr('id') == 'id_'+parent_id+'-layout') {
                        parent.empty();
                    }
                });
            }
            selected_panel[id] = me.children('option:selected').val();
        });
    });
})(jQuery);
