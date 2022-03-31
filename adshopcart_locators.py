import datetime
import random
from faker import Faker
fake = Faker(locale='en_CA')

# ----------------- Advantage Shopping Cart App DATA PARAMETERS ----------------------
app = 'Advantage Shopping Cart'
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_order_url='https://advantageonlineshopping.com/#/MyOrders'
adshopcart_home_page_title = 'Advantage Shopping'
adshopcart_status = 'No orders'
#
valid_flag = False
while not valid_flag:
    new_username = fake.user_name()
    while len(new_username) > 0 and len(new_username) <=15:
        valid_flag=True
        break
    else:
        new_username=fake.user_name()
# new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
phonenum = fake.phone_number()
country = fake.current_country()
city = fake.city()
loginerror='Incorrect user name or password.'
address = fake.address().replace("\n", " ")
addresstemp = address.split()
if (len(addresstemp[-1]) <= 3):
   ZipCode = f'{addresstemp[-2]} {addresstemp[-1]}'
   State = addresstemp[-3]
elif (len(addresstemp[-1]) >= 6):
    ZipCode = f'{addresstemp[-1]}'
    State = addresstemp[-2]
address1=(address.replace(ZipCode," ")).strip()
address2=(address1.replace(State," ")).strip()
address_only = address2.replace(",", " ")

delname = new_username
delpwd = new_password

#-----LAB 4-1. Homepage check list ----------------
homepg_dsp1 ='SPEAKERS'
homepg_dsp2 ='TABLETS'
homepg_dsp3 ='HEADPHONES'
homepg_dsp4 ='LAPTOPS'
homepg_dsp5 ='MICE'
#-----LAB 4-2. Homepage check list ----------------
lst_prod=['Laptops', 'Headphones', 'Tablets','Speakers','Mice']
contact1=lst_prod[random.randint(0,4)]
if contact1 == 'Laptops':
   contact2 = 'HP ENVY - 17t Touch Laptop'
elif contact1 == 'Headphones':
     contact2 = 'Logitech USB Headset H390'
elif contact1 == 'Tablets':
     contact2 = 'HP Pro Tablet 608 G1'
elif contact1 =='Speakers':
     contact2 = 'Bose SoundLink Wireless Speaker'
elif contact1 == 'Mice':
     contact2 = 'Logitech G502 Proteus Core'
else : breakpoint()

description = f'Python Selenium Automated script for Capstone on {datetime.datetime.now()}'
# SPECIAL OFFER
# POPULAR ITEMS
# CONSTACT US

# # -----------------------------------------------------------------------