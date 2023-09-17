"""
Program to add comments to the Firestore database
"""
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import uuid  # to generate a unique comment_id

def to_firestore(db, uid, comment_data):
    """
    Main function to add comments to the database
    """
    # Connect to Firestore
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    
    # Generate a unique comment_id
    comment_id = str(uuid.uuid4())
    
    # Define the path to the document where the comment should be stored
    comment_ref = db.collection("users").document(uid).collection("comments").document(comment_id)
    
    # Add the comment data to the specified document
    comment_ref.set(comment_data)
    
    return 200
