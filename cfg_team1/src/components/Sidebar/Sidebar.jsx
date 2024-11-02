import './Sidebar.css';

const Sidebar = ({patientData}) => {
  return (
    <div className='single-sidebar'>
      <div className='eclipse'></div>
      <p className='name'>{patientData.name}</p>
      <div className='ageFlex'>
        <div className='age'>Age: {patientData.age}</div>
        <div className='age race'>Race: {patientData.race}</div>
      </div>
      <div className='address'>Address: {patientData.address}</div>
      <div className='ageFlex'>
        <div className='age'>Smoker: {patientData.smoking}</div>
        <div className='age race'>Gender: {patientData.gender}</div>
      </div>
      <div className='ageFlex'>
        <div className='age'>Active Level: {patientData.physical_activity}</div>
        <div className='age race'>Phone Number: {patientData.phone_number}</div>
      </div>
    </div>
  );
};

export default Sidebar;
