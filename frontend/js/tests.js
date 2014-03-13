// This script presumes mocha, chai, mocha-as-promised and chai-as-promised
(function generator_tests(comm) {
	
	// There are 3 states: not logged in, logged in admin, logged in user.
	// There are 4 issue states: not created, unapproved, approved, closed.
	
	// Setting up for the tests:
	//    Add a user
	//    Add in issues:
	//    	Not created
	//		Unapproved
	// 		Approved
	// 		Closed
	//
	
	// Testing:
	//  Test all logged out behavior (easy - view issues , sign in, create account - they should work)
	//  Test user capabilities (sign in, sign out, adding an issue, update account, view account, add photo)
	//  Test admin capabilities (approve issues, update any account, add note, view any account)
	//  Things not mentioned in a level or above should fail
	
	

    var should = chai.should()
    
    var admin ={
		email:"Phil@haha.jk",
		password:"phil"
	}
	
	var normal ={
		email:"Bob@haha.jk",
		password:"bob"
	}

	function generateAndCheck(users, admin, name) {
		u = users.next(admin, name);
		u.should.have.property("name")
			.that.equals(name);
		u.should.have.property("admin")
			.that.equals(admin);
	}
    
    function login(comm, email, pass){
        return comm.signIn({email:email, password:pass})
                .then(function(){ return comm; });
    }
    
    function login_admin(comm){
        return login(comm, admin.email, admin.password)
    }
    
    function login_normal(comm){
        return login(comm, normal.email, normal.password )
    }
    
    function eventualPropertyValue(obj, propName, val){
        return obj.eventually.should.have.property(propName).that.is(val)
    }
    
    function checkIssue(issue, id, oracle, approved, open){
        var noCheckKeys = ['id','open','approved','created_at','updated_at','owner']
        var conditions = []
        if (id != undefined) {
            conditions.push( issue.should.eventually.have.property('id').that.equals(id) );
        }
        if (oracle) 
            conditions = conditions.concat(Object.keys(oracle).filter(function(key){
                return noCheckKeys.indexOf(key) < 0;
            })            
            .map(function(key){
                return issue.should.eventually.have.property(key).that.equals(oracle[key])
            }));
        if (approved != undefined) conditions.push(
            issue.should.eventually.have.property('approved').that.equals(approved)
        );
        if (open != undefined) conditions.push(
            issue.should.eventually.have.property('open').that.equals(open)
        );
        return Promise.all(conditions)
    }
    
    describe('User', function () {
        describe('#next()', function () {
            users = new Users();
            it('should generate users according to parameters', function () {
                generateAndCheck(users, false, "George")
                generateAndCheck(users, true, "Hanna")
            })
        })
    });

    describe('Fake-Communicator', function () {
        describe('Sign in/out', function () {
			var userPromise;
            describe('#signIn()', function () {
                it('should sign you in', function () {
                    userPromise = comm.signIn({
                        email: "Phil@haha.jk",
                        password: "phil"
                    });
                    return userPromise;
                })
            });
            describe('#signOut()', function () {
				it('should sign you out', function () {
					return userPromise.then(function(){return comm.signOut();})
				})
			})
        }) 
        
        describe('Signed out behavior', function () {
            describe('#createAccount()', function () {
                it("should create an account", function () {
					var registerResponse = comm.createAccount({
							email:"asdfqwer_asdfqwerNNNN@asdfJAJAJA.net",
							password:"I_am_a_test",
							name:"Mr. Test"						
						})
					return registerResponse;
                })
            });
            describe('#getCurrentAccount()', function () {
                it("should not work - you're not logged in.", function () {
					var accountsResponse = comm.getAccount();
					return accountsResponse.should.eventually.be.rejected;
                })
            });
            describe('#getAccount()', function () {
                it("should not work - you're not logged in.", function () {
					var accountsResponse = comm.getAccount(0);
					return accountsResponse.should.eventually.be.rejected;
                })
            });
            describe('#getAccounts()', function () {
                it("should not work - you're not logged in.", function () {
					var accountsResponse = comm.getAccounts();
					return accountsResponse.should.eventually.be.rejected;
                })
            });
            describe('#updateAccount()', function () {
                it("should not work - you're not logged in.", function () {
					var registerResponse = comm.updateAccount(0,{
							password:"asdasdfasdf"					
						})
					return registerResponse.should.eventually.be.rejected;
                })
            });
            
            
            
			describe('#createIssue()', function () {
                it('should fail to create an issue (not logged in)', function () {
                     var oracleIssue = new Generator().next();
                     var responsePromise = comm.createIssue(oracleIssue);
                     return responsePromise.should.eventually.be.rejected;
                })
            });
            
			describe('#getIssue()', function () {
                it('should get an approved issue', function () {
                     return comm.getIssue(0);
                })
            });
            
			describe('#getIssues() [ Still needs work - needs to check to see if all issues are approved ]', function () {
                it('should get approved issues for you', function () {
                    var issuesResponse = comm.getIssues()
                    var issuesArr = issuesResponse.should.eventually.have.property("issues")
                    var issue0 = issuesArr.should.eventually.have.property(0)
                    return Promise.all([
                        issuesResponse.should.eventually.be.an("object"),
                        issuesResponse.should.eventually.have.property("offset").that.is.a("number"),
                        issuesResponse.should.eventually.have.property("total_results").that.is.a("number"),
                        issuesResponse.should.eventually.have.property("total_returned").that.is.a("number"),
                        issuesArr.should.eventually.be.an("array")
                    ])
                })
            });
            
			describe('#updateIssue()', function () {
                it("should not update the issue - you're not logged in.", function () {
                    var issuesResponse = comm.updateIssue(0,{open:false});
                    return issuesResponse.should.eventually.be.rejected;
                })
            });
            
			describe('#submitPhoto()', function () {
                it("should not update the issue - you're not logged in.", function () {
                    var submissionResponse = comm.submitPhoto("asdfasdfasdf");
                    return submissionResponse.should.eventually.be.rejected;
                })
            });            
        })
        
        describe('THE ISSUES CYCLE', function () {
            var issueID
            var oracleIssue = new Generator().next();
            
            describe('$  submit & check', function () {
                it('sign in as normal user', function () {
                    return login(comm,normal.email, normal.password)
                });
                it('submit the issues [as normal user]',function(){
                    oracleIssue.open = false;
                    oracleIssue.approved = true;
                    var response = comm.createIssue(oracleIssue);
                    response.should.eventually.be.a("number")
                    response.then(function(id){
                        issueID = id;
                    })
                })
                it('check the issue [as normal user] and fail (right?)',function(){
                    oracleIssue.open = false;
                    oracleIssue.approved = false;
                    return checkIssue(comm.getIssue(issueID),issueID, oracleIssue).should.be.rejected;
                })
                it('logout [normal user]',function(){
                    return comm.signOut();
                })
            });
            
            describe('$  mark approved; check as admin', function () {
                it('sign in as phil', function () {
                    return login_admin(comm)
                });
                it('check the issue and succeed (unapproved)',function(){
                    return checkIssue(comm.getIssue(issueID),issueID, oracleIssue, false, false);
                });
                it('approve the issue', function(){
                    return comm.updateIssue(issueID, {approved:true, open:true });
                });
                it('check the issue and succeed (approved)',function(){
                    return checkIssue(comm.getIssue(issueID),issueID, oracleIssue, true, true);
                });
                it('logout [admin]',function(){
                    return comm.signOut();
                })
            });
            
            describe('$  check as anyone [post approval]', function (){ 
                it('check the issue [not logged in] and succeed',function(){
                    return checkIssue(comm.getIssue(issueID),issueID, oracleIssue,true,true);
                })
            })
        });        

    });


}(new FakeCommunicator(new Generator(), new Users())));
