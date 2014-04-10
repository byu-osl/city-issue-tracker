var issuePopup = (function(){
	var issuePopup = {
		viewIssue:function(issue){
			console.log(issue)
			if (issue.id == undefined){
				var id = issue;	
				issue = comm.issues.issues.filter(function(i){return i.id == [id]})[0];
			}
			console.log(issue);
			useData(issue);
			setEditable(false || comm.user.admin);
			setMode(false,comm.user.admin)
			setVisible(true);
		},
		addIssue:function(data){
			if (!data.priority) data.priority = "medium";
			useData(data);
			setEditable(true);
			setMode(true,comm.user.admin)
			setVisible(true);
		}
	};
	
	// The form has no place for this - and this is the simplest solution
	var extraData = {
		"id":undefined,
		"lat":undefined,
		"long":undefined,
		"approved":undefined
	};
	
	function setVisible(visible){
		$("#issue-popup").toggleClass('target',visible);
	}
	
	//private
	function useData(data){
			var address;
			if (data.location){
				extraData.lat = data.location.lat 
				extraData.long = data.location.long;
				address = data.location.address;
			}
			extraData.id = data.id;
			extraData.approved = data.approved;
			extraData.open = data.open;
			$("#popup-issue-title").val(data.title || "");
			$("#popup-location").val(address);
			$("#popup-description").val(data.description || "");
			$("#popup-image").empty()
			
			$("#popup-image").empty()
	}
	
	// private
	function setEditable(editable){
		[
			$("#popup-issue-title"),
			$("#popup-location"),
			$("#popup-description"),
			$("#popup-image"),
			$("#popup-priority")
		].forEach(function (jq) {jq.attr("disabled",!editable)});
	}
	
	// private
	function setMode(isNew, isAdmin){
		var publish = isAdmin && !isNew && !extraData.approved
		var update = isAdmin && !isNew
		var submit = isNew
		var priority = isAdmin
		var footer = publish || update || submit
		
		$("#publish").toggle(publish);
		$("#update").toggle(update);
		$("#submit").toggle(submit);
		$("#edit-priority-div").toggle(priority);
		$("#issue-popup footer").toggle(footer);
		
	}
	
	// private 
	function updateIssue(){
		var issue = extractIssue();
		comm.updateIssue(issue.id, issue).then(
			function success(){
				setVisible(false);
				// TODO: Fix the alert to make it another dialog
				alert("Issue updated successfully");
				// TODO: FIX ME!!! so very bad. This shouldn't be refering to manageIssues.js
				manageIssues.updateIssue(issue);
			},
			function failure(err){
				alert("There was an error communicating with the server.");
				console.log(err, "time");
			}
		)
	}
	
	// private 
	function submitIssue(){
		var issue = extractIssue();
		comm.createIssue(issue).then(
			function success(){
				issuePopup.setVisible(false);
				// TODO: Fix the alert to make it another dialog
				alert("Issue submitted successfully. It is now pending review.");
			},
			function failure(err){
				alert("There was an error communicating with the server.");
				console.log(err, "time");
			}
		)
	}
	
	// private 
	function approveIssue(){
		var id = extraData.id
		comm.updateIssue(id, {"approved":true}).then(
			function success(){
				$("#publish").hide();	
				// TODO: Fix the alert to make it another dialog
				alert("Issue updated successfully");
				// TODO: FIX ME!!! so very bad. This shouldn't be refering to manageIssues.js
				manageIssues.updateIssue(issue);
			},
			function failure(err){
				alert("There was an error communicating with the server.");
				console.log(err, "time");
			}
		)
	}
	
	//private
	function extractIssue(){
		var issue = {
			"id":extraData.id,
			"approved":extraData.approved,
			"open":extraData.open,
			"title": $("#popup-issue-title").val() || undefined,
			"location": {
				"address":$("#popup-location").val() || undefined,
				"lat":extraData.lat,
				"long":extraData.long
			},
			"priority":$("#popup-priority").val() || undefined,
			"description":$("#popup-description").val() || undefined
		}
		return issue;
	}

	$("#issue-close-button").click(function(){
		setVisible(false);
	});
	
	$("#update").on('click',updateIssue);
	$("#submit").on('click',submitIssue);
	$("#publish").on('click',approveIssue);
	
	issuePopup.issue = extractIssue;
	
	return issuePopup;
}())
