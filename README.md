<h1>Create a Document for Firebase</h1>

Script developed for automating the creation of a valid Pago Movil (Payment method in Venezuela) in Firebase which receives number of iterations to do and amount for each iteration.

This script was created to automate the QA Process of Payment Methods testing on an Online Pharmacy Web Page and Mobile App (iOS & Android). To proceed with the order, there should be a document in firebase that says "Payment completed" this is a JSON with three parameters. Script creates the JSON and uploads it to Firebase.

With this script we are able to automate and complete the process a lot faster and efficiently

<h1>Requirements</h1>

0. Any version of Python >= 3.9 will be sufficient

1. Use pip install to install the requirements.txt using the following command: "pip install -r requirements.txt" on the project root folder

2. It is required that the database_handler.py file is present in the same path as the add_doc.py file

3. A credentials json should be created from firebase and added as 'cred.json' on the same path as add_doc.py file

4. Run app.py file with "py add_doc.py" or "python3 app.py"

<h1>How to use it</h1>

After fulfilling the requirements above, run the script and enter both inputs:

First input requires the number of Pago movil to create (iterations)

Second input requires the amount of Bs. to set for each Pago movil

Finally, after creation, test the Pago Movil in Staging (Web or App). Buying products for the amount set in the second input.

Additionally you can just check the 'cableados' collection in firebase as these are the Pago movil used in staging, documents created there will work in staging
