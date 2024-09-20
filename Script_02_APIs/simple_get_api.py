import requests

url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=36e6f30176404586a22893235b25572c"
get_Request = requests.get(url)
content = get_Request.json()
print(type(content))
print(content['articles'][0]['url'])