import ChatBox from './chatbox';
import HomeSidebar from '../components/HomeSideBar/HomeSidebar';
import './Home.css'; // Add your custom CSS for styling

const Home = () => {
  return (
    <div className='home-container'>
      <HomeSidebar />
      {/* Main Chat Area */}
      <div className='main-content'>

        {/* Chat Area */}
        <ChatBox/>

      </div>
    </div>
  );
};

export default Home;
