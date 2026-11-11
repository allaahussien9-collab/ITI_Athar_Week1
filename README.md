# Weather Information App

**ITI ATHAR Initiative – Week 1 Task**

## Project Description
A simple Python application that retrieves current weather data from the Open-Meteo public REST API, parses the JSON response, stores the information in a Python class, and displays a formatted weather report.

## Features
- Fetch current weather data using a REST API.
- Parse JSON responses.
- Store weather information in a Python class.
- Display city name, temperature, and humidity.
- Use environment variables for configuration.
- Handle HTTP errors using `raise_for_status()`.

## Technologies
- Python 3
- Requests
- python-dotenv
- Open-Meteo API
- Git and GitHub

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/allaahussien9-collab/ITI_Athar_Week1.git
cd ITI_Athar_Week1
```

**2. Create a virtual environment**

```bash
py -m venv .venv
```

**3. Activate the virtual environment (Windows PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**4. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**5. Create a `.env` file in the project folder**

```env
WEATHER_API_URL=https://api.open-meteo.com/v1/forecast
LATITUDE=31.2001
LONGITUDE=29.9187
CITY=Alexandria
```

**6. Run the application**

```bash
python main.py
```

## Example Output

```text
===== WEATHER REPORT =====
City: Alexandria
Temperature: 19.7 °C
Humidity: 79 %
==========================
```

*Note: Weather values change depending on the current conditions.*

## Project Structure

```text
ITI_Athar_Week1/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

The `.env` file and `.venv` directory are excluded from Git tracking.

## API Information

This application uses the Open-Meteo public weather API, which does not require an API key for standard non-commercial usage.

API documentation: https://open-meteo.com/en/docs