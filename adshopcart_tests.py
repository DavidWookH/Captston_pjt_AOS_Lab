import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods

class AdshopcartAppPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest that is function inside class (vs @classmethod)
    def test_create_new_user(): # test_in the name is mandatory
        methods.setUp()
        methods.SignUp()
        methods.check_full_name()  # check_new_user_can_login()
        methods.check_orders()
        methods.log_out()  # logout
        methods.log_in(locators.new_username,locators.new_password)
        methods.delete_test_account()
        methods.tearDown()

        # methods.log_in(locators.admin_name,locators.admin_password)
        # methods.delete_user()
        # methods.log_out()
        # methods.tearDown()

