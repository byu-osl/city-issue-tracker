// include this line wherever you need a communicator

// change this line to change the communicator
var comm = new FakeCommunicator(new Generator(), new Users());
comm = addCaching(comm);

// comm now has the following attributes:
// user - the user - it's {} if no-one is logged in.
