// This script presumes mocha, chai, mocha-as-promised and chai-as-promised
(function generator_tests() {

    var should = chai.should()

        function generateAndCheck(users, admin, name) {
            u = users.next(admin, name);
            u.should.have.property("name")
                .that.equals(name);
            u.should.have.property("admin")
                .that.equals(admin);
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
    
    function login(comm, email, pass){
        return comm.signIn({email:email, password:pass})
                .then(function(){ return comm; });
    }
    
    function login_admin(comm){
        return login(comm, "Phil@haha.jk", "phil")
    }
    
    function login_normal(comm){
        return login(comm, "Phil@haha.jk", "phil")
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

    describe('Fake-Communicator', function () {
        describe('LOGGED OUT BEHAVIOR', function () {
            describe('#signIn()', function () {
                it('should sign you in', function () {
                    var comm = new FakeCommunicator(new Generator(), new Users())
                    var userPromise = comm.signIn({
                        email: "Phil@haha.jk",
                        password: "phil"
                    });
                    return userPromise
                })
            });
            
            describe('#issues()', function () {
                it('should get approved issues for you', function () {
                    var comm = new FakeCommunicator(new Generator(), new Users())
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
        })
        
        describe('THE ISSUES CYCLE', function () {
            var comm = new FakeCommunicator(new Generator(), new Users())
            var issueID
            var oracleIssue = new Generator().next();
            
            describe('$submit & check', function () {
                it('sign in as bob (normal user)', function () {
                    return login(comm,"Bob@haha.jk","bob")
                });
                it('submit the issues [as bob]',function(){
                    oracleIssue.open = false;
                    oracleIssue.approved = true;
                    var response = comm.createIssue(oracleIssue);
                    response.should.eventually.be.a("number")
                    response.then(function(id){
                        issueID = id;
                    })
                })
                it('check the issue [as bob] and fail (right?)',function(){
                    oracleIssue.open = false;
                    oracleIssue.approved = false;
                    return checkIssue(comm.getIssue(issueID),issueID, oracleIssue);
                })
                it('logout [bob]',function(){
                    return comm.signOut();
                })
            });
            
            describe('$mark approved; check as admin', function () {
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
                it('logout [phil]',function(){
                    return comm.signOut();
                })
            });
            
            describe('$check as anyone', function (){ 
                it('check the issue [as bob] and fail (right?)',function(){
                    return checkIssue(comm.getIssue(issueID),issueID, oracleIssue,true,true);
                })
            })
        });
        
        

        describe('#signout()', function () {
            it('should sign you in', function () {
                var comm = new FakeCommunicator(new Generator(), new Users())
                return login(comm, "Phil@haha.jk","phil").then(function(){return comm.signOut();})
            })
        });
        

    });


}());
