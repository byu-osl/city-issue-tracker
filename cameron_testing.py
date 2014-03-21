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
        s = models.Service(
            serviceId=1,
            serviceName='Take out trash',
            description='Take out trash',
            metaData=True,
            type='realtime',
            attributes=[sa, sa1],
            keywords=[k, k1])
        db.session.add(s)
        db.session.commit()
        assert s in db.session
        
        s1 = models.Service.query.filter_by(serviceName='Take out trash').first()
        assert s1.serviceId == 1
        assert s1.serviceName == 'Take out trash'
        assert s1.description == 'Take out trash'
        
        db.session.delete(s1)
        db.session.commit()
        assert s1 not in db.session

    def test_Two_Services(self):
        print '\ntest_Two_Services'
        sa = models.ServiceAttribute()
        db.session.add(sa)
        sa1 = models.ServiceAttribute()
        db.session.add(sa1)
        k = models.Keyword()
        db.session.add(k)
        k1 = models.Keyword()
        db.session.add(k1)
        s1 = models.Service(
            serviceId=1,
            serviceName='Repair sidewalk',
            description='Chipped sidewalk needs repair',
            metaData=True,
            type='realtime',
            attributes=[sa1],
            keywords=[k,k1])
        s2 = models.Service(
            serviceId=2,
            serviceName='Take out trash',
            description='Overflowing garbage bin',
            metaData=True,
            type='batch',
            attributes=[sa,sa1],
            keywords=[k])
        db.session.commit()
        assert s1 in db.session
        assert s2 in db.session

        s3 = models.Service.query.filter_by(type='batch').first()
        assert s3.serviceId == 2

        db.session.delete(s1)
        db.session.commit()
        assert s1 not in db.session
        db.session.delete(s2)
        db.session.commit()
        assert s2 not in db.session

class SubTestUser(MyTest):
    
    def test_User(self):
        print '\ntest_User'
        sr = models.ServiceRequest()
        db.session.add(sr)
        user = models.User(
            userId=1,
            firstName='Cameron',
            lastName='Jones',
            phone='7192007970',
            passwordHash='60744474c3277428a8be861186e1e368',
            passwordSalt='s0mRIdlKvI',
            role='user',
            lastLogin=date.today(),
            joined=date.today(),
            subscriptionList=[sr])
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

    def test_Two_Users(self):
        print '\ntest_Two_Users'
        user = models.User(
            userId=1,
            firstName='Cameron',
            lastName='Jones',
            phone='7192007970',
            passwordHash='60744474c3277428a8be861186e1e368',
            passwordSalt='s0mRIdlKvI',
            role='user',
            lastLogin=date.today(),
            joined=date.today())
        user1 = models.User(
            userId=1,
            firstName='Susan',
            lastName='Jones',
            phone='7194602421',
            role='employee')
        db.session.add(user)
        db.session.add(user1)
        from sqlalchemy.exc import IntegrityError
        self.assertRaises(IntegrityError, lambda: db.session.commit())
        assert user1 not in db.session

class SubTestAgency(MyTest):
    
    def test_Agency(self):
        print '\ntest_Agency'
        agency = models.Agency(
            name='Name1'
            )
        db.session.add(agency)
        sr = models.ServiceRequest()
        sr1 = models.ServiceRequest()
        db.session.add(sr)
        db.session.add(sr1)
        db.session.commit()
        assert agency in db.session
        assert sr.serviceRequestId is not None
        assert sr1.serviceRequestId is not None
        
class SubTestKeyword(MyTest):

    def test_Keyword(self):
        print '\ntest_Keyword'
        keyword = models.Keyword(
            keyword='Trash')
        keyword1 = models.Keyword(
            keyword='Repair')
        db.session.add(keyword)
        db.session.add(keyword1)
        db.session.commit()
        assert keyword in db.session
        assert keyword1 in db.session
if __name__ == '__main__':
    unittest.main()