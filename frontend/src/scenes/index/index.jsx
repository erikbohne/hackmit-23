import { Box } from "@mui/material";
import React, { useEffect, useState } from "react";
import Navbar from "../../components/Navbar";
import Comment from "../../components/Comment";
import { collection, getDocs, getDoc, doc, query } from "firebase/firestore";
import { auth, db } from "../../Firebase";

const Home = () => {
  const [comments, setComments] = useState([]);
  const [userId, setUserId] = useState(null);  // <-- Initialize the userId state
  const [terraId, setTerraId] = useState(null);  // <-- Initialize the terraId state

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged(user => {
      if (user) {
        const uid = user.uid;
        
        setUserId(uid);  // <-- Set the userId when user logs in
        fetchComments(uid);
        fetchTerraId(uid);
      } else {
        // Handle situation where user is not logged in or session has expired
        setUserId(null);  // Clear userId
        setComments([]);  // Clear comments
      }
    });

    return () => unsubscribe();  // Cleanup the listener on component unmount
  }, []);

  const fetchComments = async (uid) => {
    const q = query(collection(db, "users", uid, "comments"));
    const querySnapshot = await getDocs(q);

    let fetchedComments = [];
    querySnapshot.forEach((doc) => {
      fetchedComments.push({ ...doc.data(), id: doc.id });
    });

    setComments(fetchedComments);
  };

  const fetchTerraId = async (uid) => {
    // Reference to the user's document directly
    const userDocRef = doc(db, "users", uid);

    const userDoc = await getDoc(userDocRef);

    if (userDoc.exists()) {
        const terraId = userDoc.data().terraId;

        setTerraId(terraId); // This assumes terraId is a single value and not an array.
    } else {
        console.warn(`Document for UID ${uid} does not exist`);
    }
  }

  return (
    <Box
      sx={{
        minHeight: '100vh',
        backgroundColor: '##FFFCFF',
      }}
    >

      {console.log(typeof terraId, terraId)}
      {/* Navbar */}
      <Navbar 
        userId={userId} 
        terraId={terraId}
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
        {comments.sort((a, b) => new Date(b.date) - new Date(a.date)).map(comment => (
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
