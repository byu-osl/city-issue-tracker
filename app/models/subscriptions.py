from app import db
#http://docs.sqlalchemy.org/en/rel_0_9/orm/relationships.html
#http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/associationproxy.html

subscriptions = db.Table('subscriptions',
	db.Column('serviceRequestId', db.Integer, db.ForeignKey('serviceRequest.serviceRequestId')),
	db.Column('userId', db.Integer, db.ForeignKey('user.userId'))
)

"""
A Model to define User's Subscriptions to Service Requests

Attributes
subscriptionId (int): The primary key of the Subscription
serviceRequestId (int): The id of the service request this subscription is for
userId (int): The user_id for the user matched to this Subscription
"""