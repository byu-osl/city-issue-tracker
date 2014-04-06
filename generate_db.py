#TODO: This file will generate a database and popuplate it will fake data
import json

from app import app, db
from app import models



#Create the table
db.create_all()


json_data = open('default_services.json')
data = json.load(json_data)

for service in data:
	s = models.Service()
	s.serviceName = service['name']
	s.description = service['description']
	s.metaData = service['metadata']
	s.type = service['type']
	db.session.add(s)

	print("=====")
	print("Creating New Service")
	print(service['name'])
	print(service['description'])
	print(service['metadata'])
	print(service['type'])
	print("=====\n")


db.session.commit()


#TODO: Load in JSON file of services


#TODO: For each service type add the information


