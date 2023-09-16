import React from "react";
import { motion } from "framer-motion";
import { Box, Typography } from "@mui/material";

const Comment = ({ date, comment }) => {
  return (
    <motion.div
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
          background: '#F2AA0D',
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
