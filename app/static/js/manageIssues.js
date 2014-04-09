var manageIssues = (function(){
    
    function bindShowFunction(){
        $(".issue").on("click",function(){
            console.log("HERE")
            console.log($(this).attr("issue-id"));
            var issue = comm.issues.issues.filter(function(i){return i.id == [$(this).attr("issue-id")]},this)[0];
            issuePopup.setEditable(comm.user.admin, comm.user.admin);
            issuePopup.useData(issue);
            issuePopup.setVisible(true);
        });
    }
    
    function renderSingle(issue){
        var $el = $("<li class='issue' issue-id='"+ issue.id +"'></li>");
        $el.append('<span class="glyphicon glyphicon-map-marker"></span>');
        $el.append('<span class="issue-title">'+issue.title+'</span>');
        $el.append('<span class="issue-description"> - '+issue.description +'</span>');
        if(comm.user.admin){
            var color = issue.open ? "green" : "gray";
            var check = $('<span class="close glyphicon glyphicon-ok"></span>');
            check.attr('style','color:'+color);
            check.on('click',function(event){
                event.stopPropagation();
                comm.updateIssue(issue.id,{approved:true}).then(function(){
                    check.attr('style','color:green');
                })
                return false;
            })
            $el.append(check);
        }
        $("#issue-list").append($el);
        addIssueToMap(issue);
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
            }
            else{
                $(this).show();
            }
        });
    });
    
    $("#add-new-issue").click(function(){
        startAddIssue({});
    });
    
    var controller = {
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
        
    onLogin.push(controller.updateFromServer.bind(controller))
    onLogin.push(function(){
        $("#add-new-issue").show();
    })
    
    onLogout.push(function(){
        $("#add-new-issue").hide();
    })  
    return controller;
}())
