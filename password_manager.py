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

def verify_user(first_name,password):
	'''
	This function verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	This function generates a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	This function creates a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential


