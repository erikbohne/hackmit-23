import react from 'react';
import { AppBar, Typography, Box } from '@mui/material';

const Navbar = () => {
  return (
    <AppBar position="static">
      <Box 
        sx={{ 
          display: 'flex', 
          justifyContent: 'center', 
          p: 2,
          backgroundColor: '#222',  // Dark grey background for the AppBar
          borderBottom: '3px solid #F2AA0D',  // Adding a bottom border for a touch of contrast
        }}
        >
        <Typography 
          sx={{
            background: "linear-gradient(to left, #F2AA0D, #FF8200)",
            WebkitBackgroundClip: "text",
            color: "transparent",
            fontSize: "32px",
            fontWeight: "bold",
          }}
        >
          RHYTHM AI
        </Typography>
      </Box>
    </AppBar>
  );
};

export default Navbar;
