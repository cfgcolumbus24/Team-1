from flask import Flask, jsonify, request, abort
import mysql.connector

# Initialize the Flask app
app = Flask(__name__)

# Connect to the MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user=None,
            password=None,
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
        query = """SELECT * FROM patient_data WHERE name LIKE %s"""
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
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM patient_data")
        patients = cursor.fetchall()
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
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM patient_data WHERE patient_id = %s", (id,))
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

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
