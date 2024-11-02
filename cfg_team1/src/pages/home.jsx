import React from 'react';
import './Home.css'; // Add your custom CSS for styling

const Home = () => {
  return (
    <div className="home-container">
      {/* Sidebar */}
      <div className="sidebar">
        <div className="profile-icon"> {/* Placeholder for Profile Icon */} </div>
        <div className="sidebar-item">Home Page</div>
        <div className="sidebar-item">Reports</div>
        <div className="sidebar-item">Log Off</div>
      </div>

      {/* Main Chat Area */}
      <div className="main-content">
        {/* Search Bar */}
        <div className="search-bar">
          <input type="text" placeholder="Search" className="search-input" />
        </div>

        {/* Chat Area */}
        <div className="chat-area">
          <div className="chat-bubble user-query">Yap Yap Yap Blah Blah Blah </div>
          <div className="chat-bubble response">Hello world!</div>
        </div>

        {/* Input Area */}
        <div className="input-area">
          <input type="text" placeholder="Type here!" className="chat-input" />
        </div>
      </div>
    </div>
  );
};

export default Home;
