import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

#create text file and record info in it
with open(location+".txt", "w") as file:
	file.write("-------------------------------------------------------------\n")
	file.write("Weather Stats for - {}  || {}".format(location.upper(), date_time)+"\n")
	file.write("-------------------------------------------------------------\n")

	file.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
	file.write("\nCurrent weather desc  :" + str(weather_desc))
	file.write("\nCurrent Humidity      :" + str(hmdt) + '%')
	file.write("\nCurrent wind speed    :" + str(wind_spd) + 'kmph')
