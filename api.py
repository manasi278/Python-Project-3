import requests

def get_weather(api_key, location):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for invalid responses
        data = response.json()

        # Extract relevant weather information
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        # Prepare and return the weather information
        return temperature, humidity, description

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None, None, None

def display_weather(location, temperature, humidity, description):
    """Display the weather information in a user-friendly format."""
    if temperature is not None:
        print(f"Weather in {location.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.title()}")
    else:
        print("Could not retrieve weather information.")

def main():
    # Ask for API key and location
    api_key = input("Enter your OpenWeatherMap API key: ").strip()  # Get API key
    location = input("Enter a city name or ZIP code: ").strip()  # Get location

    # Fetch weather data
    temperature, humidity, description = get_weather(api_key, location)

    # Display weather data
    display_weather(location, temperature, humidity, description)

if __name__ == "__main__":
    main()
