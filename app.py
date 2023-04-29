"""
Generated with ChatGPT using the prompt:
Design a small Python app that checks the user's 
location and outputs the current temperature, high 
and low temperature for the day, wind speed and direction, 
precipitation, air quality, humidity and air pressure.
"""

# Uses the OpenWeatherMap API
import requests
import json
import config

# Replace with your own API key
API_KEY = config.API_KEY

# Get user's location from IP address
response = requests.get("http://ip-api.com/json")
location_data = json.loads(response.content)

# Get latitude and longitude from location data
lat = location_data["lat"]
lon = location_data["lon"]

# Get weather data for user's location
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
weather_data = json.loads(response.content)

# Check for errors in the API response
if weather_data["cod"] != 200:
    print(f"Error: {weather_data['message']}")
else:
    # Extract relevant weather information
    temperature = round(weather_data["main"]["temp"] * 9/5 - 459.67, 2) # Convert to Fahrenheit
    high_temp = round(weather_data["main"]["temp_max"] * 9/5 - 459.67, 2) # Convert to Fahrenheit
    low_temp = round(weather_data["main"]["temp_min"] * 9/5 - 459.67, 2) # Convert to Fahrenheit
    wind_speed = weather_data["wind"]["speed"]
    wind_direction = weather_data["wind"]["deg"]
    precipitation = weather_data["weather"][0]["description"]
    air_quality = weather_data["main"]["pressure"]
    humidity = weather_data["main"]["humidity"]
    air_pressure = weather_data["main"]["pressure"]

    # Print weather information to user
    print(f"Temperature: {temperature}°F")
    print(f"High temperature: {high_temp}°F")
    print(f"Low temperature: {low_temp}°F")
    print(f"Wind speed: {wind_speed} meters/second")
    print(f"Wind direction: {wind_direction} degrees")
    print(f"Precipitation: {precipitation}")
    print(f"Air quality: {air_quality} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Air pressure: {air_pressure} hPa")

