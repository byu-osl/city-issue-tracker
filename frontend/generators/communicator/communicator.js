Communicatior = function communicator_namespace() {
  

  function Communicator() {}

  
  //Sign into an account. Should set a session cookie.
  Communicator.prototype.signIn = function(callback, data) {
    $.ajax({
      url: "/users/sign_in",
      type: "POST",
      data: data,
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
  
  //Create a new account
  Communicator.prototype.createAccount = function(callback, data) {
    $.ajax({
      url: "/users",
      type: "POST",
      data: data,
      success: callback
    });
  };
  
  //Update account details. Account user and administrators only.
  Communicator.prototype.updateAccount = function(callback, id, data) {
    $.ajax({
      url: "/users/"+id,
      type: "POST",
      data: data,
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
  
  //Get a list of all accounts.
  Communicator.prototype.getAccounts = function(callback) {
    $.ajax({
      url: "/users",
      type: "GET",
      
      success: callback
    });
  };
  
  //View a particular issue.
  Communicator.prototype.getIssue = function(callback, id) {
    $.ajax({
      url: "/issues/"+id,
      type: "GET",
      
      success: callback
    });
  };
  
  //Create a new issue. Shouldn't be visible until approved.
  Communicator.prototype.createIssue = function(callback, data) {
    $.ajax({
      url: "/issues",
      type: "POST",
      data: data,
      success: callback
    });
  };
  
  //Updates an issue (admin only)
  Communicator.prototype.updateIssue = function(callback, id, data) {
    $.ajax({
      url: "/issues/"+id,
      type: "POST",
      data: data,
      success: callback
    });
  };
  
  //retreives a list of issues
  Communicator.prototype.getIssues = function(callback, orderBy, offset, max, query, reversed, includeClosed) {
    $.ajax({
      url: "/issues?orderBy="+encodeURIComponent(orderBy)+"&offset="+encodeURIComponent(offset)+"&max="+encodeURIComponent(max)+"&query="+encodeURIComponent(query)+"&reversed="+encodeURIComponent(reversed)+"&includeClosed="+encodeURIComponent(includeClosed),
      type: "GET",
      
      success: callback
    });
  };
  
  //Submits a form with an image and returns the image URL
  Communicator.prototype.uploadImage = function(callback, form) {
    $.ajax({
      url: "/issues/upload_image",
      type: "POST",
      data: {},
      success: callback
    });
  };

  return Communicator;
}