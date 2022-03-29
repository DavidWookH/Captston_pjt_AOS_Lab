import datetime
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


# # -----------------------------------------------------------------------