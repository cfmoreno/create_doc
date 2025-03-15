import random
import string
import pandas as pd
from database_handler import DbHandler

def generate_random_id(prefix="DOC", length=10):
    """Generates a random alphanumeric ID with an optional prefix."""
    characters = string.ascii_uppercase + string.digits
    return prefix + ''.join(random.choices(characters, k=length))

def get_document_data():
    """Prompts the user to enter data for a document and returns it as a dictionary."""
    data = {}
    while True:
        key = input("Enter field name (or 'end' to finish): ").strip()
        if key.lower() == 'end':
            break
        value = input(f"Enter value for field '{key}': ").strip()
        data[key] = value
    return data

def process_document(db, document_data, document_id):
    """Processes a single document, uploading it to Firestore."""
    document_data['reference'] = document_id
    try:
        db.upload_data_document() # upload to firestore.
        return document_data
    except Exception as e:
        print(f"Error processing document {document_id}: {e}")
        return None

def run():
    """
    Prompts the user for the number of documents to create, then for the data of each document,
    uploads it to Firestore using DbHandler, and finally saves the data to an Excel file.
    """
    document_list = []
    try:
        num_documents = int(input('Enter the number of documents to create: '))
        db = DbHandler('cred.json', {}, '')
        for i in range(num_documents):
            print(f"\n--- Entering data for document {i + 1} ---")
            document_data = get_document_data() # get the document data from the user.
            document_id = generate_random_id(prefix=f"DOC{i+1}_") # generate document ID.
            db.document = document_data # set document to upload.
            db.document_id = document_id # set document ID.
            processed_data = process_document(db, document_data, document_id)
            if processed_data:
                document_list.append(processed_data) # add the document to the list.
            print(f"Document {i+1} processed") # progress indicator
        db.close()
        df = pd.DataFrame(document_list) # create the data frame from the list.
        df.to_excel('new_documents.xlsx', index=False) # save the dataframe to excel.
        print("\n--- Data of created documents ---")
        print(df)

    except ValueError:
        print('The number of documents to create must be an integer.') # handle invalid input.
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 

if __name__ == '__main__':
    run()