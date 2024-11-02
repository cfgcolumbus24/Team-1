// Import necessary modules
const express = require('express');
const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

// Define the file path for the CSV file
const csvFilePath = path.join(__dirname, 'data', 'patient_outcomes.csv');

// Initialize the Express app
const app = express();
const PORT = 3000;

// Function to read the patient data from CSV and parse it into an array of objects
const readPatientData = (filePath) => {
  return new Promise((resolve, reject) => {
    const patients = [];

    fs.createReadStream(filePath)
      .pipe(csv())
      .on('data', (row) => {
        patients.push(row);
      })
      .on('end', () => {
        console.log('CSV file successfully processed');
        resolve(patients);
      })
      .on('error', (error) => {
        reject(error);
      });
  });
};

// Root route to confirm the server is running
app.get('/', (req, res) => {
  res.send('Welcome to the Patient Outcomes API!');
});
// Endpoint to get all patient data
app.get('/patients', async (req, res) => {
    try {
      const patients = await readPatientData(csvFilePath);
      res.json(patients);
    } catch (error) {
      res.status(500).send('Error reading patient data');
    }
  });
  
  // Endpoint to get a specific patient by ID
  app.get('/patients/:id', async (req, res) => {
    const patientId = req.params.id;
    try {
      const patients = await readPatientData(csvFilePath);
      const patient = patients.find((p) => p['Patient ID'] === patientId);
      if (patient) {
        res.json(patient);
      } else {
        res.status(404).send(`Patient with ID ${patientId} not found.`);
      }
    } catch (error) {
      res.status(500).send('Error reading patient data');
    }
  });
  
  // Start the server
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
  