var map;
var geocoder;
//Bounds used when geocoding to bias towards returning locations in Cedar City
//This means it should return locations in Cedar City, even if Cedar City is not explicitly specified
var bounds;
function initialize() {
	geocoder = new google.maps.Geocoder();
	var sw = new google.maps.LatLng(37.616517535818396, -113.1707775592804);
	var ne = new google.maps.LatLng(37.7494418243111, -113.00580024719238);
	bounds = new google.maps.LatLngBounds(sw, ne);
	
	var mapOptions = {
		zoom: 14,
		center: new google.maps.LatLng(37.67747689999999, -113.06189310000002),
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	google.maps.event.addListener(map, 'click', function(event) {
		var marker = new google.maps.Marker({
			map: map,
			position: event.latLng
		});
		console.log(event.latLng.lat());
		console.log(event.latLng.lng());
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
			var marker = new google.maps.Marker({
				map: map,
				position: location
			});
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
 * @param callback function to call with the address passed as a parameter
 */
function reverseGeocode(location, callback) {
	geocoder.geocode({'location': location}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			marker = new google.maps.Marker({
				position: latlng,
				map: map
			});
			callback(results[0].formatted_address);
		} else {
			callback("Reserve geocode was not successful for the following reason: " + status);
		}
	});
}
