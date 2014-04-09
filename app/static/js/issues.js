var issuePopup = {
	$:function(){
		return $("#issue-popup");
	},
	setVisible:function(visible){
		if (visible) this.$().show();
		else this.$().hide();
	},
	useData:function(data){
		var latlong;
		if (data.lat && data.long) latlong = data.lat + " " + data.long
		$("#popup-issue-title").val(data.title || "");
		$("#popup-address").val(data.address || "");
		$("#popup-description").val(data.description || "");
		$("#popup-lat_long").val(latlong || "");
		$("#popup-image").empty()
	},
	setEditable:function(editable, showAdminOptions){
		[
			$("#popup-issue-title"),
			$("#popup-location"),
			$("#popup-description"),
			$("#popup-image"),
			$("#popup-priority")
		].forEach(function (jq) {jq.attr("disabled",!editable)});
		if (showAdminOptions){
			$("#edit-priority-div").show();
			$("#publish").show();
			$("#save").show();
		}
		else {
			$("#edit-priority-div").hide();
			$("#publish").hide();
			$("#save").hide();
		}
	}
};

function startAddIssue(data){
	issuePopup.useData(data)
	issuePopup.setEditable(true,comm.user.admin)
	issuePopup.setVisible(true);
}
