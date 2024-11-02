import './patientoverview.css'; // Add your custom CSS for styling
import './patientoverview.css';
// import patientItem from '../components/patientItem/patientItem';

const PaintentOverview = () => {
  return (
    <div className='home-container'>
      <div className='sidebar'>
        <div className='profile-icon'>
          {' '}
          {/* Placeholder for Profile Icon */}{' '}
        </div>
        <div className='sidebar-item'>Home Page</div>
        <div className='sidebar-item'>Reports</div>
        <div className='sidebar-item'>Log Off</div>
      </div>

      <div className='search-bar'>
        <input type='text' placeholder='Search' className='search-input' />
      </div>

      <div>
        <button className='filter-button'> Filter</button>
      </div>

      <div>
        {/* <div class="patient-item">

          <div class ="patient-image"></div>
          <span class="patient-name"> Name</span>
        </div>

        <div class="patient-item">
          <div class ="patient-image"></div>
          <span class="patient-name"> Name</span>
        </div> */}
      </div>
      <div className='patient-item'>
        <patient-item name='John Doe' />
        <patient-item name='Jane Smith' />
      </div>
    </div>
  );
};

export default PaintentOverview;
