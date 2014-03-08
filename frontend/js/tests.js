// This script presumes qunit.js

(function generator_tests(){
    function genDU(users, admin, name){
        var u = users.next(admin, name)
        equal(u.name, name)
        equal(u.admin, admin)
    }
    
    
    test( "Generating Users", function() {
        var users = new Users();
        
        genDU(users, false, "George")
        genDU(users, true, "Hanna")
    });
    
    function signin(){
        var comm = new FakeCommunicator(new Generator(), new Users())
        comm.signIn({email:"Phil@haha.jk",password:"phil"}).then(function(result){
            ok(comm.user, "Login successful")
        }, function(){
            ok(comm.user, "Login unsuccessful")
        })
        return comm
    }
    
    test("Fake Communicator - User Login", function(){
        signin()
    });
    
}());
