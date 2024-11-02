import './patientoverview.css'; // Add your custom CSS for styling
import './patientoverview.css';
// import patientItem from '../components/patientItem/patientItem';

const PaintentOverview = () => {
  return (
    <div className='home-container'>
      <div className='patient-sidebar'>
        <div className='profile-icon'>
          {' '}
          {/* Placeholder for Profile Icon */}{' '}
        </div>
        <div className='sidebar-item'>Home Page</div>
        <div className='sidebar-item'>Reports</div>
        <div className='sidebar-item'>Log Off</div>
      </div>
      <div className='patient-content'>
        <div className='flexSearch'>
          <p className='searchBar'>Search</p>
          <p className='filter'>filter</p>
        </div>
      </div>
    </div>
  );
};

export default PaintentOverview;
