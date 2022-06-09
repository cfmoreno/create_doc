import math
from datetime import datetime
import random
import string
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
from psycopg2 import Error
from firebase_admin import db

def run():

    df = pd.DataFrame()

    try:
        ntotal = input('Ingrese cantidad de Pago Movil a crear: ')
        ntotal = int(ntotal)
    except:
        print('El numero de Pago Moviles a crear debe ser un numero entero')
        exit()

    n = 0

    while n < ntotal:

        DocumentID ='CARLOS'+ str(n) +''.join(random.choices(string.ascii_uppercase + string.digits, k=13))

        try:

            monto = input('ingrese monto de Pago Movil: ')
            monto = float(monto)
        except:
            print('Por favor ingrese solo numeros para el monto del Pago Movil')
            exit()

            
        document = {
                
            'banco' : '0138',
            'monto' : str(monto),
            'referencia' : DocumentID
            
            }


        class DbHandler:

            def __init__(self, cred, document, ID):
                #get credentials
                self.cred = firebase_admin.credentials.Certificate(cred)
                #call Authenticate function 
                self.authenticate()
                self.document = document
                self.id = ID
                
            def authenticate(self):
                #initialize the firebase_admin
                self.app = firebase_admin.initialize_app(self.cred)
                # initialize storage client
                self.db = firebase_admin.firestore.client()
                # upload data to firebase you need the user id if the data is Private or Public (data_type) the name of the document (info) and the data you want to upload 
            #def upload_data_document(self, userId, data_type, info, data):
            
            #def upload_data_document(self, document, ID):
            def upload_data_document(self):
                #self.db.collection('config').document('PagoMovil').collection('cableados').document(ID).set(document)
                self.db.collection('config').document('PagoMovil').collection('cableados').document(self.id).set(self.document)
                
            def close(self):
                
                # self.close()
                firebase_admin.delete_app(self.app)
                
                #self.upload_data_document(self.document)

                #update data on the database
        #       def upload_data(self, userId, data_type, info, data):

        #        self.db.collection('User').document(userId).collection(data_type).document(info).update(data)


        db = DbHandler('cred.json', document, document['referencia'])

        db.db.project

        #db.upload_data_document(db.document, document['referencia'])
        db.upload_data_document()

        db.close()

        document = {
            
        'banco' : '0138',
        'monto' : str(monto),
        'referencia' : DocumentID,
        '' : ''
        
        }

        doc=pd.DataFrame(document , index=[n+1]).loc[n+1]

        #DEPRECADO        
        #df = df.append(doc)

        df = pd.concat([df, doc])

        df.to_excel('newPM.xlsx')

        n += 1

    print(df)


if __name__ == '__main__':
    run()