function fillProjectForm(id, name, note, due, realm_id, state) {
    formWrapper = YAHOO.util.Dom.get("projectForm");
    form = formWrapper.getElementsByTagName('form')[0];

    inputs = form.getElementsByTagName('input');

    textArea = form.getElementsByTagName('textarea')[0];

    selects = form.getElementsByTagName('select');

    inputs[0].setValue(id);
    inputs[1].setValue(name);
    textArea.setValue(note);
    inputs[3].setValue(convertDate(due));
    selects[0].setValue(realm_id);
    selects[1].setValue(state);

    button = YAHOO.util.Dom.get("showProjectForm");
    button.click();
}

function convertDate(date){
    if (date.length > 0){
        date = date[8]+date[9]+'-'+date[5]+date[6]+'-'+date[0]+date[1]+date[2]+date[3];
    }
    return date;
}