// This script presumes mocha, chai, mocha-as-promised and chai-as-promised

(function generator_tests(){

    var should = chai.should()

    function generateAndCheck(users, admin, name){
        u = users.next(admin,name);
        u.should.have.property("name").that.equals(name);
        u.should.have.property("admin").that.equals(admin);
    }

    describe('User', function(){
      describe('#next()', function(){
        users = new Users();
        it('should generate users according to parameters', function(){
            generateAndCheck(users, false, "George")
            generateAndCheck(users, true, "Hanna")
        })
      })
    });
    
    
    
    describe('Fake-Communicator', function(){
      describe('#signIn()', function(){
        users = new Users();
        it('should sign you in', function(){
            var comm = new FakeCommunicator(new Generator(), new Users())
            var userPromise = comm.signIn({email:"Phil@haha.jk",password:"phil"})
            return userPromise
        })
      })
    });
    
    describe('Fake-Communicator', function(){
      describe('#signIn()', function(){
        users = new Users();
        it('should sign you in', function(){
            var comm = new FakeCommunicator(new Generator(), new Users())
            var userPromise = comm.signIn({email:"Phil@haha.jk",password:"phil"})
            return userPromise
        })
      });
      
      describe('#signout()', function(){
        users = new Users();
        it('should sign you in', function(){
            var comm = new FakeCommunicator(new Generator(), new Users())
            var userPromise = comm.signIn({email:"Phil@haha.jk",password:"phil"})
            return userPromise.then(function(){comm.signOut()})
        })
      });
    });
    
    
}());
