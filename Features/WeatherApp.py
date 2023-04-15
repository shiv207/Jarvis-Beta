import requests
from Body.SpeakUI import streamspeak

def get_weather_data(city):
    # Enter your API key here
    api_key = "43fd515d50f51222fb4cd9f608535c7d"

    # Create the API endpoint URL with the provided city and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Make a request to the API endpoint and retrieve the JSON data
    response = requests.get(url)
    data = response.json()

    # Check if the API request was successful
    if response.status_code != 200:
        # Raise an exception with the error message
        raise Exception(data["message"])

    # Extract the relevant weather data from the JSON data
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    # Return the extracted data as a dictionary
    return {"temperature": temperature, "description": description}

def print_weather_data(data):
    # Format and print the weather data for the user
    streamspeak(f"The weather in Bangalore is {data['temperature']}°C.")
    streamspeak(f"with {data['description']}.")
