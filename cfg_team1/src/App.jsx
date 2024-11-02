import { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

// Importing page components 
import HR_Report from './pages/HR_report';
import Login from './pages/login';
import PatientOverview from './pages/paitentoverview';
import SinglePatientOverview from './pages/SinglePaitentOverview';
import Home from './pages/home';

function App() {
  const [count, setCount] = useState(0);

  return (
    <BrowserRouter>
      <>
        {/* Existing content */}
        <div>
          <a href="https://vite.dev" target="_blank">
            <img src={viteLogo} className="logo" alt="Vite logo" />
          </a>
          <a href="https://react.dev" target="_blank">
            <img src={reactLogo} className="logo react" alt="React logo" />
          </a>
        </div>
        <h1>Vite + React</h1>
        <div className="card">
          <button onClick={() => setCount((count) => count + 1)}>
            count is {count}
          </button>
          <p>
            Edit <code>src/App.jsx</code> and save to test HMR
          </p>
        </div>
        <p className="read-the-docs">
          Click on the Vite and React logos to learn more
        </p>

        {/* Routing setup */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/hr-report" element={<HR_Report />} />
          <Route path="/login" element={<Login />} />
          <Route path="/patient-overview" element={<PatientOverview />} />
          <Route path="/single-patient-overview" element={<SinglePatientOverview />} />
        </Routes>
      </>
    </BrowserRouter>
  );
}

export default App;
