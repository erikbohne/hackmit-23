import React from "react";
import { motion } from "framer-motion";
import { Box, Typography } from "@mui/material";

const Comment = ({ title, comment, date }) => {

  const jsDate = new Date(date);

  const fadeInFromBelow = {
    initial: { opacity: 0, y: 50 },
    animate: { opacity: 1, y: 0 },
    exit: { opacity: 0, y: -50 }
  };

  return (
    <motion.div
      initial={fadeInFromBelow.initial}
      animate={fadeInFromBelow.animate}
      exit={fadeInFromBelow.exit}
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.9 }}
    >
      <Box
        display="flex"
        flexDirection="column"
        alignItems="flex-start"
        sx={{
          width: "70vw",
          minHeight: "100px",
          overflowY: "auto",
          margin: '10px auto',
          padding: '10px',
          borderRadius: '10px',
          background: "linear-gradient(to right, #F2AA0D, #FF8200)",
          boxShadow: '0 2px 4px 0 rgba(0,0,0,0.25)',
        }}
      >

        {/* Title and Date Container */}
        <Box
          mb={1}
          display="flex"
          flexDirection="row"
          justifyContent="space-between"
          alignItems="center" // Ensures vertical alignment
          width="100%" // Ensures the Box takes full available width
        >
          {/* Title */}
          <Typography
            sx={{
              textAlign: 'left',
              fontSize: '12px',
              fontWeight: 'bold',
              color: '#233D4D',
              flexGrow: 1, // This will make sure the title grows and takes up as much space as it can, pushing the date to the right
            }}
          >
            {title}
          </Typography>

          {/* Date */}
          <Typography
            sx={{
              fontSize: '12px',
              color: '#EEE',
              marginLeft: 'auto', // This will push the date to the right
            }}
          >
            {jsDate.toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'long' })}
          </Typography>
        </Box>
        
        {/* Comment on session */}
        <Typography
          sx={{
            textAlign: 'center',
            fontSize: '10px',
            color: '#EEE',
          }}
        >
          {comment}
        </Typography>
      </Box>
    </motion.div>
  );
}

export default Comment;
