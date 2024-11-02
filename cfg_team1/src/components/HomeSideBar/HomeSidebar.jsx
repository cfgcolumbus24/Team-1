import React from 'react';
import {useNavigate} from 'react-router-dom';

const HomeSidebar = () => {
  const navigate = useNavigate();
  return (
    <>
      {/* Sidebar */}
      <div className='sidebar'>
        <div
          className='profile-icon'
          onClick={() => navigate('/')} // Navigate to home page when clicked
          style={{cursor: 'pointer'}}
        ></div>
        <div
          className='sidebar-item'
          onClick={() => navigate('/patient_overview')}
        >
          {' '}
          Paitient Page
        </div>
        <div className='sidebar-item' onClick={() => navigate('/hr-report')}>
          Reports
        </div>
        <div className='sidebar-item' onClick={() => navigate('/logout')}>
          Log Off
        </div>
      </div>
    </>
  );
};

export default HomeSidebar;
