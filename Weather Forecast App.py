import requests
from datetime import datetime

# Replace with your own OpenWeatherMap API key
API_KEY = "c9fd221e9c9b15b3b5dc2a987537f06e"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_weather(city):
    # Automatically add ,IN if not present
    if "," not in city:
        city = city + ",IN"

    # Current weather
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print(f"❌ City not found: {city}. Please try again.")
        return None

    print("\n---- Current Weather ----")
    print(f"City: {data['name']}, {data['sys']['country']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description'].title()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

    return data["coord"]  # return lat, lon for forecast


def get_forecast(lat, lon):
    # 7-day forecast (One Call API)
    url = f"{BASE_URL}onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "daily" not in data:
        print("⚠️ Forecast data not available. Check your API key or plan.")
        return

    print("\n---- 7-Day Forecast ----")
    for day in data["daily"][:7]:
        date = datetime.fromtimestamp(day["dt"]).strftime("%Y-%m-%d")
        temp_day = day["temp"]["day"]
        temp_night = day["temp"]["night"]
        weather = day["weather"][0]["description"].title()
        print(f"{date}: {weather}, Day {temp_day}°C / Night {temp_night}°C")


if __name__ == "__main__":
    city = input("Enter city name: ")
    coords = get_weather(city)
    if coords:
        get_forecast(coords["lat"], coords["lon"])

