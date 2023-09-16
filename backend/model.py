import pandas as pd
import openai

# 1. Load the CSV file into a DataFrame
df = pd.read_csv('backend/updated_trackpoints.csv')

# 2. Generate necessary columns based on rolling averages
# Calculate rolling averages for Power and Heart Rate to smooth out the data
df['Rolling Power'] = df['Power'].rolling(window=5).mean()
df['Rolling Heart Rate'] = df['Heart Rate'].rolling(window=5).mean()

# Identify intervals of low power (below 70% of average) as potential struggle points
avg_power = df['Power'].mean()
df['Low Power Interval'] = df['Rolling Power'] < 0.7 * avg_power

# Identify intervals of high heart rate (above 130% of average) as potential intense efforts
avg_heart_rate = df['Heart Rate'].mean()
df['High Heart Rate Interval'] = df['Rolling Heart Rate'] > 1.3 * avg_heart_rate

# 3. Extract summary details based on the generated columns
struggle_intervals = df[df['Low Power Interval']]
intense_intervals = df[df['High Heart Rate Interval']]

num_struggle_intervals = len(struggle_intervals)
avg_struggle_elevation = struggle_intervals['Elevation (m)'].mean()

num_intense_intervals = len(intense_intervals)
avg_intense_elevation = intense_intervals['Elevation (m)'].mean()

summary = {
    'Number of Struggle Intervals': num_struggle_intervals,
    'Average Elevation during Struggles': avg_struggle_elevation,
    'Number of Intense Effort Intervals': num_intense_intervals,
    'Average Elevation during Intense Efforts': avg_intense_elevation
}

openai.api_key = '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'
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=f"The runner had {num_struggle_intervals} struggle intervals at an average elevation of {avg_struggle_elevation} meters. They had {num_intense_intervals} intense effort intervals at an average elevation of {avg_intense_elevation} meters. Provide insights and recommendations.",
  max_tokens=200
)
insights = response.choices[0].text.strip()

print(insights)
