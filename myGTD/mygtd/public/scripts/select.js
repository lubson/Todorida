function callAjax(url, field, replace) {
    var callback = {
        success: function(o) {
            YAHOO.util.Dom.get(replace).innerHTML = o.responseText;
        },
        failure: function(o) {
            alert("Failed to retrieve required information.");
        }
    }
    url = url + '?realm_id=' + YAHOO.util.Dom.get(task_realm_id).value;
    var transaction = YAHOO.util.Connect.asyncRequest('GET', url, callback, null);
}