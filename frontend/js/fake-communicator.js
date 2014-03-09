///////////////////////////////////////////////////////////////////////
//////  The fake communicator can be used while the backend team is 
/////  getting ready. It uses the fake data generator, and it 
////  uses actual date objects instead of date strings
///
// It also ignores any extra queries on the get issues (ie, offset, sort, etc)
//////////////////////////////////////////////////////////////////////

FakeCommunicator = (function communicator_namespace() {
  
    function getList(gen, num){
        var l = [];
        for (var x = 0; x < num; x++){
            l.push(gen.next());
        }
        return l;
    }

    function dupShallow(obj){
        var item = {};
        for (key in obj){
            item[key] = obj[key];
        }
        return item;
    }
    
    function passwordless(users){
        return self.users.map(function (u){
            var user = dupShallow(u)
            delete user.password
            return user
        })
    }
    
    function asArrayResponse(arr, name){
        deets = {
            "total_results": arr.length,
            "total_returned": arr.length,
            "offset": 0
        };
        deets[name] = arr;
        return deets;
    }
    
    // The actual class

    function FakeCommunicator(fakeGenerator, fakeUserGenerator) {
        this.issues = getList(fakeGenerator, 20);
        this.users = [
            fakeUserGenerator.next(true,"Phil"),
            fakeUserGenerator.next(false,"Bob")
        ].concat(getList(fakeUserGenerator, 18));
        this.user = undefined;
    }

  
    // Private
  
    function getUserByName(val){
        return this.users.filter(function(user){
            return user.email == val;
        });
    }
  
  
    // Account create/view/edit
  
    FakeCommunicator.prototype.createAccount = function(account) {
        var self = this;
        var conflict = getUserByName.call(self,account.email)[0];
        return new Promise(function(resolve, reject){
            if (conflict){
                reject(Error("That email is already taken"));
            } else {
                // the id started at 0
                account.id = this.users.length;
                this.users.push(account);
                resolve("Success");
            }
        });
    };
    
    FakeCommunicator.prototype.getAccounts = function() {
        var admin = self.user && self.user.admin;
        var users = self.users
        return new Promise(function(resolve, reject){
            if (admin){
                resolve(asArrayResponse(passwordless(users),"users"));
            }else{
                reject(Error("You are not an admin"));
            }
        });
    };
  
    FakeCommunicator.prototype.updateAccount = function(id, account) {
        var toEdit = self.users[id];
        var user = this.user;
        var conflict = getUsersByEmail.call(this, account.email)[0]
        return new Promise(function(resolve, reject){
            if (!toEdit){
                reject(Error("Bad ID"));
            } else if (!user){
                reject(Error("Not logged in"));
            } else if (conflict){
                reject(Error("Can't switch to that email - it's taken"));
            } else if ((account.admin != toEdit.admin) && !user.admin){
                reject(Error("You are not an admin - you cannot give admin priveleges."));
            } else {
                toEdit.name = account.name;
                toEdit.admin = account.admin;
                resolve("Success");
            }
        });
    };
    
    // Sign-in/out
    
    FakeCommunicator.prototype.signIn = function(credentials) {
        var self = this;
        var user = getUserByName.call(self,credentials.email)[0];
        return new Promise(function(resolve, reject){
            if (self.user){
                reject(Error("You're already logged in."));
            } else if (user && (user.password == credentials.password)){
                self.user = user;
                resolve("Success!");
            } else {
                reject(Error("Incorrect email/password combination"));
            }
        });
    };
  
    FakeCommunicator.prototype.signOut = function() {
        var self = this;
        return new Promise(function(resolve, reject){
            if (self.user){
                self.user = undefined;
                resolve("Success!");
            } else {
                reject(Error("You weren't logged in."));
            }
        });
    };
  
  
  
  
    //-----------------------------------------------------------
    //    ISSUES
    //----------------------------------------------------------

    // issue creation & view    
    FakeCommunicator.prototype.createIssue = function(details) {
        var newIssue = dupShallow(details);
        var issues = this.issues
        var user = this.user;
        return new Promise(function(resolve, reject){
            if (user){
                newIssue.id = issues.length;
                newIssue.approved = false;
                newIssue.open = false;
                newIssue.owner = user.email;
                newIssue.created_at = Date.now();
                newIssue.updated_at = newIssue.created_at;
                
                issues.push(newIssue);  
                resolve(newIssue.id);
            } else {
                reject(Error("Must be logged into to submit a report."))
            }
        });
    };
    
    FakeCommunicator.prototype.getIssue = function(id) {
        var user = this.user;
        var issue = dupShallow(this.issues[id])
        return new Promise(function(resolve, reject){
            if (issue && user && user.admin){
                resolve(issue)
            } else if (issue && issue.approved) {
                delete issue.owner;
                resolve(issue);
            } else {
                reject(Error("No issues with that ID could be found: " + id));
            }
        });
    };
  
    //retreives a list of issues
    FakeCommunicator.prototype.getIssues = function(orderBy, offset, max, query, reversed) {
        var issues = this.issues.map(dupShallow);
        var admin = self.user && self.user.admin
        return new Promise(function(resolve, reject){
            if (admin){
                resolve(asArrayResponse(issues,"issues"));
            } else {
                console.log(issues, issues.filter(function(issue){
                        return issue.approved;
                    }))
                resolve(asArrayResponse(
                    issues
                    .filter(function(issue){
                        return issue.approved;
                    })
                    .map(function(issue){
                        delete issue.owner;
                        return issue;
                    }), "issues"
                ));
            }
        });
    };
    
    //submits a photo
    FakeCommunicator.prototype.submitPhoto = function(image) {
        var user = this.user;
        return new Promise(function(resolve, reject){
            if (user){
                resolve("http://lorempixel.com/600/600/sports/");
            } else {
                reject(Error("You must be logged in."));
            }
        });
    };  
    
    //Adds a note (admin only)
    FakeCommunicator.prototype.addNote = function(id, note) {
        var issue = this.issues[id];
        var admin = this.user && this.user.admin
        return new Promise(function(resolve, reject){
            if (admin){
                if (issue){
                    issue.notes.push({
                        data:Date.now(),
                        note:note
                    });
                    resolve("Success!");
                } else {
                    reject("No issue with that id found.")
                }
            } else {
                reject("You are not an admin.")
            }
        });
    };
    
    // ADMIN only
    FakeCommunicator.prototype.updateIssue = function(id, details) {
        var issue = this.issues[id];
        var admin = this.user && this.user.admin
        return new Promise(function(resolve, reject){
            if (admin){
                if (issue){
                    for (key in details){
                        issue[key] = details[key];
                    }
                    issue.update_at = Date.now();
                    resolve("Success!");
                } else {
                    reject("No issue with that id found: " + id)
                }
            } else {
                reject("You are not an admin.")
            }
        });
    };

  return FakeCommunicator;
}());
