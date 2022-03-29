import datetime
from time import sleep
from selenium import webdriver  # import Selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select # <-- add this import for drop down list
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options

s = Service(executable_path='../chromedriver.exe') # no deprecation
driver = webdriver.Chrome(service=s)

# user_system_id=''
# # create a Chrome driver Instance, specify path to chromedriver file
# # this gives a DeprecationWarning

# Advantage Shopping Cart Test Automation Plan
# launch Advantage Shopping Cart App Website  - validate we are on the home page

def setUp():
    print("*-------------------------------------------------------*")
    print(" Advantage Shopping Cart App --- by Wook Huang           ")
    print("*-------------------------------------------------------*")
    print("")
    print(f' ### Launch {locators.app} App ### ')
    print(f'*---------------------------------------------------------------------------------')
    print(f' Test Start time : {datetime.datetime.now()}')
    print(f'*---------------------------------------------------------------------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give the browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get(locators.adshopcart_url)
    ## Check that Advantage Shopping URL and the home page titles are displayed
    print(f'*---[Create New Account]---------------------------------------------------------')
    if driver.current_url == locators.adshopcart_url and locators.adshopcart_home_page_title in driver.title:
        print(f'*---Checking Title and URL---------------------------------------------------')
        print(f' {locators.app} websites launched successfully!')
        print(f' Current URL   : {driver.current_url}')
        print(f' Homepage title: {driver.title}')
        print(f'*----------------------------------------------------------------------------')
        sleep(2) # holding website for 3seconds otherwise close very quickly
    else:
        print(f'*-----------------------------------------------------------------------------')
        print(f'{locators.app} did not launch. Check your code or the application')
        print(f' Current URL   : {driver.current_url}')
        print(f' Homepage title: {driver.title}')
        print(f'*-----------------------------------------------------------------------------')
        tearDown()

def SignUp():
# For SignUp, click Account icon and populate necessary information
    print(f'*---[Sign Up New Account]---------------------------------------------------------*')
    if driver.current_url == locators.adshopcart_url:  # check we are on the home page
        sleep(2)
        driver.find_element(By.ID, 'menuUserLink').click()
        if driver.current_url == locators.adshopcart_url and locators.adshopcart_home_page_title in driver.title:
            # check we are on the login page -- how to check pop up?
            print(f'---- {locators.app} App Login page is displayed! Continue to log in.')
            print(f'*---[ACCOUNT DETAILS]---------------------------------------------------------*')
            sleep(2)
            driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
            sleep(0.5)
            driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
            sleep(0.5)
            driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
            sleep(0.5)
            driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
            sleep(0.5)
            driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
            sleep(0.5)
            print(f' User name : {locators.new_username}')
            print(f' email     : {locators.email}')
            print(f' password  : {locators.new_password}')
            print(f'*---[PERSONAL DETAILS Info]-------------------------------------------------------*')
            driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
            sleep(0.5)
            driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
            sleep(0.5)
            driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phonenum)
            sleep(0.5)
            print(f' First Name    : {locators.first_name}')
            print(f' Last Name     : {locators.last_name}')
            print(f' Phone Number  : {locators.phonenum}')
            print("")
            print(f'*---[ADDRESS DETAILS Info]--------------------------------------------------------*')
            Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
            sleep(0.5) # Country
            driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
            sleep(0.5) # City
            driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address_only)
            sleep(0.5) # State
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.State)
            sleep(0.5) # zip code
            driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.ZipCode)
            sleep(0.5) # State
            print(f' City      : {locators.city}')
            print(f' Address   : {locators.address_only}')
            print(f' State/Province/Region   : {locators.address}')
            print(f' Postal Code  : {locators.ZipCode}')
            print(f'*----------------------------------------------------------------------------*')
            driver.find_element(By.NAME, 'i_agree').click()
            sleep(1)
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(2) ###register_button
    else:
         print(f' Something is wrong with program. Check your code or website and try again.')

# Precondition: SignUp() process is completed and user is logged in
def check_full_name():
     print(f'*---[Check Full name from My account ]-----------------------------------------------*')
     print(driver.current_url == locators.adshopcart_url)
     if driver.current_url == locators.adshopcart_url:
#        print(driver.current_url == locators.adshopcart_url and locators.adshopcart_home_page_title in driver.title)
         driver.find_element(By.ID, 'menuUserLink').click()
         sleep(3)  #check account icon
         driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="My_account"]').click()
         sleep(1.5)
         print(f'*---Account page is displayed---------------------------------------------------*')
         #print(locators.full_name)
         assert driver.find_element(By.XPATH,f'//label[contains(., "{locators.full_name}")]').is_displayed()
         checkorder = (driver.find_element(By.XPATH, f'//label[contains(.,"{locators.full_name}")]').is_displayed())
         #print(checkorder)
         print(f'The full name of {locators.full_name}  is verified: {checkorder} ')
         print(f'*---Full name in the account is checked ---------------------------------------------*')
     else:
         print(f' Please check your name again')

def check_orders():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="My_Orders"]').click()
    sleep(3)
    print(f'*-[My Order Statues Check ] -------------------------------------------------------*')
    # valid 1 is True when there is "No Order" in the account
    valid1 = driver.find_element(By.XPATH, f'//label[contains(., "No order")]').is_displayed()
    #print(valid1)
    if valid1:
        print ("There is No orders in My Order")
    else:
        print ("Invalid Order exits, Please move to next process")
    print(f'*---[NO Order Checking is completed: {datetime.datetime.now()}]---------------*')
    print(f' ')

def log_in(username, password):
    if driver.current_url == locators.adshopcart_url:
       driver.find_element(By.ID, 'menuUserLink').click()
       print(f'*--[LOG IN PAGES]--------------------------------------------------------------*')
       print(f'## Login page is displayed! please Continue.')
       sleep(1)
       driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
       sleep(0.5)
       driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
       sleep(0.5)
       driver.find_element(By.ID, 'sign_in_btnundefined').click() #method 1 using ID
       # driver.find_element(By.XPATH,'//button[contains(text(),"SIGN IN")]').click() # method 3 using XPATH
       sleep(0.5)
       if driver.current_url == locators.adshopcart_url and  locators.adshopcart_home_page_title in driver.title:
          print(f'{locators.app}  Login is successful. {datetime.datetime.now()} ')
          print("")
       else:
          print(f'Dashboard is not displayed. Check your code or website and try again.')

def log_out():
    print(f'*---[Sign Out]----------------------------------------------------------------*')
    sleep(1)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="Sign_out"]').click()
    sleep(2)
    if driver.current_url == locators.adshopcart_url:
       print(f'# Sign Out successful! {datetime.datetime.now()}')
       print(f'*----------------------------------------------------------------------------*')

def delete_test_account():
    print(f'*--[DELETE TEST ACCOUNT]--------------------------------------------------------------*')
    # Navigate to Site Administration > Users Browse list of users
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="My_account"]').click()
    sleep(5)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    #driver.find_element(By.CSS_SELECTOR, 'div.deleteBtnText').click()
    sleep(5)
    # driver.find_element(By.XPATH, '//*[@id="deletePopupBtn deleteRed"]').click()
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    #driver.find_element(By.LINK_TEXT, 'YES').click()
    sleep(3)
    print(f'*--DELETION COMPLETED : {datetime.datetime.now()} ----------------------------------*')
    # -----------------------------------------------------------------------------
def tearDown():
    if driver is not None:
        print(f'*--------------------------------------------------------------------------------------------*')
        print(f'The test is completed at : {datetime.datetime.now()}')
        print(f'*--------------------------------------------------------------------------------------------*')
        sleep(3)
        driver.close()
        driver.quit()

# setUp()
# SignUp()
# check_full_name()
# check_orders()
# log_out()
# log_in(locators.new_username,locators.new_password)
# delete_test_account()
# #log_in(locators.delname,locators.delpwd)
# tearDown()

