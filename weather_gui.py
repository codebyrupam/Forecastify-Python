import requests
import customtkinter as ctk
from datetime import datetime
from PIL import Image, ImageTk
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ==============================
# API CONFIG
# ==============================
API_KEY = "c9fd221e9c9b15b3b5dc2a987537f06e"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

# ==============================
# APP CLASS
# ==============================
class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌤 Modern Weather Forecast App")
        self.geometry("900x650")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Weather Forecast", font=("Arial Black", 28, "bold"), text_color="cyan")
        self.title_label.pack(pady=15)

        # Search Frame
        self.search_frame = ctk.CTkFrame(self)
        self.search_frame.pack(pady=10)

        self.city_entry = ctk.CTkEntry(self.search_frame, width=250, height=35, placeholder_text="Enter city name...")
        self.city_entry.grid(row=0, column=0, padx=10)

        self.search_btn = ctk.CTkButton(self.search_frame, text="Search", command=self.show_weather)
        self.search_btn.grid(row=0, column=1, padx=10)

        # Current Weather Card
        self.weather_frame = ctk.CTkFrame(self, corner_radius=15)
        self.weather_frame.pack(pady=15, fill="x", padx=20)

        self.weather_label = ctk.CTkLabel(self.weather_frame, text="🌎 Search for a city to see weather", font=("Arial", 16))
        self.weather_label.pack(pady=20)

        # Forecast Frame
        self.forecast_frame = ctk.CTkFrame(self, corner_radius=15)
        self.forecast_frame.pack(pady=15, fill="both", expand=True, padx=20)

    # ==============================
    # GET CURRENT WEATHER
    # ==============================
    def get_weather(self, city):
        url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        return response.json()

    # ==============================
    # GET 7-DAY FORECAST
    # ==============================
    def get_forecast(self, lat, lon):
        url = f"{BASE_URL}onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric"
        response = requests.get(url)
        return response.json()

    # ==============================
    # SHOW WEATHER DATA
    # ==============================
    def show_weather(self):
        city = self.city_entry.get()
        if not city:
            self.weather_label.configure(text="⚠️ Please enter a city name")
            return

        data = self.get_weather(city)
        if data.get("cod") != 200:
            self.weather_label.configure(text="❌ City not found")
            return

        # Current Weather Data
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        self.weather_label.configure(
            text=f"📍 {city_name}, {country}\n🌡 Temp: {temp}°C\n☁ Condition: {condition}\n💧 Humidity: {humidity}%\n🌬 Wind: {wind} m/s",
            font=("Arial", 16),
        )

        coords = data["coord"]
        forecast_data = self.get_forecast(coords["lat"], coords["lon"])
        self.show_forecast(forecast_data)

    # ==============================
    # SHOW 7-DAY FORECAST
    # ==============================
    def show_forecast(self, forecast_data):
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()

        # Frame for Forecast Cards
        cards_frame = ctk.CTkFrame(self.forecast_frame)
        cards_frame.pack(side="top", pady=10)

        temps = []
        days = []

        for i, day in enumerate(forecast_data["daily"][:7]):
            date = datetime.fromtimestamp(day["dt"]).strftime("%a %d %b")
            temp_day = day["temp"]["day"]
            temp_night = day["temp"]["night"]
            weather = day["weather"][0]["description"].title()

            temps.append(temp_day)
            days.append(date)

            card = ctk.CTkFrame(cards_frame, width=120, height=100, corner_radius=12)
            card.grid(row=0, column=i, padx=8, pady=8)

            label = ctk.CTkLabel(
                card,
                text=f"{date}\n🌡 {temp_day}°C / {temp_night}°C\n☁ {weather}",
                font=("Arial", 12),
                justify="center",
            )
            label.pack(padx=5, pady=5)

        # Plot Graph
        fig, ax = plt.subplots(figsize=(7, 3), dpi=100)
        ax.plot(days, temps, marker="o", color="cyan", linewidth=2)
        ax.set_title("7-Day Temperature Trend", fontsize=12, color="white")
        ax.set_ylabel("Temperature (°C)", color="white")
        ax.set_xlabel("Days", color="white")
        ax.tick_params(colors="white")
        fig.patch.set_facecolor("#2b2b2b")
        ax.set_facecolor("#2b2b2b")

        canvas = FigureCanvasTkAgg(fig, master=self.forecast_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)


# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()

