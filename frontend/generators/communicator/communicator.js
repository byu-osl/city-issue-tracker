Communicatior = function communicator_namespace() {
  

  function Communicator() {}

  
  //Sign into an account. Should set a session cookie.
  Communicator.prototype.signIn = function(data) {
    return $.ajax({
      url: "/users/sign_in",
      data: data,
      type: "POST"
    });
  };
  
  //Sign out of an account. Removes the session cookie.
  Communicator.prototype.signOut = function() {
    return $.ajax({
      url: "/users/sign_out",
      data: {},
      type: "POST"
    });
  };
  
  //Create a new account
  Communicator.prototype.createAccount = function(data) {
    return $.ajax({
      url: "/users",
      data: data,
      type: "POST"
    });
  };
  
  //Update account details. Account user and administrators only.
  Communicator.prototype.updateAccount = function(id, data) {
    return $.ajax({
      url: "/users/"+id,
      data: data,
      type: "POST"
    });
  };
  
  //View account details. Account user and administrators only.
  Communicator.prototype.getAccount = function(id) {
    return $.ajax({
      url: "/users/"+id,
      
      type: "GET"
    });
  };
  
  //Get a list of all accounts.
  Communicator.prototype.getAccounts = function() {
    return $.ajax({
      url: "/users",
      
      type: "GET"
    });
  };
  
  //View a particular issue.
  Communicator.prototype.getIssue = function(id) {
    return $.ajax({
      url: "/issues/"+id,
      
      type: "GET"
    });
  };
  
  //Create a new issue. Shouldn't be visible until approved.
  Communicator.prototype.createIssue = function(data) {
    return $.ajax({
      url: "/issues",
      data: data,
      type: "POST"
    });
  };
  
  //Updates an issue (admin only)
  Communicator.prototype.updateIssue = function(id, data) {
    return $.ajax({
      url: "/issues/"+id,
      data: data,
      type: "POST"
    });
  };
  
  //retreives a list of issues
  Communicator.prototype.getIssues = function(orderBy, offset, max, query, reversed, includeClosed) {
    return $.ajax({
      url: "/issues?orderBy="+encodeURIComponent(orderBy)+"&offset="+encodeURIComponent(offset)+"&max="+encodeURIComponent(max)+"&query="+encodeURIComponent(query)+"&reversed="+encodeURIComponent(reversed)+"&includeClosed="+encodeURIComponent(includeClosed),
      
      type: "GET"
    });
  };
  
  //Submits a form with an image and returns the image URL
  Communicator.prototype.submitPhoto = function(form) {
    return $.ajax({
      url: "/issues/upload_image",
      data: {},
      type: "POST"
    });
  };

  return Communicator;
}