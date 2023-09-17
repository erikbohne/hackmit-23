"""
Program to add comments to the Firestore database
"""
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import uuid  # to generate a unique comment_id

def initialize_firebase():
    """
    Initialize Firebase Admin SDK
    """
    if not firebase_admin._apps:
        cred = credentials.Certificate("service_account.json")
        firebase_admin.initialize_app(cred)

def to_firestore(uid, comment_data, title, date):
    """
    Main function to add comments to the database
    """
    # Ensure Firebase Admin SDK is initialized
    initialize_firebase()
    db = firestore.client()
    
    # Generate a unique comment_id
    comment_id = str(uuid.uuid4())
    
    # Define the path to the document where the comment should be stored
    comment_ref = db.collection("users").document(uid).collection("comments").document(comment_id)
    
    COMMENT = {
        "date": date,
        "comment": comment_data,
        "title": title,
    }
    
    # Add the comment data to the specified document
    comment_ref.set(COMMENT)
    
    return 200
