

function listRenderUser(user){
	var tr = $("<tr class='user'></tr>");
	tr.append("<td class='user-name'>" + user.name + "</td>");
	tr.append("<td class='user-email'>" + user.email + "</td>");
	var isAdmin = "";
	if(user.admin){
		isAdmin = "<span admin glyphicon glyphicon-ok>Yes</span>";
	}
	else{
		isAdmin = "<span glyphicon glyphicon-remove>No</span>"
	}
	tr.append("<td class='user-admin'>" + isAdmin + "</td>");
	tr.append("<td class='user-id'>" + user.id + "</td>");
	$("#user-table-body").append(tr);
}

$("tr.user").click(function(){
	$("#popup-user-name").val($(this).children(".user-name").text());
	$("#popup-email").val($(this).children(".user-email").text());
	if($(this).children(".user-admin span").hasClass("admin")){
		$("#popup-administrator").prop("checked","checked");
	}
	else{
		$("#popup-administrator").removeProp("checked");
	}
	$("#user-popup").show();
});