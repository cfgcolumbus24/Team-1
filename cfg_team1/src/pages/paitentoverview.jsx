import React, { useEffect, useState } from 'react';
import './patientoverview.css';
import HomeSidebar from '../components/HomeSideBar/HomeSidebar';
import {useNavigate} from 'react-router-dom';

const PatientOverview = () => {
  const [patients, setPatients] = useState([]);
  const [filteredPatients, setFilteredPatients] = useState([]); // Ensure this is initialized as an array
  const [name, setName] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPatients = async () => {
      try {
        const response = await fetch('http://ec2-3-80-140-21.compute-1.amazonaws.com:3000/patients');
        const data = await response.json();
        setPatients(data); // Assuming the response is an array of patients
        setFilteredPatients(data); // Initialize filteredPatients with all patients
        console.log(data);
      } catch (error) {
        console.error('Error fetching patient data:', error);
      }
    };

    fetchPatients();
  }, []);

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  const handleFilterClick = async (event) => {
    event.preventDefault(); // Prevent form submission
    const results = await searchPatientsByName(name);
    if (Array.isArray(results)) {
      setFilteredPatients(results); // Update filteredPatients only if results is an array
    } else {
      setFilteredPatients([]); // If not an array, reset to an empty array
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      handleFilterClick(event); // Trigger search on Enter key press
    }
  };

  async function searchPatientsByName(name) {
    try {
      const response = await fetch('http://ec2-3-80-140-21.compute-1.amazonaws.com:3000/patients/search?name=' + encodeURIComponent(name));
      const data = await response.json();

      if (response.ok) {
        console.log('Patients:', data);
        return data; // Return the matched patients
      } else {
        console.log('No patients found matching the search query.');
        return []; // Return an empty array if no patients found
      }
    } catch (error) {
      console.error('Error processing the search request:', error.message);
      return []; // Return an empty array in case of error
    }
  }

  return (
    <div className='home-container'>
      <HomeSidebar />

      <div className='content'>
        <form className='search-bar' onSubmit={handleFilterClick}>
          <input 
            type='text' 
            placeholder='Search' 
            className='search-input' 
            value={name} 
            onChange={handleInputChange} 
            onKeyPress={handleKeyPress} // Listen for key presses
          />
          <button type="submit" className="filter-button">Filter</button>
        </form>

        <div className='patient-list'>
          {Array.isArray(filteredPatients) && filteredPatients.map(patient => (
            <div className="patient-item" key={patient.id}>
              {/* <div className="patient-image"></div> */}
              <span className="patient-name" onClick={() => navigate('/single-patient-overview')}>{patient.name}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default PatientOverview;
