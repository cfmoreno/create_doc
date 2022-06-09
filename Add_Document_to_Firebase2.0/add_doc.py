import random
import string
import pandas as pd
from database_handler import DbHandler

def run():

    try:
        ntotal = int(input('Ingrese cantidad de Pago Movil a crear: '))
    except:
        print('El numero de Pago Moviles a crear debe ser un numero entero')
        exit()

    n = 0

    while n < ntotal:

        DocumentID = str(n)+'CARLOS'+''.join(random.choices(string.ascii_uppercase + string.digits, k=13))

        try:
            monto = float(input('ingrese monto de Pago Movil: '))
        except:
            print('Por favor ingrese solo numeros para el monto del Pago Movil')
            exit()
            
        document = {
            'banco' : '0138',
            'monto' : str(monto),
            'referencia' : DocumentID
            }

        db = DbHandler('cred.json', document, document['referencia']) ##import data to class ('cred' are credentials from firebase in json format) in an instance var 'db'

        db.upload_data_document()

        db.close()

        document[' '] = '' #includes an empty line for better readability on print and on excel file

        df = pd.DataFrame()

        doc=pd.DataFrame(document , index=[n+1]).loc[n+1]

        df = pd.concat([df, doc])

        df.to_excel('newPM.xlsx')

        n += 1

    print(df)

if __name__ == '__main__':
    run()