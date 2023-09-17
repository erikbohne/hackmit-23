"""
Endpoint for the API - takes a gpx file as input and writes a comment to the firestore database
"""

import flask
from flask_cors import CORS
from gpx_to_df import gpx_to_df
from get_comment_data import get_comment_data
from to_firestore import to_firestore

# init flask app
app = flask.Flask(__name__)

# enable CORS
CORS(app)

@app.route("/api/v1/add_comment", methods=["POST"])
def add_comment():
    """
    Endpoint for the API - takes a gpx file as input and writes a comment to the firestore database
    """
    try:
        # Check if gpx_file is present
        if 'gpxFile' not in flask.request.files:
            return {"error": "No gpx_file provided."}, 400
        
        # Get the gpx file from the request
        gpx_file = flask.request.files["gpxFile"]
        
        # Check if user ID is present
        if 'userId' not in flask.request.form:
            return {"error": "No user ID provided."}, 400
        
        # Get the user id from the request
        uid = flask.request.form["userId"]
        
        # Get title and date from gpX file
        title = gpx_file.filename
        title = title[:len(title)-4]
        title = title.replace("_", " ")
        
        # Convert the gpx file to a dictionary
        gpx_dict, date = gpx_to_df(gpx_file)
        
        # Get the comment data from the gpx file
        comment_data = get_comment_data(gpx_dict)
        
        # Add the comment to the database
        to_firestore(uid, comment_data, title, date)
        
        return {"message": "Comment added successfully"}, 200

    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"Error occurred: {e}")
        
        # Return a general error message (consider not exposing the actual error in production for security)
        return {"error": "An error occurred while processing the request."}, 500
