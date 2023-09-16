"""
Program to add comments to the Firestore database
"""
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import uuid  # to generate a unique comment_id

TESTDATA = {
    "comment": "This is a test comment",
    "date": "2023-09-16",
}

def main(db, uid, comment_data):
    """
    Main function to add comments to the database
    """
    # Generate a unique comment_id
    comment_id = str(uuid.uuid4())
    
    # Define the path to the document where the comment should be stored
    comment_ref = db.collection("users").document(uid).collection("comments").document(comment_id)
    
    # Add the comment data to the specified document
    comment_ref.set(comment_data)
    print(f"Comment added with ID: {comment_id}")

if __name__ == "__main__":
    
    # Connect to Firestore
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    
    # You would typically retrieve this UID from an authenticated user session or some other source.
    user_id = "XMS14wGVQ4SpyUpl5lJnBBXwYiq1"
    
    main(db, user_id, TESTDATA)
