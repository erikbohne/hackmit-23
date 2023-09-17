import { Box } from "@mui/material";
import React, { useEffect, useState } from "react";
import Navbar from "../../components/Navbar";
import Comment from "../../components/Comment";
import { getFirestore, collection, getDocs, query } from "firebase/firestore";
import { auth } from "../../Firebase";

const Home = () => {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged(user => {
      if (user) {
        const userId = user.uid;
        fetchComments(userId);
      } else {
        // Handle situation where user is not logged in or session has expired
        setComments([]); // Clear comments
      }
    });

    return () => unsubscribe();  // Cleanup the listener on component unmount
  }, []);

  const fetchComments = async (userId) => {
    const db = getFirestore();
    const q = query(collection(db, "users", userId, "comments"));
    const querySnapshot = await getDocs(q);

    let fetchedComments = [];
    querySnapshot.forEach((doc) => {
      fetchedComments.push({ ...doc.data(), id: doc.id });
    });

    setComments(fetchedComments);
  };

  return (
    <Box
      sx={{
        height: '100vh',
        backgroundColor: '##FFFCFF',
      }}
    >

      {/* Navbar */}
      <Navbar
        userId={auth.currentUser?.uid}
      />
        
      {/* Comments */}
      <Box
        display="flex"
        flexDirection="column"
        justifyContent="center"
        alignItems="center"
        sx={{
          marginTop: '20px',
        }}
      >
        {comments.map(comment => (
          <Comment
            key={comment.id}
            date={comment.date}
            comment={comment.comment}
            title={comment.title}
          />
        ))}
      </Box>

    </Box>
  );
};

export default Home;
