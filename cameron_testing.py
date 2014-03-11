from flask.ext.testing import TestCase
from app import app, db, models
import unittest
import time
from datetime import date

class MyTest(unittest.TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        return app
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
class SubTest_Services(MyTest):
    
    def test_something(self):
        print '\ntest_something Service'
        s = models.Service()
        db.session.add(s)
        db.session.commit()
        assert s in db.session

    def test_Service(self):
        print '\ntest_Service'
        sa = models.ServiceAttribute()
        db.session.add(sa)
        sa1 = models.ServiceAttribute()
        db.session.add(sa1)
        k = models.Keyword()
        db.session.add(k)
        k1 = models.Keyword()
        db.session.add(k1)
        s = models.Service(id=1, service_name='Take out trash', description='Take out trash', meta_data=True, type='realtime', attributes=[sa, sa1], keywords=[k, k1])
        db.session.add(s)
        db.session.commit()
        assert s in db.session
        
        s1 = models.Service.query.filter_by(service_name='Take out trash').first()
        assert s1.id == 1
        assert s1.service_name == 'Take out trash'
        assert s1.description == 'Take out trash'
        
        db.session.delete(s1)
        db.session.commit()
        assert s1 not in db.session
    
    def test_User(self):
        print '\ntest_User'
        sr = models.ServiceRequest()
        db.session.add(sr)
        user = models.User(
            userId=1,
            email='cejonesmsncom',
            firstName='Cameron',
            lastName='Jones',
            phone='7192007970',
            passwordHash='60744474c3277428a8be861186e1e368',
            passwordSalt='s0mRIdlKvI',
            role='user',
            lastLogin=date.today(),
            joined=date.today(),
            subscriptions=[sr])
        sr.accountId = user.userId
        db.session.add(user)
        db.session.commit()
        assert user in db.session
        
        u1 = models.User.query.filter_by(firstName='Cameron').first()
        assert u1.firstName == 'Cameron'
        assert u1.lastName == 'Jones'
        
        non_user = models.User()
        db.session.add(non_user)
        db.session.commit()
        db.session.delete(non_user)
        db.session.commit()
        assert user in db.session
        db.session.delete(user)
        db.session.commit()
        assert user not in db.session

def SubTestUser(MyTest):
    pass

if __name__ == '__main__':
    unittest.main()