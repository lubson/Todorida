YAHOO.namespace("example.container");
	function init() {
		// Build taskForm based on markup, initially hidden, fixed to the center of the viewport, and 300px wide
	    YAHOO.example.container.taskForm = new YAHOO.widget.Overlay("taskForm", { fixedcenter:true,
	                                                                              visible:false,
       	                                                                          width:"320px" } );
	    YAHOO.example.container.taskForm.render();

        YAHOO.example.container.projectForm = new YAHOO.widget.Overlay("projectForm", { fixedcenter:true,
	                                                                              visible:false,
       	                                                                          width:"320px" } );
	    YAHOO.example.container.projectForm.render();

		YAHOO.util.Event.addListener("showTaskForm", "click", YAHOO.example.container.taskForm.show, YAHOO.example.container.taskForm, true);
        YAHOO.util.Event.addListener("showTaskForm", "click", YAHOO.example.container.projectForm.hide, YAHOO.example.container.projectForm, true);
		YAHOO.util.Event.addListener("hideTaskForm", "click", YAHOO.example.container.taskForm.hide, YAHOO.example.container.taskForm, true);

        YAHOO.util.Event.addListener("showProjectForm", "click", YAHOO.example.container.projectForm.show, YAHOO.example.container.projectForm, true);
        YAHOO.util.Event.addListener("showProjectForm", "click", YAHOO.example.container.taskForm.hide, YAHOO.example.container.taskForm, true);
        YAHOO.util.Event.addListener("hideProjectForm", "click", YAHOO.example.container.projectForm.hide, YAHOO.example.container.projectForm, true);
	}
	YAHOO.util.Event.addListener(window, "load", init);