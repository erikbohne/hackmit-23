import React, { useState, useRef } from 'react';
import { AppBar, Typography, Box, IconButton, Menu, MenuItem, Button } from '@mui/material';
import { db } from '../Firebase';
import { doc, setDoc } from 'firebase/firestore';
import MenuIcon from '@mui/icons-material/Menu';

const Navbar = ( {userId, terraId} ) => {
  const [anchorEl, setAnchorEl] = useState(null);
  const fileInput = useRef(null); // using useRef to reference the file input

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData69 = new FormData();
      formData69.append('gpxFile', file);
      formData69.append('userId', userId);
      console.log(formData69);

      try {
        const response = await fetch('https://vishruthb--app-py-create-app-dev.modal.run/api/v1/add_comment', {
          method: 'POST',
          body: formData69,
        });

        if (!response.ok) {
          console.error('Server responded with', response.status);
          const text = await response.text();
          console.error('Response body:', text);
          return;
        }

        const result = await response.json();
        console.log(result); // Handle the backend response accordingly.
        window.location.reload(); // Reload the page to see the new comment.

      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }
  };

  const handleConnectStrava = async () => { // Make sure to mark the function as async if using await inside
    if (terraId === "empty") {
        console.log("terraId is empty");

        const formData = new FormData();
        formData.append('userId', userId.userId);
        
        const response = await fetch('https://vishruthb--app-py-create-app-dev.modal.run/api/v1/get_auth', {
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

        // add result.terraId to the user's document in firestore users/{userId}/terraId
        const new_terraId = result.terraId;
        const userDocRef = doc(db, "users", userId);
        await setDoc(userDocRef, {
            terraId: new_terraId,
        }, { merge: true });

        // go to the strava auth page received from the result.auth_url
        if (result.auth_url) {
          window.open(result.auth_url, '_blank');
      }

      window.location.reload(); // Reload the page.

    } else {
      // alert alearady connected
      alert("Already connected to Strava!");
    }
  };

  const handleSyncStrava = async () => {
    const formData = new FormData();
      formData.append('userId', userId.userId);
      formData.append('terraId', terraId);

      const response = await fetch('https://vishruthb--app-py-create-app-dev.modal.run/api/v1/sync', {
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
      window.location.reload(); // Reload the page to see the new comment.
  };

  const handleLogout = () => {
    localStorage.removeItem('userToken');
    window.location.href = "/";
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
            <MenuItem onClick={handleConnectStrava}>Connect Strava</MenuItem>
            <MenuItem onClick={handleSyncStrava}>Sync Strava</MenuItem>
            <MenuItem onClick={handleLogout}>Logout</MenuItem>
          </Menu>
        </Box>
      </Box>
    </AppBar>
  );
};

export default Navbar;
