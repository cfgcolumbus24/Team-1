import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className='sidebar'>
      <div className='eclipse'></div>
      <p className='name'>NAME</p>
      <div className='ageFlex'>
        <div className='age'>Age: </div>
        <div className='age race'>Race: </div>
      </div>
      <div className='address'>Address: </div>
      <div className='ageFlex'>
        <div className='age'>Blood Type: </div>
        <div className='age race'>BMI: </div>
      </div>
      <div className='ageFlex'>
        <div className='age'>Active Level: </div>
        <div className='age race'>Medication Administered: </div>
      </div>
    </div>
  );
};

export default Sidebar;
