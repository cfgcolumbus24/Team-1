import Sidebar from '../components/Sidebar/Sidebar';
import './SinglePaitentOverview.css';
import graph from '../assets/graph.png';
import {useEffect, useState} from 'react';
import {useSearchParams} from 'react-router-dom';

const SinglePaitentOverview = () => {
  const [searchParams] = useSearchParams();
  const id = searchParams.get('id');
  const [patientData, setPatientData] = useState({});
  useEffect(() => {
    const fetchPatientData = async () => {
      try {
        const response = await fetch(
          `http://ec2-3-80-140-21.compute-1.amazonaws.com:3000/patient/${id}`,
        );
        const data = await response.json();
        setPatientData(data); // Assuming the response is an array of patients
        console.log(data);
      } catch (error) {
        console.error('Error fetching patient data:', error);
      }
    };

    fetchPatientData();
  }, []);
  return (
    <div className='sPatientOverview'>
      <Sidebar patientData={patientData} />
      <div className='pRecordDiv'>
        <div className='patient'>
          <p className='pRecord'>Patient And Records</p>
          <img src={graph} alt='graph' className='image' />
        </div>
        <div className='ph9q'>
          <p className='pRecord'>PH9Q</p>
          <img src={graph} alt='graph' className='image' />
        </div>
      </div>
    </div>
  );
};

export default SinglePaitentOverview;
