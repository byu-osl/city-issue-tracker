
#These are taken from http://wiki.open311.org/GeoReport_v2

# It will be important to note that the json will have values such as 'true' and 'null'


#This page is meant to help with the future gola of generating new fake data
service_list = [
	{
		"service_code":001,
		"service_name":"Cans left out 24x7",
		"description":"Garbage or recycling cans that have been left out for more than 24 hours after collection. Violators will be cited.",
		"metadata": True,
		"type":"realtime",
		"keywords":"lorem, ipsum, dolor",
		"group":"sanitation"
	},
	{
		"service_code":002,
		"metadata":True,
		"type":"realtime",
		"keywords":"lorem, ipsum, dolor",
		"group":"street",
		"service_name":"Construction plate shifted",
		"description":"Metal construction plate covering the street or sidewalk has been moved."
	},
	{
		"service_code":003,
		"metadata":True,
		"type":"realtime",
		"keywords":"lorem, ipsum, dolor",
		"group":"street",
		"service_name":"Curb or curb ramp defect",
		"description":"Sidewalk curb or ramp has problems such as cracking, missing pieces, holes, and/or chipped curb."
	}
]

service_def = {
	"service_code":"DMV66",
	"attributes":[
		{
			"variable":True,
			"code":"WHISHETN",
			"datatype":"singlevaluelist",
			"required":True,
			"datatype_description":None,
			"order":1,
			"description":"What is the ticket/tag/DL number?",
			"values":[
				{
					"key":123,
					"name":"Ford"
				},
				{
					"key":124,
					"name":"Chrysler"
				}
			]
		}
	]
}

get_service_reqs = [
	{
		"service_request_id":638344,
		"status":"closed",
		"status_notes":"Duplicate request.",
		"service_name":"Sidewalk and Curb Issues",
		"service_code":006,
		"description":None,
		"agency_responsible":None,
		"service_notice":None,
		"requested_datetime":"2010-04-14T06:37:38-08:00",
		"updated_datetime":"2010-04-14T06:37:38-08:00",
		"expected_datetime":"2010-04-15T06:37:38-08:00",
		"address":"8TH AVE and JUDAH ST",
		"address_id":545483,
		"zipcode":94122,
		"lat":37.762221815,
		"long":-122.4651145,
		"media_url":"http://city.gov.s3.amazonaws.com/requests/media/638344.jpg "
	},
	{
		"service_request_id":638349,
		"status":"open",
		"status_notes":None,
		"service_name":"Sidewalk and Curb Issues",
		"service_code":006,
		"description":None,
		"agency_responsible":None,
		"service_notice":None,
		"requested_datetime":"2010-04-19T06:37:38-08:00",
		"updated_datetime":"2010-04-19T06:37:38-08:00",
		"expected_datetime":"2010-04-19T06:37:38-08:00",
		"address":"8TH AVE and JUDAH ST",
		"address_id":545483,
		"zipcode":94122,
		"lat":37.762221815,
		"long":-122.4651145,
		"media_url":"http://city.gov.s3.amazonaws.com/requests/media/638349.jpg"
	}
]

get_service_req = [
	{
		"service_request_id":638344,
		"status":"closed",
		"status_notes":"Duplicate request.",
		"service_name":"Sidewalk and Curb Issues",
		"service_code":006,
		"description":None,
		"agency_responsible":None,
		"service_notice":None,
		"requested_datetime":"2010-04-14T06:37:38-08:00",
		"updated_datetime":"2010-04-14T06:37:38-08:00",
		"expected_datetime":"2010-04-15T06:37:38-08:00",
		"address":"8TH AVE and JUDAH ST",
		"address_id":545483,
		"zipcode":94122,
		"lat":37.762221815,
		"long":-122.4651145,
		"media_url":"http://city.gov.s3.amazonaws.com/requests/media/638344.jpg"
	}
]

user_data = {
	"first_name": "Jeff",
	"last_name": "Hoffman",
	"email": "jhoffman@fakeemail.com",
	"role": 1,
	"subscriptions": [
		{"issue_id": 1},
		{"issue_id": 2},
		{"issue_id": 3},
		{"issue_id": 4}
	]
}

