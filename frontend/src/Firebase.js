// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBdpb8IQZKYWXg1BzujZWhxVmaHNiPpFsQ",
  authDomain: "hackmit23.firebaseapp.com",
  projectId: "hackmit23",
  storageBucket: "hackmit23.appspot.com",
  messagingSenderId: "99644001188",
  appId: "1:99644001188:web:697a4da58fd0fb720acf31"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);

// Get the Firebase Auth instance
const auth = getAuth(app);

export { auth };