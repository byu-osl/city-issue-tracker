#This file is to test the models fuctionality

#TODO: We might need to redo how we handle the app stuff

#NOTE: This is based off of the Flask Mega-tutorial
#http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing

import os
import unittest

#TODO: How to import the app
#from app import app, db


class BaseTestCase(unittest.TestCase):
	"""
	This is the BaseTest Class for everything.
	IF YOU CREATE A NEW TEST CASE MAKE SURE IT INHERITS FROM THIS CLASS
	"""
	def setUp(self):
		print("SetUp")
		#TODO: Config

		#TODO: Enable the creation of a test db

		#db.create_all()#TODO: What does this do?

	def tearDown(self):
		print("tearDown")
		#TODO: Kill the test db
		#db.session.remove()
		#db.drop_all()



class TestCaseService(BaseTestCase, unittest.TestCase):
	"""
	This testCase deals only with the Service and it's various methods
	"""

	def test_total_services(self):
		"""Tests the function to give the total number of services"""
		result = -1
		assert result == 0

		#TODO: Add two services

		#TODO: Check the number

	def test_invalid_type(self):
		"""Tests for a the attempt to save an invalid type"""
		result = -1
		assert result == 0

	def test_invalid_service_name(self):
		"""
		Tests for an attempt to save an invalid service name
		which is longer than 255 characters or 0 characters
		"""
		result = -1
		assert result == 0

	def test_get_type_list(self):
		"""
		Tests that the valid list type is return
		"""
		expected_result = ['','','']#TODO:
		result = -1
		assert result == 0


class TestCaseServiceAttribute(BaseTestCase, unittest.TestCase):
	"""
	This testcase to to test the ServiceAttribute model
	"""

	#TODO: NOTE: Since this requires a Service for the id the tearDown and setUp need to be extended

	def test_save_when_metadata_false(self):
		"""Tests for when an atribute tries to save when the Service metadata is false"""#TODO: Fix sentence
		result = -1
		assert result == 0


	def test_get_datatype_list(self):
		"""
		Test that the correct list of datatypes is returned
		"""
		result = -1
		assert result == 0


class TestCaseKeyword(BaseTestCase, unittest.TestCase):
	"""
	This testcase is to test the Keyword model
	"""

	def test_add(self):
		"""Test simply adding a new Keyword model"""
		result = -1
		assert result == 0

	def test_double_keyword(self):
		"""Test adding the same keyword twice(should fail)"""
		result = -1
		assert result == 0

	def test_keyword_limit(self):
		"""Test that you can't have 0 or moer than 255 characters"""
		result = -1
		assert result == -0





class TestCaseUser(BaseTestCase, unittest.TestCase):
	"""
	This testCase deals only with the User and it's various methods
	"""

#I don't understand what this if statement does
if __name__ == '__main__':
	unittest.main()
