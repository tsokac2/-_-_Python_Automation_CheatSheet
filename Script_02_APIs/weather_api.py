# Access Weather Forcas for specific city data and save it in the *.txt file
import requests

def get_weather(city, units='metric', api_key='<your_api_key>'):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    get_Request = requests.get(url)
    content = get_Request.json()
    with open('weather_data.txt', 'a') as file:
        for dictonary in content['list']:
            file.write(f"{city}, {dictonary['dt_txt']}, {dictonary['main']['temp']}, {dictonary['weather'][0]['description']}\n")
    # return content

print(get_weather(city="Dublin"))
