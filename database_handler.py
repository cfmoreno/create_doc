import firebase_admin
from firebase_admin import credentials, firestore
import logging

logging.basicConfig(level=logging.ERROR)  # Configure logging

class DbHandler:
    """Handles interactions with the Firestore database."""

    def __init__(self, cred_path, document, document_id):
        """
        Initializes the DbHandler.

        Args:
            cred_path (str): Path to the Firebase credentials JSON file.
            document (dict): The document data to upload.
            document_id (str): The ID of the document.
        """
        self.cred_path = cred_path
        self.document = document
        self.document_id = document_id
        self.app = None  # Initialize Firebase app
        self.db = None  # Initialize Firestore client
        self.authenticate()

    def authenticate(self):
        """Authenticates with Firebase and initializes the Firestore client."""
        try:
            cred = credentials.Certificate(self.cred_path)
            self.app = firebase_admin.initialize_app(cred)  # Initialize Firebase app
            self.db = firestore.client()  # Initialize Firestore client
        except Exception as e:
            logging.error(f"Error authenticating with Firebase: {e}")
            raise  # Re-raise the exception to be handled by the caller

    def upload_data_document(self):
        """Uploads the document data to Firestore."""
        try:
            # Upload document to the specified collection and document ID
            self.db.collection('config').document('PagoMovil').collection('cableados').document(self.document_id).set(self.document) # Change to the desired collection and document ID
        except Exception as e:
            logging.error(f"Error uploading document {self.document_id}: {e}")
            raise

    def close(self):
        """Closes the connection to the Firestore database."""
        try:
            if self.app:
                firebase_admin.delete_app(self.app) # Delete the firebase app to close the connection
        except Exception as e:
            logging.error(f"Error closing Firebase connection: {e}")
            raise