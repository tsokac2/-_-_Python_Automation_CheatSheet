# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/
import requests

url = "https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3"

req = requests.get(url)
content = req.content

with open('downloads/dowload.mp3', 'wb') as file:
  file.write(content)