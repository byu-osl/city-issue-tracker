// include this line wherever you need a communicator

// change this line to change the communicator
var comm = new FakeCommunicator(new Generator(), new Users());
comm = addCaching(comm);

// comm now has the following attributes:
// user - the user - it's {} if no-one is logged in.

// Login management

var showLogin;

var onLogin = [];
var onLogout = [];

function initLoginBindings(){
	$("#login-close-button").click(function(){
		$("#login-popup").hide();
	});
	
	showLogin = function showLogin(){
		$("#login-popup").show();
	}
	
	$("#login").click(function(){
		comm.signIn({
			email:$("#login-email")[0].value,
			password:$("#login-password")[0].value
		}).then(
			function success(user){
				$("#login-popup").hide();
				$("#login-close-button").off('click');
				onLogin.map(function(func){func()})
			},
			function failure(){
				console.log("Failure");
			}
		)
	});
};

initLoginBindings();

showLogin();
