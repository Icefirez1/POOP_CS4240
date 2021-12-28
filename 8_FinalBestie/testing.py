import requests
from geopy.geocoders import Nominatim
import json
import os 

AIR_QUALITY_API_KEY = "4d8aa992-f3dd-4306-8219-880f0373ed3b"

geolocator = Nominatim(user_agent="final_project")

print('Welcome to Weather or Not. Please input a location to check data for. (Zip code, address or city)')
user_loc = input('> ')

location = geolocator.geocode(user_loc)

r = requests.get(f"https://api.weather.gov/points/{location.latitude},{location.longitude}")
data = r.json()

forecast = requests.get(data['properties']['forecast']).json()

if forecast.get("status") == 503:
    print("The Weather API is missing data for today in your specified location. Exiting.")
    exit(0)

today = forecast["properties"]["periods"][0]
tomorrow = forecast["properties"]["periods"][2]

# {
#   "number": 1,
#   "name": "Today",
#   "startTime": "2021-11-18T10:00:00-05:00",
#   "endTime": "2021-11-18T18:00:00-05:00",
#   "isDaytime": true,
#   "temperature": 77,
#   "temperatureUnit": "F",
#   "temperatureTrend": "falling",
#   "windSpeed": "6 to 9 mph",
#   "windDirection": "SW",
#   "icon": "https://api.weather.gov/icons/land/day/rain_showers,20?size=medium",
#   "shortForecast": "Slight Chance Rain Showers",
#   "detailedForecast": "A slight chance of rain showers. Partly sunny. High near 77, with temperatures falling to around 70 in the afternoon. Southwest wind 6 to 9 mph, with gusts as high as 16 mph. Chance of precipitation is 20%. New rainfall amounts less than a tenth of an inch possible."
# }
# print(json.dumps(today, indent=2))

#el o el 
air_quality = requests.get(f'http://api.airvisual.com/v2/nearest_city?lat={location.latitude:.3f}&lon={location.longitude:.3f}&key={AIR_QUALITY_API_KEY}').json()
# print(json.dumps(air_quality, indent=2))
# {
#   "status": "success",
#   "data": {
#     "city": "Ogden",
#     "state": "North Carolina",
#     "country": "USA",
#     "location": {
#       "type": "Point",
#       "coordinates": [
#         -77.793399,
#         34.252921
#       ]
#     },
#     "current": {
#       "weather": {
#         "ts": "2021-11-18T16:00:00.000Z",
#         "tp": 22,
#         "pr": 1026,
#         "hu": 74,
#         "ws": 1.34,
#         "wd": 92,
#         "ic": "04d"
#       },
#       "pollution": {
#         "ts": "2021-11-18T16:00:00.000Z",
#         "aqius": 7,
#         "mainus": "p2",
#         "aqicn": 3,
#         "maincn": "p2"
#       }
#     }
#   }
# }
# https://api-docs.iqair.com/?version=latest#detailed-response-example

air_quality_index = air_quality["data"]["current"]["pollution"]["aqius"]
air_pollutant_type = air_quality["data"]["current"]["pollution"]["mainus"]

"""print('Here\'s your weather')

print(f'-- Today\'s Forecast for {air_quality["data"]["city"]} --')
print(f'Temperature: {today["temperature"]} {today["temperatureUnit"]}')
print(f'Short Forcast: {today["shortForecast"]}')

print('-- Pollutants --')
print(f'Air quality index is {air_quality_index}')
print(f'The pollutant that is mostly in the air is {air_pollutant_type}')
"""
print('Weather Output saved to file as weather_output.txt')

with open("weather_output.txt", "w") as OUTfile:
    OUTfile.write('Here\'s your weather\n')
    OUTfile.write(f'-- Today\'s Forecast for {air_quality["data"]["city"]} --\n')
    OUTfile.write(f'Temperature: {today["temperature"]} {today["temperatureUnit"]}\n')
    OUTfile.write(f'Short Forecast: {today["shortForecast"]}\n')
    OUTfile.write(f'Detailed Forcast: {today["detailedForecast"]}\n\n')    
    OUTfile.write(f'-- Tomorrow\'s Forecast for {air_quality["data"]["city"]} --\n')
    OUTfile.write(f'Temperature: {tomorrow["temperature"]} {tomorrow["temperatureUnit"]}\n')
    OUTfile.write(f'Short Forecast: {tomorrow["shortForecast"]}\n')
    OUTfile.write(f'Detailed Forecast: {tomorrow["detailedForecast"]}\n\n')
    OUTfile.write('-- Pollutants --\n')
    OUTfile.write(f'Air quality index is {air_quality_index}\n')
    OUTfile.write(f'The pollutant that is mostly in the air is {air_pollutant_type}\n')

os.startfile("weather_output.txt")