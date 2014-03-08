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
    
    
}());
