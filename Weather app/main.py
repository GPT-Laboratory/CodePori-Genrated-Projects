import requests
import tkinter as tk
from tkinter import messagebox
import geocoder

# Constants
API_KEY = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API Key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_location():
    """Get the user's current location using geocoder."""
    g = geocoder.ip('me')  # Get location based on IP
    return g.city

def get_weather_data(city):
    """Fetch weather data from OpenWeatherMap API."""
    try:
        complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
        response = requests.get(complete_url)
        weather_data = response.json()

        if weather_data["cod"] != "404":
            main_data = weather_data["main"]
            wind_data = weather_data["wind"]
            weather_desc = weather_data["weather"][0]["description"]
            temp = main_data["temp"]
            humidity = main_data["humidity"]
            wind_speed = wind_data["speed"]

            return {
                "temperature": temp,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "description": weather_desc.capitalize(),
                "city": weather_data["name"]
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather():
    """Update weather information in the GUI."""
    city = city_entry.get() or get_location()

    if not city:
        messagebox.showerror("Error", "Unable to determine your location. Please enter a city.")
        return

    weather = get_weather_data(city)

    if weather:
        weather_label.config(text=f"City: {weather['city']}\n"
                                  f"Temperature: {weather['temperature']}°C\n"
                                  f"Humidity: {weather['humidity']}%\n"
                                  f"Wind Speed: {weather['wind_speed']} m/s\n"
                                  f"Condition: {weather['description']}")
    else:
        messagebox.showerror("Error", "City not found or unable to fetch weather data.")

# GUI Setup
app = tk.Tk()
app.title("Real-Time Weather App")
app.geometry("400x400")

# Label
heading_label = tk.Label(app, text="Weather App", font=("Helvetica", 16))
heading_label.pack(pady=10)

# City Entry Field
city_label = tk.Label(app, text="Enter city (or leave blank for current location):")
city_label.pack(pady=5)

city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=5)

# Button
weather_button = tk.Button(app, text="Get Weather", command=display_weather)
weather_button.pack(pady=10)

# Weather Display
weather_label = tk.Label(app, font=("Helvetica", 12), justify="left")
weather_label.pack(pady=20)

# Run the App
app.mainloop()
