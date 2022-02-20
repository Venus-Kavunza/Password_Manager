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
