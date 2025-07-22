import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "aa57516637ad57dbb2b7fb5c48a1aa3e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            city_name = data['name']
            country = data['sys']['country']
            temperature = data['main']['temp']
            condition = data['weather'][0]['description'].title()
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            result_text = (
                f"📍 {city_name}, {country}\n"
                f"🌡️ Temperature: {temperature}°C\n"
                f"🌥️ Condition: {condition}\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind Speed: {wind_speed} m/s"
            )
            result_label.config(text=result_text)

        else:
            result_label.config(text="❌ City not found. Try again.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Something went wrong:\n{e}")

# GUI Setup 
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("350x400")
root.resizable(False, False)
root.config(padx=20, pady=20)

title_label = tk.Label(root, text="🌦️ Weather App", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
city_entry.pack(pady=10)
city_entry.focus()

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify='left')
result_label.pack(pady=20)

root.mainloop()
