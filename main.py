import requests

# import requests

# # WeatherAPI request
# weatherapi_url = "http://api.weatherapi.com/v1/current.json"
# params = {
#     'key': 'danwycliffnjokandwiga0720292757',  # Your provided API key
#     'q': 'Nairobi',  # City to query
#     'aqi': 'yes'  # Air Quality Index not required
# }

# response = requests.get(weatherapi_url, params=params)
# weather_data = response.json()

# # Print the fetched weather data
# print(weather_data)


# OpenWeatherMap API request
import requests
import psycopg2
from datetime import datetime

# Fetch weather data from OpenWeatherMap API
openweather_url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'Nairobi,KE',  # City and country code
    'appid': 'c35aaeb68bf03d486a1fce460df95b19',  # API key (replace if disabled)
    'units': 'metric'  # Metric units for temperature (Celsius)
}

response = requests.get(openweather_url, params=params)
openweather_data = response.json()

# Extract relevant weather information
city = openweather_data['name']
country = openweather_data['sys']['country']
temperature = openweather_data['main']['temp']
humidity = openweather_data['main']['humidity']
wind_speed = openweather_data['wind']['speed']
weather_description = openweather_data['weather'][0]['description']
recorded_at = datetime.now()

# Print the extracted data (optional)
print(f"City: {city}, Country: {country}, Temperature: {temperature}°C, "
      f"Humidity: {humidity}%, Wind Speed: {wind_speed} m/s, Weather: {weather_description}, "
      f"Recorded At: {recorded_at}")

# Insert data into PostgreSQL
try:
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="your_dbname",  # Replace with your database name
        user="your_username",  # Replace with your PostgreSQL username
        password="your_password",  # Replace with your PostgreSQL password
        host="localhost",  # or other hostname if you're using a remote server
        port="5432"  # default PostgreSQL port
    )
    cursor = conn.cursor()

    # SQL query to insert data
    insert_query = """
    INSERT INTO weather_data (city, country, temperature, humidity, wind_speed, weather_description, recorded_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    # Execute the query with the weather data
    cursor.execute(insert_query, (city, country, temperature, humidity, wind_speed, weather_description, recorded_at))

    # Commit the transaction to make sure the data is saved
    conn.commit()
    print("Weather data inserted successfully into PostgreSQL")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")

