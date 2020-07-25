from bs4 import BeautifulSoup
import requests

weatherLink = requests.get('https://www.wunderground.com/weather/us/ny/new-york-city').text

weather = BeautifulSoup(weatherLink, 'html.parser')

temperature = weather.find("span", {"class": "wu-value wu-value-to"})

temperatureInt = int(temperature.text.strip())

if temperatureInt >= 80:
    print("It will be really really hot outside. The temperature in New York City is ", temperatureInt, ".", sep= "")
elif temperatureInt < 80:
    print("It will be really cold outside. The temperature in New York City is  ", temperatureInt, ".", sep= "")
elif temperatureInt >= 70:
    print("It will be warm outside, you can wear short sleves today. The temperature in New York City is  ", temperatureInt, ".", sep= "")
elif temperatureInt >= 60:
    print("Its chilly outside bring a sweater The temperature in New York City is  ", temperatureInt, ".", sep= "")
elif temperatureInt >= 50:
    print("It is brisk outside like a cool spring day. The temperature in New York City is  ", temperatureInt, ".", sep= "")
elif temperatureInt >= 40:
    print("Its getting cold, wear a jacket. The temperature in New York City is  ", temperatureInt, ".", sep= "")
elif temperatureInt >= 30:
    print("It is close to below freezing a jacket is needed. The temperature in New York City is  ", temperatureInt, ".", sep= "")
elif temperatureInt >= 20:
    print("It below freezing wear a jacket and a hat may be necessary. The temperature in New York City is  ", temperatureInt, ".", sep= "")
else:
    print("An error occured")
