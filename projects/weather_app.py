import requests

API_KEY = "97c7947b35d728e981e7370cfe7c1d60"   

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raises error if city not found or API fails

        data = response.json()

        # Extract key fields
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        print("\n--- Weather Info ---")
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}\n")

    except requests.exceptions.HTTPError:
        print("❌ City not found or invalid API request.")
    except requests.exceptions.ConnectionError:
        print("❌ Network problem — please check your internet.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

city = input("Enter a city: ")
get_weather(city)
