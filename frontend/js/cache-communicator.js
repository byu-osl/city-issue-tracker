CacheCommunicator = (function communicator_namespace() {
  
    // Account create/view/edit
    
    function CacheCommunicator(source){
        this.source = source
    }
    
    function useSourceFor(funcName):
        CacheCommunicator.prototype[funcName] = function passBack(){
            return this[funcName].call(this,arguments)
        }
    }
    
    [  
        "signIn",
        "signOut",
        "submitPhoto",
        "createIssue",
        "getIssue",
        "getIssues",
        "addNote",
        "updateIssue",
        "createAccount",
        "getAccounts",
        "updateAccount"
    ].map(useSourceFor)

  return CacheCommunicator;
}());
