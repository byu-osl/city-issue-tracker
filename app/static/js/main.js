function renderIssues(issuesResponse){
	$("#issue-list").html("")
    issuesResponse.issues.forEach(listRenderIssue);
}

function listRenderIssue(issue){
	var $el = $("<li class='issue' issue-id='"+ issue.id +"'></li>");
	$el.append('<span class="glyphicon glyphicon-map-marker"></span>');
	$el.append('<span class="issue-title">'+issue.title+'</span>');
	$el.append('<span class="issue-description"> - '+issue.description +'</span>');
	if(comm.user.admin){
		$el.append('<span class="close glyphicon glyphicon-trash"></span>');
		if(!issue.open){
			$el.append('<span class="close glyphicon glyphicon-ok"></span>');
		}
	}
	$("#issue-list").append($el);
	addIssueToMap(issue);
}

$("#issue-close-button").click(function(){
	$("#issue-popup").hide();
});

$("#add-new-issue").click(function(){
	clearIssuePopup();
	$("#issue-popup").show();
});

function clearIssuePopup(){
	$("#popup-issue-title").val("");
	$("#popup-location").val("");
	$("#popup-description").val("");
	$("#popup-image").empty()
}

function saveIssue(){

}

$(".issue").click(function(){
	var issue = issues[$(this).attr("issue-id")];
	$("#popup-issue-title").val(issue.service_name);
	$("#popup-location").val(issue.address);
	$("#popup-description").val(issue.description);
	$("#popup-image").html("<img src='" + issue.media_url + "'/>");
	$("#issue-popup").show();
});

$("#search-box").keypress(function(e){
	$("#issue-list-div .panel-heading").text("Results");
	var searchString = $("#search-box").val().toLowerCase();
	if(searchString == ""){
		$(".issue").show();
		$("#issue-list-div .panel-heading").text("Recent Issues");
	}
	console.log("searchString",searchString);
	$(".issue").each(function(){
		var title = $(this).children(".issue-title").text().toLowerCase();
		if(title.indexOf(searchString) == -1){
			$(this).hide();
		}
		else{
			$(this).show();
		}
	});
});

function fetchIssues(){
	comm.getIssues().then(renderIssues)
}

fetchIssues()

onLogin.push(fetchIssues)
