import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods

class AdshopcartAppPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest that is function inside class (vs @classmethod)
    def test_create_new_user(): # test_in the name is mandatory
        methods.setUp()
        methods.check_homepage()
        methods.SignUp()
        methods.check_full_name()
        methods.check_orders()
        methods.log_out()
        methods.log_in(locators.new_username,locators.new_password)
        methods.delete_test_account()
        methods.log_in(locators.new_username,locators.new_password)
        methods.credential_check()
        methods.tearDown()




