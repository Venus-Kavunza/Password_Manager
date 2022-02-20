import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    """
    Class that test cases for the user class behaviours.

    Args:
        unittest.Testcase: is used in creating test cases
    """
    def setUp(self):
        """
        This function is used to create a user account 
        """
        self.new_user = User('Venus','Mwende','dwsp003')

    def test__init__(self):
        """
        Test to if check the initialization/creation of user instances is properly done
        """
        self.assertEqual(self.new_user.first_name,'Venus')
        self.assertEqual(self.new_user.last_name,'Mwende')
        self.assertEqual(self.new_user.password,'dwsp003')

    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
		


if __name__ == '__main__':
	unittest.main(verbosity=2)