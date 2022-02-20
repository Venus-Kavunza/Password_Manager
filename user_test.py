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
        
		
class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Venus','Mwende','dwsp003')
		self.new_user.save_user()
		user2 = User('Muya','Trojan','dwsp003')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

    def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Venus','Twitter','Vee','dwsp003')
		twitter.save_credentials()
		gmail = Credential('Venus','Gmail','Vee','dwsp001')
		gmail.save_credentials()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),3)

    
if __name__ == '__main__':
	unittest.main(verbosity=2)