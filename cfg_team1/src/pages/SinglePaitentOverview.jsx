import Sidebar from '../components/Sidebar/Sidebar';
import './SinglePaitentOverview.css';
import graph from '../assets/graph.png';

const SinglePaitentOverview = () => {
  return (
    <div className='sPatientOverview'>
      <Sidebar />
      <div className='pRecordDiv'>
        <div className='patient'>
          <p className='pRecord'>Patient And Records</p>
          <div className='patientdiv'></div>
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
