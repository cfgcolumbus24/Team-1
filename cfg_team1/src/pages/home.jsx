import HomeSidebar from '../components/HomeSideBar/HomeSidebar';
import './Home.css'; // Add your custom CSS for styling

const Home = () => {
  return (
    <div className='home-container'>
      <HomeSidebar />

      {/* Main Chat Area */}
      <div className='main-content'>

        {/* Chat Area */}
        <div className='chat-area'>
          <div className='chat-bubble user-query'>
            Yap Yap Yap Blah Blah Blah{' '}
          </div>
          <div className='chat-bubble response'>Hello world!</div>
        </div>

        {/* Input Area */}
        <div className='input-area'>
          <input type='text' placeholder='Type here!' className='chat-input' />
        </div>
      </div>
    </div>
  );
};

export default Home;
