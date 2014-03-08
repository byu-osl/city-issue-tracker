///////////////////////////////////////////////////////////////////////
//////  The fake communicator can be used while the backend team is 
/////  getting ready. It uses the fake data generator, and it 
////  uses actual date objects instead of date strings
///
// It also ignores any extra queries on the get issues (ie, offset, sort, etc)
//////////////////////////////////////////////////////////////////////

FakeCommunicator = (function communicator_namespace() {
  
    // Utility Functions
    function getObject(gen,num){
        var items = {};
        getList(gen, num).map(function(item){
            items[item.id] = item;
        });
        return items;
    }

    function getList(gen, num){
        var l = [];
        for (var x = 0; x < num; num++){
            l.push(gen.next());
        }
        return l;
    }

    function asList(obj){
        return Object.prototype.keys.call(obj).map(function(key){return obj.key;});
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
    
    function asArrayResponse(obj, name){
        deets = {
            "total_results": number,
            "total_returned": number,
            "offset": number
        }
        deets[name] = obj
        return deets
    }
    
    // The actual class

    function FakeCommunicator(fakeGenerator, fakeUserGenerator) {
        this.issues = getObject(fakeGenerator, 20);
        this.users = getList(fakeUserGenerator, 20);
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
        var user = getUserByName.call(self,account.email)[0];
        return new Promise(function(resolve, reject){
            if (self.user){
                reject(Error("You're already logged in."));
            } else if (user && (user.password == credentials.password)){
                resolve("Success!");
            } else {
                reject(Error("Incorrect email/password combination"));
            }
        });
    };
  
    FakeCommunicator.prototype.signOut = function() {
        var self;
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
        details = dupShallow(details);
        var issues = this.issues
        var user = this.user;
        return new Promise(function(resolve, reject){
            if (user){
                details.id = issues.length;
                details.public = false;
                details.owner = user.email;
                details.created_at = Date.now();
                details.updated_at = details.created_at;
                issues.push(details);  
                resolve(details.id);
            } else {
                reject(Error("Must be logged into to submit a report."))
            }
        });
    };
    
    FakeCommunicator.prototype.getIssue = function(id) {
        var user = this.user;
        var issue = dupShallow(self.issues[id])
        return new Promise(function(resolve, reject){
            if (issue && user && user.admin){
                resolve(issue)
            } else if (issue && issue.public) {
                delete issue.public;
                delete issue.owner;
                resolve(issue);
            } else {
                reject(Error("No issues with that ID could be found"));
            }
        });
    };
  
    //retreives a list of issues
    FakeCommunicator.prototype.getIssues = function(orderBy, offset, max, query, reversed) {
        var issues = this.issues.map(dupShallow);
        var admin = self.user && self.user.admin
        return new Promise(function(resolve, reject){
            if (admin){
                resolve(asArrayResponse(issues));
            } else {
                resolve(asArrayResponse(
                    issues
                    .filter(function(issue){
                        return issues.public;
                    })
                    .map(function(issue){
                        delete issue.owner;
                        delete issue.public;
                        return issue;
                    })
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
        return new Promise(function(resolve, reject){
            if (admin){
                if (issue){
                    for (key in details){
                        issue[key] = details[key];
                    }
                    issue.update_at = Date.now();
                    resolve("Success!");
                } else {
                    reject("No issue with that id found.")
                }
            } else {
                reject("You are not an admin.")
            }
        });
    };

  return FakeCommunicator;
}());
