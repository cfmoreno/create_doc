# Firestore Document Creation Tool

This script automates the creation of documents in a Firestore database. It prompts the user for document data and uploads it to a specified collection. Additionally, it saves the created document data to an Excel file.

This tool is designed to streamline the process of populating Firestore with structured data, which can be useful for various purposes, including testing, data migration, and initial data setup.

## Requirements

1.  Python 3.9 or higher.
2.  Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure `requirements.txt` includes `firebase-admin`, `pandas`, and any other necessary libraries.)
3.  A Firebase service account credentials JSON file (e.g., `cred.json`) must be placed in the same directory as the script.
4.  The `db_handler.py` file must be present in the same directory as the main script.

## How to Use

1.  **Prepare Credentials:** Download your Firebase service account credentials JSON file and rename it to `cred.json`. Place it in the script's directory.
2.  **Install Dependencies:** Run `pip install -r requirements.txt` to install the required Python packages.
3.  **Run the Script:** Execute the main script using Python:
    ```bash
    python your_script_name.py
    ```
4.  **Enter Document Data:**
    * The script will prompt you to enter the number of documents to create.
    * For each document, you will be prompted to enter field names and their corresponding values.
    * Type `end` when you have finished entering fields for a document.
5.  **Verify Data:**
    * The script will upload the documents to your Firestore collection.
    * The created document data will also be saved to an Excel file named `new_documents.xlsx` in the same directory.
    * You can verify the created documents in the Firestore console.

## Customization

* **Credentials:** Replace `cred.json` with the path to your Firebase credentials file if it's named differently or located elsewhere.
* **Collection Path:** Modify the collection path (`'config/PagoMovil/cableados'`) in the `db_handler.py` file to match your desired Firestore collection.
* **Excel File Name:** Change the Excel file name (`'new_documents.xlsx'`) in the main script to your preferred name.
* **Document Structure:** Customize the document structure by modifying the `get_document_data()` function in the main script.
* **Error Handling:** Enhance error handling by catching specific exceptions and providing more informative error messages.
* **Logging:** Implement logging to record script activity and errors.
* **Input Validation:** Add input validation to ensure that user input is in the correct format.