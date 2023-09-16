import pandas as pd
import openai
import json
import math

# Haversine distance formula for calculating distance
def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    R = 6371.0  # Earth radius in kilometers
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (math.sin(dlat / 2)**2 + 
         math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# 1. Load the CSV file into a DataFrame
df = pd.read_csv('backend/updated_trackpoints.csv')

# Calculate distance between consecutive points and sum for total distance
df['Distance'] = df.apply(lambda row: haversine_distance(row['Latitude'], row['Longitude'], 
                                                        df.at[row.name - 1, 'Latitude'] if row.name > 0 else row['Latitude'], 
                                                        df.at[row.name - 1, 'Longitude'] if row.name > 0 else row['Longitude']), axis=1)
distance = df['Distance'].sum()
duration = df['Timestamp'].count() * 1  # Assuming each row represents a 1 second interval
avg_speed = distance / (duration / 3600)  # Convert duration to hours
total_elevation_gain = df['Elevation (m)'].diff().where(df['Elevation (m)'].diff() > 0).sum()
total_elevation_loss = -df['Elevation (m)'].diff().where(df['Elevation (m)'].diff() < 0).sum()
avg_heart_rate = df['Heart Rate'].mean()
max_heart_rate = df['Heart Rate'].max()
avg_power = df['Power'].mean()
variability_index = df['Power'].std() / avg_power

# Calculate rolling averages for Power and Heart Rate
df['Rolling Power'] = df['Power'].rolling(window=5).mean()
df['Rolling Heart Rate'] = df['Heart Rate'].rolling(window=5).mean()

# Identify intervals of low power (below 70% of average) as potential struggle points
df['Low Power Interval'] = df['Rolling Power'] < 0.7 * avg_power

# Identify intervals of high heart rate (above 130% of average) as potential intense efforts
df['High Heart Rate Interval'] = df['Rolling Heart Rate'] > 1.3 * avg_heart_rate

# 3. Calculate Intervals, Zones, and Elevation Impact
zones = {'Zone 1': (0, 120), 'Zone 2': (120, 140), 'Zone 3': (140, 185)}
zone_times = {}
for zone, (min_hr, max_hr) in zones.items():
    time_in_zone = df[(df['Heart Rate'] >= min_hr) & (df['Heart Rate'] < max_hr)]['Heart Rate'].count()
    zone_times[zone] = time_in_zone

power_zones = {'Low': (0, 100), 'Medium': (100, 250), 'High': (250, 400)}
power_zone_times = {}
for zone, (min_power, max_power) in power_zones.items():
    time_in_zone = df[(df['Power'] >= min_power) & (df['Power'] < max_power)]['Power'].count()
    power_zone_times[zone] = time_in_zone

# 4. Extract summary details
struggle_intervals = df[df['Low Power Interval']]
intense_intervals = df[df['High Heart Rate Interval']]

num_struggle_intervals = len(struggle_intervals)
avg_struggle_elevation = struggle_intervals['Elevation (m)'].mean()

num_intense_intervals = len(intense_intervals)
avg_intense_elevation = intense_intervals['Elevation (m)'].mean()

# 5. Use OpenAI API to get insights
with open('backend/config.json', 'r') as file:
    config = json.load(file)
    openai.api_key = config["OPENAI_API_KEY"]

prompt_text = f"""
The runner covered a distance of {distance:.2f} km in a duration of {duration//3600} hours {duration%3600//60} minutes.
Their average speed was {avg_speed:.2f} km/h with an elevation gain of {total_elevation_gain:.2f} meters and a loss of {total_elevation_loss:.2f} meters.
The average heart rate was {avg_heart_rate:.2f} bpm with a max of {max_heart_rate} bpm. The average power exerted was {avg_power:.2f} watts with a variability index of {variability_index:.2f}.
They spent {zone_times['Zone 1']} seconds in Zone 1, {zone_times['Zone 2']} seconds in Zone 2, and {zone_times['Zone 3']} seconds in Zone 3, with this as the key: 'Low': (0, 100), 'Medium': (100, 250), 'High': (250, 1000)
Given these metrics, identify areas that might require improvement and provide personalized, clear, and actionable insights and recommendations. Ensure the advice is easily understandable for anyone of all ages. Be specific, concise, positive, encouraging, honest, respectful, and professional.
Try not to use all the metrics given, just use the ones that would help the user. Make it as user-friendly as possible.
"""

response = openai.Completion.create(engine="text-davinci-003", prompt=prompt_text, max_tokens=500)
insights = response.choices[0].text.strip()

print(insights)
