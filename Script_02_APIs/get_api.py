import requests

url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=<your_api_key>"
get_Request = requests.get(url)
content = get_Request.json()
print(type(content))
print(content['articles'][0]['url'])