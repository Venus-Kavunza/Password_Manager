import unittest

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
