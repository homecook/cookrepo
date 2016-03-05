import os
import ipdb
import django

ipdb. set_trace()
os.environ['DJANGO_SETTINGS_MODULE'] = 'cookdj.cookdj.settings'
django.setup()  # need to include this for 'stand-alone' code using django

from cookrepo.cookdj.users.models import Users

# test getting a user from database
user1 = Users.objects.get(user_id=1006)
print(user1)

# test writing a new user to database
new_user = Users(
    # user_id = 8979,   # This is a auto-field and need not be specified!
    user_email = 'test123@gmail.com',
    user_pass = 'klskd',
    user_fname = 'Test',
    user_lname = 'User',
    user_address = '111 Dundas St W',
    user_city = 'Mississauga',
    user_prov = 'Ontario',
    user_country = 'Canada',
    user_phone_mobile = '',
    user_phone_home = '245-842-0099',
    user_payment_verified = False
)
print(new_user)
new_user.save()

print('test_db.py - success.')


