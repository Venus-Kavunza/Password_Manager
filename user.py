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
