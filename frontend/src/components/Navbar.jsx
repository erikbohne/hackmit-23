import React, { useState, useRef } from 'react';
import { AppBar, Typography, Box, IconButton, Menu, MenuItem, Button } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';

const Navbar = ( userId ) => {
  const [anchorEl, setAnchorEl] = useState(null);
  const fileInput = useRef(null); // using useRef to reference the file input

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleSyncWithStrava = () => {
    // TODO: Add Strava API call here
    alert('Syncing with Strava!');
  };

  const handleLogout = () => {
    localStorage.removeItem('userToken');
    window.location.href = "/";
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData = new FormData();
      formData.append('gpxFile', file);
      formData.append('userId', userId.userId); 

      console.log(userId)

      try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/add_comment', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          console.error('Server responded with', response.status);
          const text = await response.text();
          console.error('Response body:', text);
          return;
        }

        const result = await response.json();
        console.log(result); // Handle the backend response accordingly.

      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }
  };

  return (
    <AppBar position="static">
      <Box 
        sx={{ 
          display: 'flex', 
          justifyContent: 'space-between',
          p: 0.5,
          backgroundColor: '#222',
          borderBottom: '3px solid #F2AA0D',
        }}
      >
        <Typography 
          sx={{
            background: "#FF8200",
            margin: "0 0.5em",
            WebkitBackgroundClip: "text",
            color: "transparent",
            fontSize: "24px",
            fontWeight: "bold",
            fontFamily: 'IBM Plex Sans, sans-serif',
          }}
        >
          rhythm
        </Typography>

        <Box display="flex" alignItems="center">
          {/* Hidden File Input */}
          <input
            type="file"
            accept=".gpx"
            style={{ display: 'none' }}
            ref={fileInput}
            onChange={handleFileUpload}
          />

          {/* Upload Button */}
          <Button
            variant="contained"
            sx={{
              background: "linear-gradient(to right, #F2AA0D, #FF8200)",
              color: '#fff',
              borderRadius: '10em',
              padding: '0.25em 1em',
              marginRight: '1.5em',
              fontSize: '10px',
              fontWeight: 'bold',
              fontFamily: 'IBM Plex Mono, monospace',
              letterSpacing: '2px'
            }}
            onClick={() => fileInput.current.click()}
          >
            UPLOAD
          </Button>


          {/* Hamburger menu */}
          <IconButton 
            edge="start" 
            color="inherit" 
            aria-label="menu"
            onClick={handleMenuOpen}
          >
            <MenuIcon 
              sx={{ 
                fontSize: '24px',
                color: '#fff',
              }}
            />
          </IconButton>
          <Menu
            anchorEl={anchorEl}
            keepMounted
            open={Boolean(anchorEl)}
            onClose={handleMenuClose}
          >
            <MenuItem onClick={handleSyncWithStrava}>Sync Strava</MenuItem>
            <MenuItem onClick={handleLogout}>Logout</MenuItem>
          </Menu>
        </Box>
      </Box>
    </AppBar>
  );
};

export default Navbar;
