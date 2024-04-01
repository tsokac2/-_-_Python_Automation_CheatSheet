import requests

url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=36e6f30176404586a22893235b25572c"

getRequest = requests.get(url)

content = getRequest.json()

print(content)