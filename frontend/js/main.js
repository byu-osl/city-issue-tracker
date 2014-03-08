var issues = {};
var user = {"name":"Steve","id":1,"isAdmin":true};

var g = new Generator();
// var u = new Users();
// var c = new FakeCommunicator(new Generator(), new Users());

for(var i = 0; i < 10; i++){
  var issue = g.next();
  issue.id = i;
  issues[i] = issue;
  listRenderIssue(issue);
}

function listRenderIssue(issue){
  var $el = $("<li class='issue' issue-id='"+ issue.id +"'></li>");
  $el.append('<span class="glyphicon glyphicon-map-marker"></span>');
  $el.append('<span class="issue-title">'+issue.service_name+'</span>');
  $el.append('<span class="issue-description"> - '+issue.description +'</span>');
  if(user.isAdmin){
    $el.append('<span class="close glyphicon glyphicon-trash"></span>');
    if(issue.status == "close"){
      $el.append('<span class="close glyphicon glyphicon-ok"></span>');
    }
  }
  $("#issue-list").append($el);
}

$(".close-button").click(function(){
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
