import requests
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

API_KEY = "97c7947b35d728e981e7370cfe7c1d60"
FILENAME = "weather_history.csv"


def log_weather_data(city, temperature, feels_like, description):
    try:
        with open(FILENAME, "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(FILENAME, "a", newline="") as file:
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


def get_weather(city, text_widget):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", "City not found.")
            return

        city_name = data["name"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].title()

        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END,
            f"City: {city_name}\n"
            f"Weather: {description}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels Like: {feels_like}°C\n"
        )

        log_weather_data(city_name, temperature, feels_like, description)

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "Internet connection error.")


def open_history_window():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
    except FileNotFoundError:
        messagebox.showinfo("History", "No history found.")
        return

    win = tk.Toplevel()
    win.title("Weather History")

    tree = ttk.Treeview(win, columns=(1,2,3,4,5), show="headings", height=20)
    headers = ["City", "Temp", "Feels Like", "Description", "Time"]

    for i, h in enumerate(headers, start=1):
        tree.heading(i, text=h)
        tree.column(i, width=150)

    for row in rows[1:]:
        tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True)

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

output_box = tk.Text(root, height=8, width=40)
output_box.pack(pady=10)

search_button = tk.Button(
    root,
    text="Get Weather",
    command=lambda: get_weather(city_entry.get(), output_box)
)
search_button.pack(pady=5)

history_button = tk.Button(
    root,
    text="View History",
    command=open_history_window
)
history_button.pack()

root.mainloop()
