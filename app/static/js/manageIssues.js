var manageIssues = (function(){
    
    function id(issue_dom){
        return $(issue_dom).attr("issue-id");
    }
    
    function bindShowFunction(){
        $(".issue").on("click",function(){
            console.log("HERE")
            console.log(id(this));
            issuePopup.viewIssue($(this).attr("issue-id"));
        });
    }
    
    function renderSingle(issue){
        var $el = $("<li class='issue' issue-id='"+ issue.id +"'></li>");
        renderListItemContents($el,issue);
        $("#issue-list").append($el);
        mapView.add(issue);
    }
    
    function makeCheck(issue){
        var color = issue.open ? "gray" : "green";
        var check = $('<span class="close glyphicon glyphicon-ok"></span>');
        check.attr('style','color:'+color);
        check.on('click',function(event){
            event.stopPropagation();
            alert("Insert stuff here about closing with a note.");
            return false;
        });
        return check;
    }
    
    function makeEye(issue){
        var color = issue.approved ? "black" : "gray";
        var eye = $('<span class="close glyphicon"></span>');
        eye.attr('style','color:'+color);
        eye.toggleClass("glyphicon-eye-open", issue.approved);
        eye.toggleClass("glyphicon-eye-close", !issue.approved);
        eye.on('click',function(event){
            event.stopPropagation();
            comm.updateIssue(issue.id,{approved:true}).then(function(){
                issue.approved = true; 
                updateIssue(issue);
            })
            return false;
        });
        return eye;
    }
    
    function renderListItemContents($el,issue){
        $el.append('<span class="glyphicon glyphicon-map-marker"></span>');
        $el.append('<span class="issue-title">'+issue.title+'</span>');
        $el.append('<span class="issue-description"> - '+issue.description +'</span>');
        if(comm.user.admin){
            $el.append(makeEye(issue));
            $el.append(makeCheck(issue));
        }
    }
    
    function updateIssue(issue){
        var $el = $("[issue-id='"+ issue.id +"']");
        $el.html("");
        renderListItemContents($el,issue);
        mapView.add(issue);
    }
    
    $("#search-box").keyup(function(e){
        $("#issue-list-div .panel-heading").text("Results");
        var searchString = $("#search-box").val().toLowerCase();
        if(searchString == ""){
            $(".issue").show();
            $("#issue-list-div .panel-heading").text("Recent Issues");
        }
        
        $(".issue").each(function(){
            var title = $(this).children(".issue-title").text().toLowerCase();
            if(title.indexOf(searchString) == -1){
                $(this).hide();
                mapView.hide(id(this))
            }
            else{
                $(this).show();
                console.log(this,id(this));
                mapView.show(id(this))
            }
        });
    });
    
    $("#add-new-issue").click(function(){
        issuePopup.addIssue({});
    });
    
    var controller = {
        updateIssue:updateIssue,
        renderResponse:function(issuesResponse){
            console.log("here",this);
            $("#issue-list").html("")
            issuesResponse.issues.forEach(renderSingle);
            bindShowFunction()	
        },        
        updateFromServer:function(){
            comm.getIssues().then(this.renderResponse.bind(this));
        }
    }
    
    var updateFunction = controller.updateFromServer.bind(controller); 
        
    onLogin.push(updateFunction)
    onLogin.push(function(){
        $("#add-new-issue").show();
    })
    onLogout.push(updateFunction);
    onLogout.push(function(){
        $("#add-new-issue").hide();
    })  
    return controller;
}())
