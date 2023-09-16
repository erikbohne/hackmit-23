import {Box} from '@mui/material';
import {signInWithPopup, GoogleAuthProvider} from 'firebase/auth';
import {getFirestore, setDoc, doc} from 'firebase/firestore';
import {auth} from '../../Firebase';

const Login = () => {

  const signInWithGoogle = async () => {
    try {
        const provider = new GoogleAuthProvider();
        const result = await signInWithPopup(auth, provider);
        
        // The signed-in user info.
        const user = result.user;
  
        // Create a user in your Firestore database
        const db = getFirestore();
        await setDoc(doc(db, "users", user.uid), {
            username: user.displayName,
            email: user.email,
            createdAt: new Date(),
        });
  
        // You can add navigation logic here if needed
        navigate('/');
    } catch (error) {
        // Handle Errors here.
        console.error(error);
        setError(error.message);
    }
  };

  return (
    <Box>
      {/* Google Sign Up */}
      <CustomSignUp 
        onClick={signInWithGoogle} 
        variant="contained" 
        sx={{ 
          mt: 2, 
          mb: 1, 
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
          alignItems: 'center'
        }}
        startIcon={<img src={`${process.env.PUBLIC_URL}/google_logo.png`} alt='Google Logo' style={{ height: '18px', marginRight: '8px' }}/>}  // Adjust the logo size and margin
      >
        Sign up with Google
      </CustomSignUp>
    </Box>
  )
}

export default Login;