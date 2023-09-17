"""
Endpoint for the API - takes a gpx file as input and writes a comment to the firestore database
"""

import flask
from flask_cors import CORS
from gpx_to_df import gpx_to_df
from get_comment_data import get_comment_data
from to_firestore import to_firestore
import sven_terraAPI.terra_methods as terra_methods


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
    
@app.route("/api/v1/get_auth", methods=["GET"])
def get_auth_and_terraid():
    return terra_methods.get_auth_link()
    
    

@app.route("/api/v1/sync", methods=["POST"])
def sync():
    """
    Endpoint for the API - takes uid and updates comments in firestore database
    """
    try:
        # Check if user ID is present
        if 'userId' not in flask.request.form:
            return {"error": "No user ID provided."}, 400
        
        # Get the user id from the request
        uid = flask.request.form["userId"]
        
        # Check if user has null as stravaID
        stravaId = flask.request.form["stravaId"]
        if not stravaId:
            return {"error": "user not authenticated with Strava"}, 400
            
        
        return {"message": "Synced successfully"}, 200

    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"Error occurred: {e}")
        
        # Return a general error message (consider not exposing the actual error in production for security)
        return {"error": "An error occurred while processing the request."}, 500