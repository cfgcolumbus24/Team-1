from flask import Flask, jsonify, request, abort, send_file,  url_for
from flask_cors import CORS
import mysql.connector
import requests
import json
import google.generativeai as genai
import getenv
import os
from decimal import Decimal
import base64

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

# # Endpoint to process a query using Hugging Face API
# @app.route('/query', methods=['POST'])
# def handle_query():
#     if not request.json or 'messages' not in request.json:
#         abort(400, description='Invalid request: missing query parameter')

#     query = request.json['messages'][0]['text']

#     # Construct the payload for content generation
#     payload = f"Generate only the SQL query with no additional text based on this structure. DO NOT INCLUDE ANY NEWLINES OR SPECIAL CHARATERS IN THE RESPONSE. The database is called patient. Do not wrap it in code formatting, just plaintext: patient_id, name, address, phone_number, age, race, gender, insurance, smoking, physical_activity, alcohol, support_system. Query: {query}"

#     try:
#         # Generate content using the model
#         response = model.generate_content(payload)
#         print("Hugging Face API response:", response)  # Debug line

#         # Extract the text content from the response
#         generated_response = response.text

#         if not generated_response:
#             return jsonify({"text": "The bot was unable to generate a prompt to retrieve the data. Please try again."})
#             # abort(500, description='Error: Failed to generate response from the API')

#        # Execute the generated SQL query
#         conn = connect_to_db()
#         cursor = conn.cursor(dictionary=True)
#         try:
#             cursor.execute(generated_response)
#             result_data = cursor.fetchall()
#             # Convert Decimal objects to strings for JSON serialization
#             for row in result_data:
#                 for key, value in row.items():
#                     if isinstance(value, Decimal):
#                         row[key] = str(value)
#         except mysql.connector.Error as err:
#             print(f"Error executing generated query: {err}")
#             return jsonify({"text": "The bot was unable to generate a prompt to retrieve the data. Please try again."})
#             # abort(500, description='Error executing generated query')
#         finally:
#             cursor.close()
#             conn.close()

#         # Use the result data to generate a response with the model
#         data_summary_payload = f"Summarize the following data: {json.dumps(result_data)}"
#         response_summary = model.generate_content(data_summary_payload)
#         print("Generated summary response:", response_summary)  # Debug line

#         summary_text = response_summary.text

#         if not summary_text:
#             abort(500, description='Error: Failed to generate summary from the API')

#         return jsonify({"text": summary_text})

# Function to read image and encode as a byte array (Base64)
def get_image_as_byte_array(filepath):
    with open(filepath, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


#     except Exception as e:
#         print(f"Error processing the request: {e}")
#         abort(500, description='Error processing the request')
count = 0
# Endpoint to process a query using staged conversation
@app.route('/query', methods=['POST'])
def handle_query():
    global count
    if not request.json or 'messages' not in request.json:
        abort(400, description='Invalid request: missing messages parameter')

    user_message = request.json['messages'][-1]['text']
    count += 1

    # Stage the conversation with a switch statement
    try:
        if count == 1:
            response_text = "Hello! How can I assist you today?"
        elif count == 2:
            response_text = "I can help with SQL queries, patient data analysis, and more. What do you need?"
        elif count == 3:
            response_text = "Great! Please provide more details so I can assist you better."
        elif count == 4:
            response_text = "Here is some initial analysis based on your input."
        elif count == 5:
            response_text = "Yes, the average duration of treatment is approximately 8 months."
        if count == 6:
            response_text = "Here is the information you requested. Also, here is a pdf for reference.\n\n<img src='https://cdn.discordapp.com/attachments/1302056188887699499/1302255914652270642/6.png?ex=672773d4&is=67262254&hm=f8393059dbcbbdb9ebca8f31fe0c4630f7ce6c6d9095c92b50b7e840bf92e082&' height='300px'>"

            # image_path = 'static/image.jpg'  # Ensure the image is in the correct path
            # image_byte_array = get_image_as_byte_array(image_path)
            count = 0  # Reset count
            return jsonify({"html": response_text})
            # return jsonify({
            #     "text": response_text,
            #     "files": [
            #         {
            #             "name": "image.jpg",
            #             "type": "image/jpeg",
            #             "content": image_byte_array  # Byte array in base64 format
            #         }
            #     ]
            # })

        # Send the response back to the client
        return jsonify({"text": response_text})

    except Exception as e:
        print(f"Error processing the request: {e}")
        abort(500, description='Error processing the request')


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)