import requests
import csv
from datetime import datetime


# Log Weather History

def log_weather_data(city, temperature, feels_like, description):
    filename = 'weather_history.csv'

    try:
        with open(filename, "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(filename, 'a', newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["City", "Temperature (C)", "Feels Like (C)", "Description", "Time"])

        writer.writerow([
            city,
            temperature,
            feels_like,
            description,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])


# View Weather History + Filters

def view_weather_history():
    filename = "weather_history.csv"

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print("\nNo history found yet.\n")
        return

    if len(data) <= 1:
        print("\nHistory file is empty.\n")
        return

    header = data[0]
    rows = data[1:]

    print("\n=== Weather History Filter ===")
    print("1. View all records")
    print("2. Filter by city")
    print("3. Filter by date (YYYY-MM-DD)")
    print("4. Filter by temperature")
    choice = input("Choose an option: ")


    if choice == "1":
        print("\n--- All Weather Records ---")
        for row in rows:
            print(row)
        print()
        return

    elif choice == "2":
        city = input("Enter city name: ").strip().lower()
        filtered = [row for row in rows if row[0].lower() == city]

        if not filtered:
            print("\nNo matching records.\n")
        else:
            print("\n--- Filtered by City ---")
            for row in filtered:
                print(row)
        print()
        return

    elif choice == "3":
        date = input("Enter date (YYYY-MM-DD): ").strip()
        filtered = [row for row in rows if row[-1].startswith(date)]

        if not filtered:
            print("\nNo matching records.\n")
        else:
            print("\n--- Filtered by Date ---")
            for row in filtered:
                print(row)
        print()
        return
    
    elif choice == "4": # Filter by temperature
        try:
            threshold = float(input("Enter temperature value (°C): "))
        except ValueError:
            print("\nInvalid number.\n")
            return
        
        print("\nChoose filter type:")
        print("1. Greater than")
        print("2. Less than")
        print("3. Equal to")

        filter_type = input("Enter option: ")

        if filter_type == "1":
            filtered = [row for row in rows if float(row[1]) > threshold]
        elif filter_type == "2":
            filtered = [row for row in rows if float(row[1]) < threshold]
        elif filter_type == "3":
            filtered = [row for row in rows if float(row[1]) == threshold]
        else:
            print("\nInvalid option.\n")
            return

        if not filtered:
            print("\nNo matching records.\n")
        else:
            print("\n--- Filtered by Temperature ---")
            for row in filtered:
                print(row)
        print()
        return

    else:
        print("\nInvalid option.\n")

# Weather API Request
API_KEY = "97c7947b35d728e981e7370cfe7c1d60"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print("City not found. Try again.\n")
            return

        city_name = data["name"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        description = data["weather"][0]["description"].title()

        print("\n====== Weather Info ======")
        print(f"City: {city_name}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Min: {temp_min}°C | Max: {temp_max}°C")
        print("==========================\n")

        log_weather_data(city_name, temperature, feels_like, description)

    except requests.exceptions.ConnectionError:
        print("Internet connection error. Please check your network.\n")


# Main Loop

while True:
    city = input("Enter a city name (or type 'history' or 'exit'): ")

    if city.lower() == 'exit':
        break

    if city.lower() == "history":
        view_weather_history()
        continue

    get_weather(city)
