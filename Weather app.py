"""
This script fetches weather information from the OpenWeatherMap API
based on user input. It then prints the weather, temperature, humidity,
wind speed and visibility in a readable format.
"""

import requests
from colorama import Fore, Style
from emoji import emojize
from passkey import uber_secret_password

# API key for OpenWeatherMap API
api_key = uber_secret_password

# Get user input for city
user_input = input("Enter a city: ")

# Fetch weather data from API
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# Convert response to JSON
weather_data_json = weather_data.json()

# Check if city was found
if weather_data_json.get('cod') == '404':
    print(Fore.RED + f"No city called {user_input} was found" + Style.RESET_ALL)
else:
    # Set default weather emoji
    weather = emojize(":partly_sunny:")

    # Check if weather data is available
    if 'weather' in weather_data_json and len(weather_data_json['weather']) > 0:
        # Get weather description and map it to emoji
        weather_desc = weather_data_json['weather'][0]['main'].lower()
        emoji_mapping = {
            'clear': emojize("Clear :sun:"),
            'clouds': emojize("Cloudy :cloud:"),
            'rain': emojize("Rain :umbrella:"),
            'thunderstorm': emojize("Thuder storm :thunder_cloud_and_rain:"),
            'drizzle': emojize("Drizzle :cloud_with_rain:"),
            'snow': emojize("Snow :snowflake:"),
            'mist': emojize("Mist :fog:"),
        }
        weather = emoji_mapping.get(weather_desc, emojize(":partly_sunny:"))   

    # Get temperature and convert to Celsius
    temp = round(weather_data.json()['main']['temp'])
    temp_cel = round((temp - 32) * 5/9)

    # Get humidity, wind speed and visibility
    humidity = weather_data_json['main']['humidity']
    wind_speed = weather_data_json['wind']['speed']
    visibility = weather_data_json.get('visibility', 'N/A')

# Print weather information
print(Fore.BLUE + f"The weather in {user_input} is: {weather}" + Style.RESET_ALL)
print(Fore.GREEN + f"The temperature in {user_input} is: {temp_cel}℃" + Style.RESET_ALL)
print(Fore.YELLOW + f"Humidity: {humidity}%" + Style.RESET_ALL)
print(Fore.CYAN + f"Wind Speed: {wind_speed} mph" + Style.RESET_ALL)
print(Fore.MAGENTA + f"Visibility: {visibility} meters" + Style.RESET_ALL)
