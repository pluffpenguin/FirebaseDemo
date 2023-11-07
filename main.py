import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth


cred = credentials.Certificate("./config.json")
firebase_admin.initialize_app(cred)