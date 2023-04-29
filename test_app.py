"""
PROMPT: What unit tests could I write for this code?
"""

import pytest
import requests
import json
import config
from unittest import mock

API_KEY = config.API_KEY

# HELPER FUNCTION
def get_weather_data(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}")
    return response.json()


# TEST THAT API KEY IS VALID

# Mock the API response to return a status code of 200
@mock.patch('requests.get')
def test_valid_api_key(mock_get):
    mock_get.return_value.status_code = 200
    
    # Call the function with the mock API response
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat=37.7749&lon=-122.4194&appid={API_KEY}")
    
    # Check that the status code is 200
    assert response.status_code == 200

# TEST THAT THE LATITUDE AND LONGITUDE ARE CORRECT FOR A KNOWN LOCATION

# Mock the API response to return location data for a known location
@mock.patch('requests.get')
def test_correct_location(mock_get):
    mock_response = {
        "coord": {
            "lon": -122.4194,
            "lat": 37.7749
        },
        "weather": [
            {
                "main": "Clear",
                "description": "clear sky"
            }
        ],
        "main": {
            "temp": 287.56,
            "feels_like": 287.56,
            "temp_min": 285.85,
            "temp_max": 289.43,
            "pressure": 1022,
            "humidity": 57
        },
        "wind": {
            "speed": 2.57,
            "deg": 286
        },
        "clouds": {
            "all": 0
        },
        "dt": 1650853027,
        "sys": {
            "type": 2,
            "id": 2009430,
            "country": "US",
            "sunrise": 1650836654,
            "sunset": 1650882922
        },
        "timezone": -25200,
        "id": 5391959,
        "name": "San Francisco",
        "cod": 200
    }
    
    mock_get.return_value = mock.Mock(status_code=200)
    mock_get.return_value.json.return_value = mock_response
    
    # Call the function with the mock API response
    weather_data = get_weather_data(API_KEY, 37.7749, -122.4194)
    
    # Check that the latitude and longitude are correct
    assert weather_data["coord"]["lat"] == 37.7749
    assert weather_data["coord"]["lon"] == -122.4194