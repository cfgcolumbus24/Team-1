import {BrowserRouter, Routes, Route} from 'react-router-dom';
import './App.css';

// Importing page components
import HR_Report from './pages/HR_report';
import Login from './pages/login';
import PatientOverview from './pages/paitentoverview';
import SinglePatientOverview from './pages/SinglePaitentOverview';
import Home from './pages/home';

function App() {
  return (
    <BrowserRouter>
      {/* Routing setup */}
      <Routes>
        <Route path='/chat' element={<Home />} />
        <Route path='/hr-report' element={<HR_Report />} />
        <Route path='/' element={<Login />} />
        <Route path='/patient-overview' element={<PatientOverview />} />
        <Route
          path='/single-patient-overview'
          element={<SinglePatientOverview />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
