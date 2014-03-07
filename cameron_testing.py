from flask.ext.testing import TestCase
from app import app, db

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
class SubTestServices(MyTest):
    
    def test_something(self):
        pass
    
    pass