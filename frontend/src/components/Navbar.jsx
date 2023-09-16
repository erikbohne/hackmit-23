import React, { useState } from 'react';
import { AppBar, Typography, Box, IconButton, Menu, MenuItem, Link } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';

const Navbar = () => {
  const [anchorEl, setAnchorEl] = useState(null);

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar position="static">
      <Box 
        sx={{ 
          display: 'flex', 
          justifyContent: 'space-between',  // changed to space-between to place the items at the start and end
          p: 2,
          backgroundColor: '#222',
          borderBottom: '3px solid #F2AA0D',
        }}
      >
        <Typography 
          sx={{
            background: "#FF8200",
            WebkitBackgroundClip: "text",
            color: "transparent",
            fontSize: "24px",
            fontWeight: "bold",
          }}
        >
          rhythm
        </Typography>

        {/* Upload Button */}
        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          sx={{
            background: '#FF8200',
            color: '#FFF',
            borderRadius: '10px',
          }}
        >
          <Typography>
            UPLOAD
          </Typography>
        </Box>

        {/* Hamburger menu */}
        <Box>
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
            <MenuItem onClick={handleMenuClose}>Profile</MenuItem>
            <MenuItem onClick={handleMenuClose}>Settings</MenuItem>
            <MenuItem onClick={handleMenuClose}>Logout</MenuItem>
          </Menu>
        </Box>
      </Box>
    </AppBar>
  );
};

export default Navbar;
