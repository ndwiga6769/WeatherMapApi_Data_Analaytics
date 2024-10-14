# Kenyan Weather Forecast
This Python script fetches and visualizes a 5-day weather forecast for major cities in Kenya, including Nairobi, Mombasa, Kisumu, and Eldoret. It uses the OpenWeatherMap API to retrieve the forecast data and plots temperature, humidity, wind speed, and precipitation for each city.

## Features
Multi-City Support: Get weather data for multiple Kenyan cities.
5-Day Forecast: Retrieves 3-hourly forecast data for the next five days.
Visualization: Plots temperature, humidity, wind speed, and precipitation using Matplotlib.
## Requirements
Python 3.x
Libraries: requests, pandas, matplotlib
## Getting Started
1.Install Dependencies: If you haven't already, install the required libraries using pip:

        bash
        Copy code
        pip install requests pandas matplotlib
2.API Key: Sign up at OpenWeatherMap to get your API key. Replace the placeholder in the script with your actual API key:

        python
        Copy code
        api_key = "YOUR_API_KEY_HERE"
3. Run the Script: Execute the script in your Python environment. The script will fetch weather data and display a plot of the forecast.

## Example Output
The output will show a line plot representing:

Temperature (°C)
Humidity (%)
Wind Speed (m/s)
Precipitation (mm)
Each city's data will be displayed in different colors for easy comparison.

## Note
Ensure that you adhere to the OpenWeatherMap API usage policies, including rate limits.
License
This project is licensed under the MIT License - see the LICENSE file for details.

