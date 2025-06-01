# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 21:54:07 2025

@author: ADMIN
"""
#1/6/25
#API Integration and Data Visualization

import requests
import matplotlib.pyplot as plt

# Replace with your actual OpenWeatherMap API key
API_KEY = 'your_actual_api_key'
CITY = 'Chennai'

# Construct the API URL
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    dates = []
    temps = []

    # Extract temperature and date-time from the forecast data
    for entry in data['list']:
        dates.append(entry['dt_txt'])
        temps.append(entry['main']['temp'])

    # Plotting the data
    plt.figure(figsize=(12, 6))
    plt.plot(dates[:10], temps[:10], marker='o', color='teal')  # Only show first 10 entries
    plt.xticks(rotation=45)
    plt.title(f'Temperature Forecast for {CITY}')
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
    print("Response:", response.text)
