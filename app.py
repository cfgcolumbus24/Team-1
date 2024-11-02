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
@app.route('/patient/<id>', methods=['GET'])
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
    if not request.json or 'messages' not in request.json:
        abort(400, description='Invalid request: missing query parameter')

    query = request.json['messages'][0]['text']

    # Construct the payload for content generation
    payload = f"Generate only the SQL query with no additional text based on this structure. DO NOT INCLUDE ANY NEWLINES OR SPECIAL CHARATERS IN THE RESPONSE. The database is called patient. Do not wrap it in code formatting, just plaintext. If the query has nothing to do with data, just respond with an emoticon smiley face: patient_id, name, address, phone_number, age, race, gender, insurance, smoking, physical_activity, alcohol, support_system. Query: {query}"

    try:
        # Generate content using the model
        response = model.generate_content(payload)
        print("Hugging Face API response:", response)  # Debug line

        # Extract the text content from the response
        generated_response = response.text

        if not generated_response:
            return jsonify({"text": "The bot was unable to generate a prompt to retrieve the data. Please try again."})
            # abort(500, description='Error: Failed to generate response from the API')

       # Execute the generated SQL query
        conn = connect_to_db()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(generated_response)
            result_data = cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error executing generated query: {err}")
            return jsonify({"text": "The bot was unable to generate a prompt to retrieve the data. Please try again."})
            # abort(500, description='Error executing generated query')
        finally:
            cursor.close()
            conn.close()

        # Use the result data to generate a response with the model
        data_summary_payload = f"Summarize the following data: {json.dumps(result_data)}"
        response_summary = model.generate_content(data_summary_payload)
        print("Generated summary response:", response_summary)  # Debug line

        summary_text = response_summary.text

        if not summary_text:
            abort(500, description='Error: Failed to generate summary from the API')

        return jsonify({"text": summary_text})


    except Exception as e:
        print(f"Error processing the request: {e}")
        abort(500, description='Error processing the request')


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)