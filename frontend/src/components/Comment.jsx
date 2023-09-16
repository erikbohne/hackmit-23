import React from "react";
import { motion } from "framer-motion";
import { Box, Typography } from "@mui/material";

const Comment = ({ date, comment }) => {

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
        justifyContent="center"
        alignItems="center"
        sx={{
          width: "70vw",
          margin: '10px auto',
          padding: '10px',
          borderRadius: '10px',
          background: "linear-gradient(to right, #F2AA0D, #FF8200)",
          boxShadow: '0 5px 5px 0 rgba(0,0,0,.75)',
        }}
      >
        <Typography>
          {date}
        </Typography>
        <Typography
          sx={{
            textAlign: 'center',
            fontSize: '12px',
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
