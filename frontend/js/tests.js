// This script presumes qunit.js


(function generator_tests(){
    

    function generateAndCheck(users, admin, name){
        var u = users.next(admin, name)
        u.should.have.property("name", name)
        u.should.have.property("admin", admin)
    }

    describe('User', function(){
      describe('#next()', function(){
        users = new Users();
        it('should generate users according to parameters', function(){
            generateAndCheck(users, false, "George")
            generateAndCheck(users, true, "Hanna")
        })
      })
    })
    /*
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
    });*/
    
}());
