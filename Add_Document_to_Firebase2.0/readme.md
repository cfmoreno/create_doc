Script developed for automating the creation of a valid Pago Movil in Firebase which receives number of iterations to do and amount for each iteration

Requirements: 

1. It is required that the database_handler.py file is present in the same path as the create_pm.py file
2. A credentials json should be created from firebase and added as 'cred.json' on the same path as create_pm file

How to test:

After fulfilling the requirements above, run the script and enter bowth inputs:

First input requires the number of Pago movil to create (iterations)

Second input requires the amount of Bs. to set for each Pago movil

Finally, after creation, test the Pago Movil in Staging (Web or App). Buying products for the amount set in the second input.

Additionally you can just check the 'cableados' collection in firebase as these are the Pago movil used in staging, documents created there will work in staging