import firebase_admin
from firebase_admin import db, credentials

cred_cit = credentials.Certificate("/home/anton/Desktop/new_code_cit/safecity-citizen.json")
cred_app = firebase_admin.initialize_app(cred_cit, name='cit_data', options={"databaseURL" : "https://safecity-citizendata-default-rtdb.asia-southeast1.firebasedatabase.app/"})

#db.reference('/').update({'citizen_registration_data': {}})

# insert citizen details into database
def insert_citizen_registered_data(firstname, lastname, email, email_pass, address, postal, mobile, username, password):
    itr = 1 if isinstance(db.reference('/citizen_registration_data', app=cred_app).get(), type(None)) else len(db.reference('/citizen_registration_data').get())
    data = {"firstname" : firstname,
            "lastname" : lastname,
            "email" : email,
            "email_pass" : email_pass,
            "address" : address,
            "postal" : postal,
            "mobile" : mobile,
            "username" : username,
            "password" : password}
    db.reference('/citizen_registration_data/' + str(itr) + '/', app=cred_app).update(data)
    print("registered successfully")

# get the details from database
def get_citizen_details():
    if isinstance(db.reference('/citizen_registration_data', app=cred_app).get(), type(None)):
        print("no data found in citizen registration database")
    else:
        firstnames, lastnames, emails, addresses, postals, mobile_nos, usernames = [], [], [], [], [], [], []
        for i in range(len(db.reference('/citizen_registration_data', app=cred_app).get()) - 1):
            root = db.reference('/citizen_registration_data/' + str(i + 1) + '/', app=cred_app)
            firstnames.append(root.get()['firstname'])
            lastnames.append(root.get()['lastname'])
            emails.append(root.get()['email'])
            addresses.append(root.get()['address'])
            postals.append(root.get()['postal'])
            mobile_nos.append(root.get()['mobile'])
            usernames.append(root.get()['username'])
        return firstnames, lastnames, emails, addresses, postals, mobile_nos, usernames

# check the login details of citizen
def check_citizen_login(username, password):
    if isinstance(db.reference('/citizen_registration_data', app=cred_app).get(), type(None)):
        print("no data found in citizen registration database")
        return False
    else:
        for i in range(len(db.reference('/citizen_registration_data', app=cred_app).get()) - 1):
            root = db.reference('/citizen_registration_data/' + str(i + 1) + '/', app=cred_app)
            if root.get()['username'] == username and root.get()['password'] == password:
                return True
        return False

# send citizen's address, postal code, mobile number when alert is to be sent
def alert_citizen_details(logged_in_username, logged_in_password):
    if isinstance(db.reference('/citizen_registration_data', app=cred_app).get(), type(None)):
        print("no data found in citizen registration database")
        return None
    else:
        for i in range(len(db.reference('/citizen_registration_data', app=cred_app).get()) - 1):
            root = db.reference('/citizen_registration_data/' + str(i + 1) + '/', app=cred_app)
            if root.get()['username'] == logged_in_username and root.get()['password'] == logged_in_password:
                return root.get()['address'], root.get()['postal'], root.get()['mobile'], root.get()['firstname'], root.get()['lastname']
        return None