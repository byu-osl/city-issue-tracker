Communicatior = function communicator_namespace() {
  

  function Communicator() {}

  
  //Log into an account
  Communicator.prototype.login = function(callback, form) {
    $.ajax({
      url: "/users/sign_in",
      type: "POST",
      data: form.serialize(),
      success: callback
    });
  };
  
  //Create a new account
  Communicator.prototype.createAccount = function(callback, form) {
    $.ajax({
      url: "/users/new",
      type: "POST",
      data: form.serialize(),
      success: callback
    });
  };
  
  //Update account details. Account user and administrators only.
  Communicator.prototype.updateAccount = function(callback, id, form) {
    $.ajax({
      url: "/users/"+id,
      type: "POST",
      data: form.serialize(),
      success: callback
    });
  };
  
  //View account details. Account user and administrators only.
  Communicator.prototype.getAccount = function(callback, id) {
    $.ajax({
      url: "/users/"+id,
      type: "GET",
      
      success: callback
    });
  };
  
  //Sign into an account. Should set a session cookie.
  Communicator.prototype.signIn = function(callback, form) {
    $.ajax({
      url: "/users/sign_in",
      type: "POST",
      data: form.serialize(),
      success: callback
    });
  };
  
  //Sign out of an account. Removes the session cookie.
  Communicator.prototype.signOut = function(callback) {
    $.ajax({
      url: "/users/sign_out",
      type: "POST",
      data: {},
      success: callback
    });
  };
  
  //Create a new issue. Shouldn't be visible until approved.
  Communicator.prototype.createIssue = function(callback, form) {
    $.ajax({
      url: "/issues",
      type: "POST",
      data: form.serialize(),
      success: callback
    });
  };
  
  //Updates an issue (admin only)
  Communicator.prototype.updateIssue = function(callback, id, form) {
    $.ajax({
      url: "/issues/"+id,
      type: "POST",
      data: form.serialize(),
      success: callback
    });
  };
  
  //retreives a list of issues
  Communicator.prototype.getIssues = function(callback, orderBy, offset, max, query, reversed) {
    $.ajax({
      url: "/issues?orderBy="+encodeURIComponent(orderBy)+"&offset="+encodeURIComponent(offset)+"&max="+encodeURIComponent(max)+"&query="+encodeURIComponent(query)+"&reversed="+encodeURIComponent(reversed),
      type: "GET",
      
      success: callback
    });
  };
  
  //retreives an issue
  Communicator.prototype.getIssue = function(callback, id) {
    $.ajax({
      url: "/issues/"+id,
      type: "GET",
      
      success: callback
    });
  };

  return Communicator;
}