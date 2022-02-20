import pyperclip
import random
import string

global users_list
class User:
    """
    This class creates user accounts and save their details
    """

    users_list = []
    def __init__(self,first_name,last_name,password):
        '''
        This method defines the properties for each user object will hold.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        This function will save a newly created user instance
        '''
        User.users_list.append(self)

class Credential:
	'''
	This class creates  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []
	@classmethod
	def check_user(cls,first_name,password):
		'''
		This method checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_name,site_name,account_name,password):
		'''
		This method defines the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

    def save_credentials(self):
		'''
		This function saves a newly created user instance
		'''
		# global users_list
		Credential.credentials_list.append(self)
	
	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		This function generates an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass 