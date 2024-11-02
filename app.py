from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import mysql.connector
import requests
import json
import google.generativeai as genai
import getenv
import os

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Add gemini
genai.configure(api_key=os.getenv('GENAI_API_KEY'))
print(os.getenv('GENAI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")

# Connect to the MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='test',
            password='test',
            database='patient_db'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise err

# Function to search for patients by name
def search_patients_by_name(name):
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM patient WHERE name LIKE %s"
        cursor.execute(query, (f"%{name}%",))
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

# Endpoint to search for patients by name
@app.route('/patients/search', methods=['GET'])
def search_patients():
    if 'name' not in request.args:
        abort(400, description='Invalid request: missing name parameter')
    name_query = request.args['name']
    try:
        patients = search_patients_by_name(name_query)
        if patients:
            return jsonify(patients)
        else:
            return jsonify({"message": "No patients found matching the search query."})
    except Exception as e:
        abort(500, description='Error processing the search request')

# Root route to confirm the server is running
@app.route('/')
def home():
    return 'Welcome to the Patient Data API!'

# Endpoint to get all patient data
@app.route('/patients', methods=['GET'])
def get_all_patients():
    print("GET /patients endpoint called")  # Debug line
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM patient")
        patients = cursor.fetchall()
        if not patients:
            print("No patients found.")  # Debug line
            return jsonify({"message": "No patients found."})
        return jsonify(patients)
    except mysql.connector.Error as err:
        print(f"Error reading patient data: {err}")
        abort(500, description='Error reading patient data')
    finally:
        cursor.close()
        conn.close()

# Endpoint to get a specific patient by ID
@app.route('/patients/<id>', methods=['GET'])
def get_patient_by_id(id):
    print(f"GET /patients/{id} endpoint called")  # Debug line
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM patient WHERE patient_id = %s", (id,))  # Updated table name for consistency
        patient = cursor.fetchone()
        if patient:
            return jsonify(patient)
        else:
            abort(404, description=f'Patient with ID {id} not found.')
    except mysql.connector.Error as err:
        print(f"Error reading patient data: {err}")
        abort(500, description='Error reading patient data')
    finally:
        cursor.close()
        conn.close()

# Endpoint to process a query using Hugging Face API
@app.route('/query', methods=['POST'])
def handle_query():
    if not request.json or 'query' not in request.json:
        abort(400, description='Invalid request: missing query parameter')

    query = request.json['query']

    # Hugging Face API URL and headers
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
    headers = {"Authorization": "Bearer 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"}
#     payload = {
#     "inputs": f"Generate an SQL query using the following database structure: patient_id, name, address, phone_number, age, race, gender, insurance, smoking, physical_activity, alcohol, support_system. Query: {query}"
# }
    payload = f"Generate an SQL query using the following database structure: patient_id, name, address, phone_number, age, race, gender, insurance, smoking, physical_activity, alcohol, support_system. Query: {query}"


    try:
        # Make the API request
        # response = requests.post(API_URL, headers=headers, json=payload)\
        # response.raise_for_status()
        # response_json = response.json()

        response = model.generate_content(payload)
        print("Hugging Face API response:", response)  # Debug line

        # Check if a valid response was returned
        # generated_response = response_json[0]['generated_text'] if response_json else ''

        if not response:
            abort(500, description='Error: Failed to generate response from the API')

        return jsonify({"response": response})

    except requests.exceptions.RequestException as e:
        print(f"Error calling Hugging Face API: {e}")
        abort(500, description='Error processing the request')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)