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
    # Give the browser up to 15 seconds to respond
    driver.implicitly_wait(15)
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
        sleep(1) # holding website for 3seconds otherwise close very quickly
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
        sleep(1)
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
         sleep(2)  #check account icon
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
    sleep(1.5)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="My_Orders"]').click()
    sleep(2)
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
    if (username==locators.new_username and password == locators.new_password):
        driver.find_element(By.ID, 'menuUserLink').click()
        print(f'*--[LOG IN PAGES]--------------------------------------------------------------*')
        print(f'## Login page is displayed! please Continue.')
        sleep(1)
        driver.find_element(By.NAME, 'username').send_keys(username)
        sleep(0.5)
        driver.find_element(By.NAME, 'password').send_keys(password)
        sleep(0.5)
        driver.find_element(By.ID, 'sign_in_btnundefined').click() #method 1 using ID
        # driver.find_element(By.XPATH,'//button[contains(text(),"SIGN IN")]').click() # method 3 using XPATH
        sleep(0.5)
        print(f'{locators.app}  Login is successful. {datetime.datetime.now()} ')
        print("")
    else:
        print(f' There is something wrong with login. please check again ')

def log_out():
    print(f'*---[Sign Out]----------------------------------------------------------------*')
    sleep(1)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1.5)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="Sign_out"]').click()
    sleep(2)
    if driver.current_url == locators.adshopcart_url:
       print(f'# Sign Out successful! {datetime.datetime.now()}')
       print(f'*----------------------------------------------------------------------------*')

def delete_test_account():
    print(f'*--[DELETE TEST ACCOUNT]--------------------------------------------------------------*')
    # Navigate to Site Administration > Users Browse list of users
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1.5)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="My_account"]').click()
    sleep(2.5)
    #driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[1]/div[6]/button/div').click()
    #driver.find_element(By.CSS_SELECTOR, 'div.deleteBtnText').click()
    sleep(3)
    # driver.find_element(By.XPATH, '//*[@id="deletePopupBtn deleteRed"]').click()
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    #driver.find_element(By.LINK_TEXT, 'YES').click()
    sleep(3)
    print(f'*--DELETION COMPLETED : {datetime.datetime.now()} ----------------------------------*')
    # -----------------------------------------------------------------------------

def credential_check():
    assert driver.find_element(By.XPATH, f'//label[contains(., "{locators.loginerror}")]').is_displayed()
    checkerror = (driver.find_element(By.XPATH, f'//label[contains(.,"{locators.loginerror}")]').is_displayed())
    if (checkerror):
       print(f' Error lable - Incorrect user name or password - is verified ')
    else:
        print(f'Credential test is passed ')

def check_homepage():
    if driver.current_url == locators.adshopcart_url and locators.adshopcart_home_page_title in driver.title:
       hp_cam_check = driver.find_element(By.ID, 'speakersTxt').get_attribute("textContent")
       hp_tab_check = driver.find_element(By.ID, 'tabletsTxt').get_attribute("textContent")
       hp_lap_check = driver.find_element(By.ID, 'laptopsTxt').get_attribute("textContent")
       hp_mic_check = driver.find_element(By.ID, 'miceTxt').get_attribute("textContent")
       hp_head_check = driver.find_element(By.ID, 'headphonesTxt').get_attribute("textContent")
       print(f'Items(Text) are found Home page: ')
       print( hp_cam_check, hp_tab_check, hp_lap_check, hp_mic_check, hp_head_check)
    else:
       print(f'Specific item is not found!  test failed ')

    print('#---[Clickable Navigation Check ]-----------------------------------------------#')
    our_product_xpath = '/html/body/header/nav/ul/li[8]/a'
    special_offer_xpath = '/html/body/header/nav/ul/li[7]/a'
    popular_item_xpath = '/html/body/header/nav/ul/li[6]/a'
    contact_us_xpath = '/html/body/header/nav/ul/li[5]/a'

    driver.find_element(By.XPATH, special_offer_xpath).click()
    print('#- Special offer nav menu is clickable------------')
    sleep(1.5)

    driver.find_element(By.XPATH, popular_item_xpath).click()
    print('#- Popular Item nav menu is clickable------------')
    sleep(1.5)

    driver.find_element(By.XPATH, contact_us_xpath).click()
    print('#- Contact Us nav menu is clickable------------')
    sleep(1.5)

    driver.find_element(By.XPATH, our_product_xpath).click()
    print('#- navigate back to Our Product(clickable)------------')
    sleep(1.5)
    # LOGO CHECK
    print("")
    print('#---[Advantage Logo Check] ----------------------------------#')
    logo1 = driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[1]').get_attribute("textContent")
    logo2 = driver.find_element(By.CLASS_NAME, 'logoDemo.roboto-light.ng-binding').get_attribute("textContent")
    sleep(1)
    print(f'Logo checked : {logo1} and {logo2} is displayed')

    print('#---[Contact us information ] ----------------------------------#')
    driver.find_element(By.XPATH, contact_us_xpath).click()
    sleep(2)
    # product = driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER')
    print("! condtion: for updown poduct list - only one product is assigned for category to simplify")
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text(locators.contact1)
    sleep(1)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text(locators.contact2)
    sleep(1)
    sleep(1)
    # email_xpath='/html/body/div[3]/section/article[5]/div[1]/div/div[2]/sec-form/div[1]/div/sec-view[3]/div/input'
    driver.find_element(By.NAME,'emailContactUs').send_keys(locators.email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').clear()
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1.5)
    contshop=driver.find_element(By.XPATH,'/html/body/div[3]/section/article[5]/div[2]/div/a').get_attribute("textContent")
    print(f'#--  {contshop} is displayed ----------------------------------- ')
    sleep(1.5)
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
    sleep(2)

def tearDown():
    if driver is not None:
        print(f'*--------------------------------------------------------------------------------------------*')
        print(f'The test is completed at : {datetime.datetime.now()}')
        print(f'*--------------------------------------------------------------------------------------------*')
        sleep(2)
        driver.close()
        driver.quit()

# setUp()
# check_homepage()
# SignUp()
# check_full_name()
# check_orders()
# log_out()
# log_in(locators.new_username,locators.new_password)
# delete_test_account()
# log_in(locators.new_username,locators.new_password)
# credential_check()
# tearDown()

