<div align="center">

# 🌦️ Forecastify-Python  

### *Your Intelligent Weather Forecast Companion*  

<img src="assets/preview.png" alt="Forecastify Logo" width="500"/>  


[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![OpenWeather](https://img.shields.io/badge/API-OpenWeather-orange.svg)](https://openweathermap.org/api)  
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)  

</div>

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 📖 Overview
**Forecastify-Python** is a sleek and powerful weather forecasting application built in Python.  
It comes with a **modern GUI (CustomTkinter)** and a **lightweight CLI version** for terminal lovers.  
Powered by **OpenWeather API**, Forecastify delivers **real-time, accurate, and global** weather information.  

---

## 📌 Features  

| Feature | CLI | GUI |
|---------|-----|-----|
| 🌍 Search by City Name | ✅ | ✅ |
| 📡 Real-time Weather Data | ✅ | ✅ |
| 🌡️ Temperature, Humidity, Wind Speed | ✅ | ✅ |
| 🎨 User-Friendly Interface | ❌ | ✅ |
| 📖 Error Handling | ✅ | ✅ |

---

## 📂 Project Structure
```
Forecastify-Python/
│── Weather_Forecast_App.py   # CLI-based version
│── weather_gui.py             # GUI-based version
│── requirements.txt           # Project dependencies
│── assets/                    # Screenshots, logos
│── .gitignore                 # Ignored files
│── README.md                  # Documentation
```

---

## ⚙️ Installation  

Follow these steps to set up and run the project locally:

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/codebyrupam/Forecastify-Python.git
cd Forecastify-Python
```

2️⃣ Create Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Run the Application
🖥️ GUI Version

```
python weather_gui.py
```
💻 CLI Version
```
python Weather_Forecast_App.py
```
---

## 🚀 Usage

Once you have installed all dependencies, you can run the project in two modes:

🖥️ GUI Mode

A simple graphical interface to check the weather.
```
python weather_gui.py
```
**Features:**

Enter city name and get real-time weather updates

User-friendly interface with clean design

Shows temperature, humidity, weather conditions

## 💻 CLI Mode

A lightweight command-line interface version.
```
python Weather_Forecast_App.py
```
**Features:**

Run directly from the terminal

Quick and minimal weather information

Suitable for low-resource environments

---

## 📸 Demo

City: London

Temperature: 18°C

Condition: Cloudy

Humidity: 65%


<img width="1087" height="363" alt="image" src="https://github.com/user-attachments/assets/095da76e-843c-4713-b09e-8335658dd410" />

---


## 🛠️ Tech Stack

Language: Python 🐍

Libraries: Tkinter, Requests

API: OpenWeather API

---

## 🧩 Roadmap

 Add 7-day weather forecast

 Add Dark/Light theme switch

 Add Unit conversion (°C ↔ °F)

 Export weather data to CSV/PDF

 Build an installer (Windows/Linux)

---

## 🤝 Contributing

Contributions are welcome! 🚀

Fork the repository

Create your feature branch (git checkout -b feature/YourFeature)

Commit changes (git commit -m 'Add new feature')

Push to branch (git push origin feature/YourFeature)

Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

---

 ## 👨‍💻 Author

Rupam Ghosh

🔗 GitHub @codebyrupam

<div align="center">

⭐ If you found this project useful, don’t forget to star the repository! ⭐

</div> 



