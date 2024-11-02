import {useState} from 'react';
import {useNavigate} from 'react-router-dom'; // Import useNavigate for navigation
import './Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); // Initialize useNavigate

  const handleLogin = (e) => {
    e.preventDefault();
    // Mock API call logic (you can add this later)
    console.log('Username:', username);
    console.log('Password:', password);

    // Redirect to home page after clicking Submit
    navigate('/chat');
  };

  return (
    <div className='login-container'>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div className='form-group'>
          <label htmlFor='username'>Username:</label>
          <input
            type='text'
            id='username'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className='form-group'>
          <label htmlFor='password'>Password:</label>
          <input
            type='password'
            id='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type='submit' className='login-button'>
          Submit
        </button>
      </form>
    </div>
  );
};

export default Login;
