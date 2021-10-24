import unittest # Importing the unittest module
from user import user # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user =user("Claudia","1234") # create user object

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Claudia")
        self.assertEqual(self.new_user.password,"1234")
  