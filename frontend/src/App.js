import { auth, db } from './Firebase';
import { useAuthState } from 'react-firebase-hooks/auth';
import { Routes, Route } from 'react-router-dom';
import Home from './scenes/index';

function App() {
  const [user, loading] = useAuthState(auth);

  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;
