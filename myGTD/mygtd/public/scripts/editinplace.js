Event.observe(window, 'load', init, false);


 function init(){
     var editableParent = document.getElementById('editInPlace')
     var editable = editableParent.getElementsByClassName('edit')
     for (var i=0; i < editable.length; i++) {
        makeEditable(editable[i].getAttribute('id'))
     }
 }

 function makeEditable(id){
     Event.observe(id, 'click', function(){edit($(id))}, false);
     Event.observe(id, 'mouseover', function(){showAsEditable($(id))}, false);
     Event.observe(id, 'mouseout', function(){showAsEditable($(id), true)}, false);
 }

 function showAsEditable(obj, clear){
     if (!clear){
          Element.addClassName(obj, 'editable');
     }else{
          Element.removeClassName(obj, 'editable');
     }
 }

function edit(obj){
	Element.hide(obj);

	var textarea = '<div id="'+obj.id+'_editor"><textarea id="'+obj.id+'_edit" name="'+obj.id+'" rows="4" cols="60">'+obj.innerHTML+'</textarea>';
	var button	 = '<div><input id="'+obj.id+'_save" type="button" value="SAVE" /> OR <input id="'+obj.id+'_cancel" type="button" value="CANCEL" /></div></div>';

	new Insertion.After(obj, textarea+button);

	Event.observe(obj.id+'_save', 'click', function(){saveChanges(obj)}, false);
	Event.observe(obj.id+'_cancel', 'click', function(){cleanUp(obj)}, false);

}

function cleanUp(obj, keepEditable){
     Element.remove(obj.id+'_editor');
     Element.show(obj);
     if (!keepEditable) showAsEditable(obj, true);
 }

function saveChanges(obj){

	var new_content	=  encodeURI($F(obj.id+'_edit'));

	obj.innerHTML	= "Saving...";
	cleanUp(obj, true);

	var success	= function(t){editComplete(t, obj);}
	var failure	= function(t){editFailed(t, obj);}

  	var url = '/page/editInbox';
	var pars = 'id='+obj.id+'&content='+new_content;
	var myAjax = new Ajax.Request(url, {method:'post', postBody:pars, onSuccess:success, onFailure:failure});

}

function cleanUp(obj, keepEditable){
	Element.remove(obj.id+'_editor');
	Element.show(obj);
	if (!keepEditable) showAsEditable(obj, true);
}

function editComplete(t, obj){
	obj.innerHTML	= t.responseText;
	showAsEditable(obj, true);
}

function editFailed(t, obj){
	obj.innerHTML	= 'Sorry, the update failed.';
	cleanUp(obj);
}