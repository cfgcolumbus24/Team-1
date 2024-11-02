// PatientItem.js
import React from 'react';
import './patientItem.css';

const patientItem = ({ name }) => {
  return (
    <div className="patient-item">
      <div className="patient-image"></div>
      <span className="patient-name">{name}</span>
    </div>
  );
};

export default patientItem;
