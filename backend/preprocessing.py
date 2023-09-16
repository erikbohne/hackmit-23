import xml.etree.ElementTree as ET
import csv

# Parse the GPX file
tree = ET.parse('backend/3')
root = tree.getroot()

# Define namespaces
namespace = {
    'gpx': 'http://www.topografix.com/GPX/1/1',
    'gpxtpx': 'http://www.garmin.com/xmlschemas/TrackPointExtension/v1'
}

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

# Write the trackpoints to a CSV file
csv_filepath = 'backend/updated_trackpoints.csv'
with open(csv_filepath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Latitude', 'Longitude', 'Elevation (m)', 'Timestamp', 'Heart Rate', 'Power'])
    csvwriter.writerows(trackpoints)
