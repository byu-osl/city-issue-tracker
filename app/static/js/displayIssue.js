var issuePopup = {
	$:function(){
		return $("#issue-popup");
	},
	setVisible:function(visible){
		issuePopup.$().toggleClass('target',visible);
	},
	useData:function(data){
		var latlong;
		console.log(data,data.location);
		var address = data.location ? data.location.address : ""
		if (data.lat && data.long) latlong = data.lat + " " + data.long
		$("#popup-issue-title").val(data.title || "");
		$("#popup-location").val(address);
		$("#popup-description").val(data.description || "");
		$("#popup-lat_long").val(latlong || "");
		$("#popup-image").empty()
	},
	setEditable:function(editable){
		[
			$("#popup-issue-title"),
			$("#popup-location"),
			$("#popup-description"),
			$("#popup-image"),
			$("#popup-priority")
		].forEach(function (jq) {jq.attr("disabled",!editable)});
	},
	setMode:function(isNew, isAdmin){
		var publish = isAdmin && !isNew
		var update = isAdmin && !isNew
		var submit = isNew
		var priority = isAdmin
		var footer = publish || update || submit
		
		$("#publish").toggle(publish);
		$("#update").toggle(update);
		$("#submit").toggle(submit);
		$("#edit-priority-div").toggle(priority);
		$("#issue-popup footer").toggle(footer);
		
	},
	viewIssue:function(issue){
		console.log(issue)
		if (issue.id == undefined){
			var id = issue;	
			issue = comm.issues.issues.filter(function(i){return i.id == [id]})[0];
		}
		console.log(issue);
		issuePopup.useData(issue);
		issuePopup.setEditable(false || comm.user.admin);
		issuePopup.setMode(false,comm.user.admin)
		issuePopup.setVisible(true);
	},
	addIssue:function(data){
		if (!data.priority) data.priority = "medium";
		issuePopup.useData(data);
		issuePopup.setEditable(true);
		issuePopup.setMode(true,comm.user.admin)
		issuePopup.setVisible(true);
	}
};

$("#issue-close-button").click(function(){
	issuePopup.setVisible(false);
});
