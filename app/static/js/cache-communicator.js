addCaching = (function communicator_namespace() {
  
    // Account create/view/edit
    
    function CacheCommunicator(source){
        this.source = source
        this.user = {}
    }
    
    function useSourceFor(funcName){
        CacheCommunicator.prototype[funcName] = function passBack(){
            return this.source[funcName].apply(this.source,arguments)
        }
    }
    
    
    [  
        "submitPhoto",
        "createIssue",
        "getIssue",
        "getIssues",
        "addNote",
        "updateIssue",
        "createAccount",
        "getAccounts",
        "updateAccount"
    ].map(useSourceFor, this)
    
    CacheCommunicator.prototype.signIn = function login(){
        return this.source.signIn.apply(this.source,arguments).then(function saveUser(user){
            this.user = user;
            return user;
        }.bind(this));
    }
    
    CacheCommunicator.prototype.getIssues = function getIssues(){
        return this.source.getIssues.apply(this.source,arguments).then(function saveIssues(issues){
            this.issues = issues;
            return issues;
        }.bind(this));
    }
    
    CacheCommunicator.prototype.signOut = function logout(){
        return this.source.signOut.apply(this.source,arguments).then(function loggingOut(){
            this.user = {};
        }.bind(this));
    }
    
    function addCaching(communicator){
        return new CacheCommunicator(communicator)
    }

    return addCaching;
}());
