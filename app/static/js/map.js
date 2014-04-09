var map;
var geocoder;
//Bounds used when geocoding to bias towards returning locations in Cedar City
//This means it should return locations in Cedar City, even if Cedar City is not explicitly specified
var bounds;
var markers = {};
var infoWindow = new google.maps.InfoWindow({});

var createIssue = startAddIssue;

function explore(event){
	
}

function initialize() {
	geocoder = new google.maps.Geocoder();
	var sw = new google.maps.LatLng(40.392528, -111.773320);
	var ne = new google.maps.LatLng(40.431935, -111.737357);
	bounds = new google.maps.LatLngBounds(sw, ne);
	
	var mapOptions = {
		zoom: 14,
		center: new google.maps.LatLng(40.413966, -111.758901),
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	//If markers were created before the map was, add them now
	for (var id in markers) {
		markers[id].setMap(map);
	}
	
	google.maps.event.addListener(map, 'click', function(event) {
		infoWindow.close();
		infoWindow = new google.maps.InfoWindow({
			content: "<div>" +
					"<p>Would you like to create a new issue here?</p>" +
					"<button id='btn-yes' style='width: 40px; margin: 5px 15px;'>Yes</button>" +
					"<button id='btn-no'  style='width: 40px; margin: 5px 15px;'>No</button>" +
					"</div>",
			position: event.latLng
		});
		
		infoWindow.open(map);
		
		$('#btn-yes').on('click',function(){createIssue(event.latLng.lat(), event.latLng.lng());infoWindow.close();})
		$('#btn-no').on('click',function(){infoWindow.close()});	
		console.log("Latitude:", event.latLng.lat());
		console.log("Longitude:", event.latLng.lng());
	});
}
google.maps.event.addDomListener(window, 'load', initialize);

//Sets the height of the map's container.
//The height will be updated when the browser height changes.
function setMapHeight() {
	var height = window.innerHeight - $('.navbar').height() - 15;
	$('#right-container').height(height);
}
$(window).resize(setMapHeight);
setMapHeight();

/**
 * Geocodes the given address to latitude and longitude.
 * @param address string of the location to geocode
 * @param callback function to call with the LatLng passed as a parameter
 */
function geocodeAddress(address, callback) {
	geocoder.geocode( { 'address': address, 'bounds': bounds}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			var location = results[0].geometry.location;
			if (typeof callback == 'function') {
				callback(location);
			}
		} else {
			callback("Geocode was not successful for the following reason: " + status);
		}
	});
}

/**
 * Reverse geocodes the given latitude and longitude to a human readable address.
 * @param location google.maps.LatLng to get the address for
 * @param callback function to call with the address returned from the reverse geocoding
 */
function reverseGeocode(location, callback) {
	geocoder.geocode({'location': location}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			callback(results[0].formatted_address);
		} else {
			callback("Reserve geocode was not successful for the following reason: " + status);
		}
	});
}

function addIssueToMap(issue) {
	if (issue.location.address) {
		//Has address but missing latitude or longitude. Use geocoding
		if (!issue.location.lat || !issue.location.long) {
			geocodeAddress(issue.location.address, function(latLng) {
				issue.location.lat = latLng.lat();
				issue.location.long = latLng.lng();
				createMarker(issue);
			});
		} else {//Has all location information
			createMarker(issue);
		}
	//Missing address but has latitude and longitude.  Use reverse geocoding
	} else if (issue.location.lat && issue.location.long) {
		reverseGeocode(new google.maps.LatLng(issue.location.lat, issue.location.long), function(address) {
			issue.location.address = address;
			createMarker(issue);
		});
	} else {//Missing a valid address.  Cannot add to map
		return {error: true, message: "missing valid address and latitude/longitude"};
	}
	return {error: false, message: "issue added to map successfully"};
}

function createMarker(issue) {
	var latLng = new google.maps.LatLng(issue.location.lat, issue.location.long);
	var infowindow = new google.maps.InfoWindow({
		content: "<div><h1>" + issue.title + "</h1><p>" + issue.description + 
				"</p><a onclick='openIssue(" + issue.id + ")'>Go to issue</a></div>"
	});

	var marker = new google.maps.Marker({
		position: latLng,
		map: map,
		title: issue.title
	});
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map, marker);
	});
	
	
	//Keep track of the markers so that they can be removed from the map if necessary
	markers[issue.id] = marker;
}

