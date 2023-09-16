import { auth, db } from './Firebase';
import { useAuthState } from 'react-firebase-hooks/auth';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Note the import change here
import Home from './scenes/index';
import Login from './scenes/login';

function App() {
  const [user, loading] = useAuthState(auth);

  return (
    <div className="App">
      <Router> {/* Wrap your Routes with Router */}
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/home" element={<Home />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
