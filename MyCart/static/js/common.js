/*global $, jQuery, locache */

// common
//////////////////////////////////////////
var charts_tables_element_ids = [
        '#psi_chart_view',
    ];

var viewable_ids = [
        '#controller_home',
        '#configure_devices',
    ];

// Clears html content of charts / table elements
function clear_charts_tables_elements() {
    "use strict";
    $.each(charts_tables_element_ids, function (idx, div) {
        $(div).html('');
    });
}

// Brings `element` into focus while hiding everything else
function bring_to_focus(element_id) {
    "use strict";
    $.each(viewable_ids, function (idx, div) {
        $(div).hide();
    });
    $(element_id).show();
}

// Clears all elements & brings `element_id` into focus
function clear_to_focus(element_id) {
    "use strict";
    clear_charts_tables_elements();
    bring_to_focus(element_id);
}

// Ajax status loader
/////////////////////////////////////////
function ajax_loading() {
    "use strict";
    $('.status_ajax_loader').show();
}

function ajax_done() {
    "use strict";
    $('.status_ajax_loader').hide();
}

// Utilities
////////////////////////////////////////
function is_empty(obj) {
    "use strict";
    return jQuery.isEmptyObject(obj);
}

function no_data_message(type) {
    "use strict";
    var msg = ['<i class="fa fa-hand-o-right red"></i>',
               'No data is available. Please try a different ' + type + '!',
               '<i class="fa fa-hand-o-left red"></i>'
              ];
    return msg.join(' ');
}

function failure_message() {
    "use strict";
    var msg = ['<i class="fa fa-hand-o-right red"></i>',
               'Failure! Please try again.',
               '<i class="fa fa-hand-o-left red"></i>'
              ];
    return msg.join(' ');
}

function element_hide(element) {
    "use strict";
    $(element).hide();
}

function element_show(element) {
    "use strict";
    $(element).show();
}

function element_toggle(element) {
    "use strict";
    $(element).toggle();
}

function get_cache(key, value, timeout) {
    "use strict";
    var cached = locache.get(key);
    if (cached) {
        return cached;
    }

    value = value || 0;
    timeout = timeout || 0;

    if (timeout > 0) {
        locache.set(key, value, timeout);
    } else {
        locache.set(key, value);
    }
    return value;
}