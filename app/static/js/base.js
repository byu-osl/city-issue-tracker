// include this line wherever you need a communicator

// change this line to change the communicator
var comm = new FakeCommunicator(new Generator(), new Users());
comm = addCaching(comm);

// comm now has the following attributes:
// user - the user - it's {} if no-one is logged in.

// Login management
var onLogin = [];
var onLogout = [];

function bindLogin(){
	$("#login-close-button").click(function(){
		$("#login-popup").hide();
	});
	
	$("#login").click(function(){
		comm.signIn({
			email:$("#login-email")[0].value,
			password:$("#login-password")[0].value
		}).then(
			function success(user){
				onLogin.map(function(func){func()})
				bindLogout()
			},
			function failure(){
				console.log("Failure");
			}
		)
	});
	
	function showLogin(){
		$("#login-password")[0].value = "";
		$("#login-email")[0].value = "";
		$("#login-popup").show();
	}
	
	$("#logout-link").off("click");
	$("#logout-link").hide();
	
	$("#login-link").show();
	$("#login-link").on('click',showLogin)
	
};

function bindLogout(){
	
	function doLogout(){
		comm.signOut().then(
			function success(){
				onLogout.map(function(func){func()})
				bindLogin()
			},
			function failure(){
				alert("Couldn't log out!")
			}
		)
	}
	

	$("#login-popup").hide();
	$("#login-close-button").off('click');	
	$("#login-link").off("click");
	$("#login-link").hide();
	
	$("#logout-link").show();
	$("#logout-link").on('click', doLogout);
}

bindLogin();
