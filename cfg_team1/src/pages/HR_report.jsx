import HomeSidebar from '../components/HomeSideBar/HomeSidebar';
import './HR_report.css';
import imagePie from '../assets/image-1-16.png';
import imageRevenue from '../assets/image-5-20.png';
import imageDemographics from '../assets/image-3-18.png';
import imageAge from '../assets/image-2-17.png';
import imageDistribution from '../assets/image-4-19.png';

const HR_report = () => {
  return (
    <div className='hr-report'>
      <HomeSidebar />
      <div className='revBody'>
        <p className='reportsParagraph'>REPORTS</p>
        <div className='rev'>
          <p>Financial Team</p>
          <div className='revFlex'>
            <img src={imagePie} alt='' />
            <img src={imageRevenue} alt='' />
          </div>
        </div>
        <div className='rev'>
          <p>Demographics</p>
          <div className='revFlex'>
            <img src={imageDemographics} alt='' />
            <img src={imageAge} alt='' />
          </div>
        </div>
        <div className='rev'>
          <p>Distribution</p>
          <div className='revFlex'>
            <img src={imageDistribution} alt='' />
          </div>
        </div>
      </div>
    </div>
  );
};

export default HR_report;
