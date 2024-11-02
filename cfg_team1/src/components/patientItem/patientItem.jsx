// PatientItem.js
import React from 'react';
import './patientItem.css';

const PatientItem = ({ name }) => {
  return (
    <div className="patient-item">
      <div className="patient-image"></div>
      <span className="patient-name">{name}</span>
    </div>
  );
};

export default PatientItem;
