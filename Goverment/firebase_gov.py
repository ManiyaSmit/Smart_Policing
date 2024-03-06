import firebase_admin
from firebase_admin import db, credentials
import numpy as np
import face_recognition, cv2

# initialisation
cred = credentials.Certificate("/home/anton/Desktop/new_code/safecity.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "https://safecity-8381b-default-rtdb.asia-southeast1.firebasedatabase.app/"})

#db.reference("/").update({"missing_person_data" : {}})

# insert criminal data into firebase
def insert_into_criminal_database(firstname, lastname, age, gender, description, image):
    itr = 1 if isinstance(db.reference('/criminal_data').get(), type(None)) else len(db.reference('/criminal_data').get())
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encoded_image = face_recognition.face_encodings(image)[0].tolist()
    data_to_be_inserted = {'firstname' : firstname, 
                           'lastname' : lastname, 
                           'age' : age,
                           'gender' : gender, 
                           'desc' : description,
                           'encoded_image' : encoded_image}
    db.reference('/criminal_data/' + str(itr) + '/').update(data_to_be_inserted)
    print("inserted successfully!")

# get the encoded images from the firebase
def retrieved_criminal_encoded_imgs():
    path = '/criminal_data/'
    ENCODED_CRIMINAL_IMAGES = []
    if isinstance(db.reference(path), type(None)):
        return
    else:
        for i in range(len(db.reference(path).get()) - 1):
            img = np.array(db.reference(f'{path}{str(i + 1)}').get()['image'])
            ENCODED_CRIMINAL_IMAGES.append(img)
            print(f"retrieveing image : {i}")
        return ENCODED_CRIMINAL_IMAGES

# once the criminal is detected, get the rest details about criminal
def get_criminal_data(min_ind):
    FIRSTNAME = db.reference(f'/criminal_data/{min_ind + 1}').get()['firstname']
    LASTNAME = db.reference(f'/criminal_data/{min_ind + 1}').get()['lastname']
    AGE = db.reference(f'/criminal_data/{min_ind + 1}').get()['age']
    GENDER = db.reference(f'/criminal_data/{min_ind + 1}').get()['gender']
    DESC = db.reference(f'/criminal_data/{min_ind + 1}').get()['desc']
    return FIRSTNAME, LASTNAME, AGE, GENDER, DESC

#--------------------------------------------------------------------------------------------------------------

# insert missing person data into database
def insert_into_missing_person_database(firstname, lastname, age, gender, description, image):
    itr = 1 if isinstance(db.reference('/missing_person_data').get(), type(None)) else len(db.reference('/criminal_data').get())
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encoded_image = face_recognition.face_encodings(image)[0].tolist()
    data_to_be_inserted = {'firstname' : firstname, 
                           'lastname' : lastname, 
                           'age' : age,
                           'gender' : gender, 
                           'desc' : description,
                           'encoded_image' : encoded_image}
    db.reference('/missing_person_data/' + str(itr) + '/').update(data_to_be_inserted)
    print("inserted successfully!")

# get the encoded images from the firebase
def retrieved_missing_person_encoded_imgs():
    path = '/missing_person_data/'
    ENCODED_MISSING_PERSON_IMAGES = []
    if isinstance(db.reference(path), type(None)):
        return
    else:
        for i in range(len(db.reference(path).get()) - 1):
            img = np.array(db.reference(f'{path}{str(i + 1)}').get()['image'])
            ENCODED_MISSING_PERSON_IMAGES.append(img)
            print(f"retrieveing image : {i}")
        return ENCODED_MISSING_PERSON_IMAGES

# once the criminal is detected, get the rest details about criminal
def get_missing_person_data(min_ind):
    FIRSTNAME = db.reference(f'/missing_person_data/{min_ind + 1}').get()['firstname']
    LASTNAME = db.reference(f'/missing_person_data/{min_ind + 1}').get()['lastname']
    AGE = db.reference(f'/missing_person_data/{min_ind + 1}').get()['age']
    GENDER = db.reference(f'/missing_person_data/{min_ind + 1}').get()['gender']
    DESC = db.reference(f'/missing_person_data/{min_ind + 1}').get()['desc']
    return FIRSTNAME, LASTNAME, AGE, GENDER, DESC