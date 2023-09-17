"""
Endpoint for the API - takes a gpx file as input and writes a comment to the firestore database
"""

import flask
from gpx_to_df import gpx_to_df
from get_comment_data import get_comment_data
from to_firestore import to_firestore

# init flask app
app = flask.Flask(__name__)


@app.route("/api/v1/add_comment", methods=["POST"])
def add_comment():
    """
    Endpoint for the API - takes a gpx file as input and writes a comment to the firestore database
    """
    # Get the gpx file from the request
    gpx_file = flask.request.files["gpx_file"]
    
    # Get the user id from the request
    uid = flask.request.form["uid"]
    
    # Convert the gpx file to a dictionary
    gpx_dict = gpx_to_df(gpx_file)
    
    # Get the comment data from the gpx file
    comment_data = get_comment_data(gpx_dict)
    
    # Add the comment to the database
    to_firestore(uid, comment_data)
    
    return "Comment added successfully", 200