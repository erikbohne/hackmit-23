import {useState} from 'react';
import {Box, Button, Typography} from '@mui/material';
import {useNavigate} from 'react-router-dom';
import {signInWithPopup, GoogleAuthProvider} from 'firebase/auth';
import {getFirestore, setDoc, getDoc, doc} from 'firebase/firestore';
import {auth} from '../../Firebase';

const Login = () => {
  const navigate = useNavigate();
  const [error, setError] = useState('');

  const signInWithGoogle = async () => {
    try {
        const provider = new GoogleAuthProvider();
        const result = await signInWithPopup(auth, provider);
        
        // The signed-in user info.
        const user = result.user;
  
        // Check if user exists in your Firestore database
        const db = getFirestore();
        const userRef = doc(db, "users", user.uid);
        const userSnap = await getDoc(userRef);
  
        if (!userSnap.exists()) {
            // Create a new user document
            await setDoc(userRef, {
                username: user.displayName,
                email: user.email,
                createdAt: new Date(),
            });
        }
  
        // You can add navigation logic here if needed
        console.log('Successfully signed in!');
        navigate('/home');
      } catch (error) {
        console.error("Error Code:", error.code);
        console.error("Error Message:", error.message);
        setError(error.message);
     }     
  };  

  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      sx={{
        height: '100vh',
        backgroundColor: '#FFF',
      }}
    >

      {/* Header */}
      <Box
        display="flex"
        flexDirection="column"
        justifyContent="center"
        alignItems="center"
        sx={{
          margin: '20vh 0 20px 0',
          color: '#333',
        }}
      >
        <Typography
          sx={{
            background: "linear-gradient(to left, #F2AA0D, #FF8200)",
            WebkitBackgroundClip: "text",
            color: "transparent",
            fontSize: "32px",
            fontWeight: "bold",
            fontFamily: 'IBM Plex Sans, sans-serif',
          }}
        >
          rhythm
        </Typography>
        <Typography
          sx={{
            color: '#233D4D',
            fontSize: '12px',
          }}
        >
          "Your favorite workout commenter"
        </Typography>
      </Box>

      {/* Google Sign Up */}
      <Button
        onClick={signInWithGoogle} 
        variant="contained" 
        sx={{ 
          width: '70vw',
          backgroundColor: '#FFF',  // Google brand color
          color: '#000',  // Text color
          borderRadius: '2px',  // Google's buttons are usually more square
          textTransform: 'none',  // Google's buttons don't have capitalized letters
          fontFamily: 'Roboto, sans-serif',  // Google's brand font
          fontSize: '14px',
          fontWeight: '500',
          boxShadow: '0 2px 4px 0 rgba(0,0,0,0.25)',  // Google-style box-shadow
          padding: '8px 24px',  // Padding as per Google guidelines
          display: 'flex',
        }}
        startIcon={<img src={`${process.env.PUBLIC_URL}/google_logo.png`} alt='Google Logo' style={{ height: '18px', marginRight: '8px' }}/>}  // Adjust the logo size and margin
      >
        Sign in with Google
      </Button>

      {/* Footer */}
      <Box
        display="flex"
        flexDirection="column"
        justifyContent="center"
        alignItems="center"
        sx={{
          position: 'absolute',
          bottom: '20px',
          color: '#333',
        }}
      >
        <Typography
          sx={{
            fontSize: '12px',
          }}
        >
          Made with ❤️ by the rhythm team
        </Typography>
        <Typography
          sx={{
            fontSize: '12px',
          }}
        >
          © 2023 rhythm
        </Typography>
      </Box>
    </Box>
  )
}

export default Login;