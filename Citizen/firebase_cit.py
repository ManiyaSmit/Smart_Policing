import firebase_admin
from firebase_admin import db, credentials
import numpy as np
import face_recognition, cv2

# initialisation
cred = credentials.Certificate("/home/anton/Desktop/new_code/safecity.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "https://safecity-8381b-default-rtdb.asia-southeast1.firebasedatabase.app/"})

# get the encoded images from the firebase
def retrieve_criminal_encoded_imgs():
    path = '/criminal_data/'
    ENCODED_CRIMINAL_IMAGES = []
    if isinstance(db.reference(path), type(None)):
        return
    else:
        for i in range(len(db.reference(path).get()) - 1):
            img = np.array(db.reference(f'{path}{str(i + 1)}').get()['encoded_image'])
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