
# import required modules
from pyowm import OWM
import requests
owm = OWM('f05a9669cf26125379f17a8bdc8b9f4d', version='2.5')
# When has the forecast been received?


# Enter your API key here
api_key = "f05a9669cf26125379f17a8bdc8b9f4d"

# base_url variable to store url
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
# Give city name
city_name =input("Enter city name : ")
obs = owm.weather_at_place(city_name)
obs.get_reception_time(timeformat='iso')
w = obs.get_weather()
# complete_url variable to store
# complete url address
complete_url = base_url + "q=" + city_name + "&APPID=f05a9669cf26125379f17a8bdc8b9f4d"

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]
    a= x["coord"]
    b= x['wind']
    c= x['visibility']
    d= x['clouds']
    e= x['sys']
    clouds=d['all']
    long=a["lon"]
    lat=a["lat"]
    windspd= b['speed']
    winddir= b['deg']
    vis=c
    country=e['country']

    sunrise=e['sunrise']
    sunset=e['sunset']
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y['temp']
    TempF=int((((int(current_temperature)-273.15)*(9/5))+32)*100)/100
    temp_max=y['temp_max']
    TempMF=int((((int(temp_max)-273.15)*(9/5))+32)*100)/100
    temp_min=y['temp_min']
    TempmF=int((((int(temp_min)-273.15)*(9/5))+32)*100)/100
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
    PresA=int((int(current_pressure))/10.132501)/100
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
    Humidity=int(int(current_humidity)*100)/100
    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
    main_description=x["base"]
    # print following values)

    print(obs.get_reception_time(timeformat='iso'))
    print('     Latitude='+str(lat)+'   Longitude= '+str(long))
    print(" Temperature = " +
                    str(TempF) + u"\u2109"
                    '\n  High = '+str(TempMF)+u"\u2109"
                    '\n  Low = '+str(TempmF)+u"\u2109"
                    '\n  Wind Speed= '+str(windspd)+' mph'+
                    '    \n  Wind Direction= '+str(winddir)+u"\u00b0"+
          "\n Atmospheric Pressure (in atm) = " +
                    str(PresA) +
          "\n Humidity = " +
                    str(Humidity)+'%' +
          "\n Description = " +
                    str(weather_description)+
          '\n Visibility = '+ str(vis)+
          '\n Clouds = '+ str(clouds)+'%'
          '\n Country = '+ str(country)+
          '\n Rain = '+ str(w.get_rain())+
          '\n Sunrise = '+ str(w.get_sunrise_time('iso')) +
          '\n Sunset = '+ str(w.get_sunset_time('iso')))

else:
    print(" City Not Found ")
obs = owm.weather_at_place(city_name)
obs.get_reception_time(timeformat='iso')



