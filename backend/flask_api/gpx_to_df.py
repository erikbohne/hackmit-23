"""
Processes GPX file and returns a CSV file
"""

import xml.etree.ElementTree as ET
import pandas as pd

def gpx_to_df(gpx_file):
    """
    Processes GPX file and returns a CSV file
    """
    # Parse the GPX file
    tree = ET.parse(gpx_file)
    root = tree.getroot()

    # Define namespaces
    namespace = {
        'gpx': 'http://www.topografix.com/GPX/1/1',
        'gpxtpx': 'http://www.garmin.com/xmlschemas/TrackPointExtension/v1'
    }
    
    # Extract starting time 
    date = root.find(".//gpx:metadata/gpx:time", namespace)
    date = date.text if date is not None else None

    # Extract track points with heart rate and power
    trackpoints = []
    for trkpt in root.findall(".//gpx:trkpt", namespace):
        lat = trkpt.attrib['lat']
        lon = trkpt.attrib['lon']
        ele = trkpt.find('gpx:ele', namespace)
        elevation = ele.text if ele is not None else None
        time = trkpt.find('gpx:time', namespace)
        timestamp = time.text if time is not None else None
        
        hr = trkpt.find(".//gpxtpx:hr", namespace)
        heart_rate = hr.text if hr is not None else None
        
        power = trkpt.find(".//gpx:power", namespace)
        power_value = power.text if power is not None else None
        
        trackpoints.append((lat, lon, elevation, timestamp, heart_rate, power_value))

    # Return the data as pandas dataframe
    df = pd.DataFrame(trackpoints, columns=['Latitude', 'Longitude', 'Elevation (m)', 'timestamp', 'Heart Rate', 'Power'])
    return df, date
