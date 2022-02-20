import pyperclip
from user import User

def create_user(fname, lname, password):
    '''
    This function creates a new user account
    '''
    new_user = User(fname,lname,password)
    return new_user