# Weather-Application-using-API-and-Tkinter
Weather Application using API and Tkinter
This is a simple Weather Application built using Python, Tkinter, and various libraries to provide users with real-time weather updates based on their location. It includes user authentication and displays the current weather, temperature, humidity, wind speed, and other weather conditions.

## Features

- User authentication with sign-in and sign-up functionality.
- Real-time weather data retrieval using the OpenWeatherMap API.
- Notifications based on weather conditions (e.g., sunny, rainy, cold).
- User-friendly GUI built with Tkinter.
- Displays current local time based on the user's location.

## Libraries Used

- `Tkinter`: For creating the graphical user interface.
- `requests`: To make HTTP requests to the OpenWeatherMap API.
- `geopy`: For converting city names to geographical coordinates.
- `timezonefinder`: To find the timezone based on geographical coordinates.
- `pytz`: To handle timezone conversions.
- `PIL (Pillow)`: For image handling in the GUI.
- `plyer`: For sending desktop notifications.
Usage
Run the application:
python main.py
Sign up for a new account or sign in with your existing credentials.
Enter a city name in the search bar to get the current weather information.
The application will display the weather conditions, and notifications will appear based on the current weather.
