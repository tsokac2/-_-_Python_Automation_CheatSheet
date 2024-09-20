import requests
import json

url = 'https://api.languagetool.org/v2/check'
data = {
    'text': 'Tis is a nixe day!',
    'language': 'auto'
}
response = requests.get(url, data=data)
results = json.loads(response.text)
print(type(results))