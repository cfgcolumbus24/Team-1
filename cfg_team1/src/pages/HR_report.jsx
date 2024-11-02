import './HR_Report.css';
import line2 from '../assets/line-2-10.svg';
import line1 from '../assets/line-1-13.svg';
import line3 from '../assets/line-3-4.svg';
import eclipse from '../assets/ellipse-1-11.svg';
import eclipse2 from '../assets/ellipse-2-14.svg';
import polygon from '../assets/polygon-1-15.svg';
import image1 from '../assets/image-1-16.png';
import image2 from '../assets/image-2-17.png';
import image3 from '../assets/image-3-18.png';
import image4 from '../assets/image-4-19.png';
import image5 from '../assets/image-5-20.png';

const HR_Report = () => {
  return (
    <div className='hr-report-1'>
      <div className='rectangle-4138-2'></div>
      <p className='text-3'>LOG OFF</p>
      <img src={line3} className='line-3-4' alt='line-3' />
      <p className='text-5'>REPORTS</p>
      <p className='text-6'>REPORTS</p>
      <p className='text-7'>Financial Team</p>
      <p className='text-8'>Demographics </p>
      <p className='text-9'>Distrubution</p>
      <img src={line2} className='line-2-10' alt='line-2' />
      <img src={eclipse} className='ellipse-1-11' alt='ellipse-1' />
      <p className='text-12'> </p>
      <img src={line1} className='line-1-13' alt='line-1' />
      <img src={eclipse2} className='ellipse-2-14' alt='ellipse-2' />
      <img src={polygon} className='polygon-1-15' alt='polygon-1' />
      <img src={image1} className='image-1-16' alt='image-1' />
      <img src={image2} className='image-2-17' alt='image-2' />
      <img src={image3} className='image-3-18' alt='image-3' />
      <img src={image4} className='image-4-19' alt='image-4' />
      <img src={image5} className='image-5-20' alt='image-5' />
    </div>
  );
};

export default HR_Report;
