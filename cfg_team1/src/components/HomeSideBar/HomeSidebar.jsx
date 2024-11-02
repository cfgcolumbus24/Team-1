import {useNavigate} from 'react-router-dom';
import logo from '../../assets/logo.png';

const HomeSidebar = () => {
  const navigate = useNavigate();
  return (
    <>
      {/* Sidebar */}
      <div className='sidebar'>
        <img
          src={logo}
          className='profile-icon'
          onClick={() => navigate('/')} // Navigate to home page when clicked
          style={{cursor: 'pointer'}}
        />
        <div
          className='sidebar-item'
          onClick={() => navigate('/patient-overview')}
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
