import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data['cod'] == 200:
        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        messagebox.showinfo("Weather Information", f"Weather in {city_name}:\nTemperature: {temperature}°C\nDescription: {weather_description}\nHumidity: {humidity}%")
    else:
        messagebox.showerror("Error", "City not found. Please try again.")

def main():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("300x200")
    root.configure(bg="#87CEEB")  # Set background color to sky blue
    
    city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 14), bg="#87CEEB")
    city_label.pack(pady=10)
    
    city_entry = tk.Entry(root, font=("Arial", 14))
    city_entry.pack(pady=5)
    
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    
    def get_weather_info():
        city_name = city_entry.get()
        weather_data = get_weather(city_name, api_key)
        display_weather(weather_data)
    
    get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14, "bold"), command=get_weather_info, bg="#FFFFFF", fg="#000000", relief=tk.GROOVE)
    get_weather_button.pack(pady=10, ipadx=10, ipady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
