import pyperclip
from user import User, 

def create_user(fname, lname, password):
    '''
    This function creates a new user account
    '''
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
	  This function saves a new user account
	'''
	User.save_user(user)

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


if __name__ == '__main__':
	unittest.main(verbosity=2)
