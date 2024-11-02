# Import necessary modules
from flask import Flask, jsonify, request, abort
import csv
import os

# Define the file path for the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'patient_data1.csv')

# Initialize the Flask app
app = Flask(__name__)

# Function to read the patient data from CSV and parse it into a list of dictionaries
def read_patient_data(file_path):
    patients = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                patients.append(row)
        print('CSV file successfully processed')
        return patients
    except Exception as e:
        print(f'Error reading CSV file: {e}')
        raise e

# Root route to confirm the server is running
@app.route('/')
def home():
    return 'Welcome to the Patient Data API!'

# Endpoint to get all patient data
@app.route('/patients', methods=['GET'])
def get_all_patients():
    try:
        patients = read_patient_data(csv_file_path)
        return jsonify(patients)
    except Exception as e:
        abort(500, description='Error reading patient data')

# Endpoint to get a specific patient by ID
@app.route('/patients/<id>', methods=['GET'])
def get_patient_by_id(id):
    try:
        patients = read_patient_data(csv_file_path)
        patient = next((p for p in patients if p['Patient ID'] == id), None)
        if patient:
            return jsonify(patient)
        else:
            abort(404, description=f'Patient with ID {id} not found.')
    except Exception as e:
        abort(500, description='Error reading patient data')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
