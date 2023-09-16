import gpxpy
import csv

def gpx_to_csv(gpx_file, csv_file):
    # Parse the GPX file
    with open(gpx_file, 'r') as f:
        gpx = gpxpy.parse(f)

    data = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                print("Extensions:", point.extensions)

gpx_to_csv("backend/L_petur_til_Dairy_Queen.gpx", "clean.csv")
