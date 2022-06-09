import firebase_admin
from firebase_admin import credentials, firestore
from psycopg2 import Error
from firebase_admin import db

class DbHandler:

    def __init__(self, cred, document, ID):
        #get credentials
        self.cred = firebase_admin.credentials.Certificate(cred)
        #call Authenticate function 
        self.authenticate()
        #set the document to upload
        self.document = document
        #set the id of the document
        self.id = ID
        
    def authenticate(self):
        #initialize the firebase_admin
        self.app = firebase_admin.initialize_app(self.cred)
        #initialize storage client
        self.db = firebase_admin.firestore.client()
         

    def upload_data_document(self):
    #upload data to firebase you need the user id if the data is Private 
    #or Public (data_type) 
        self.db.collection('config').document('PagoMovil').collection('cableados').document(self.id).set(self.document)
        #update data on the database on the selected collection (path)
    def close(self):
        firebase_admin.delete_app(self.app)
    #end connection to database