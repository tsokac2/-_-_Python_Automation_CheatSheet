import requests
# get_Request = requests.get(url)
# content = get_Request.json()
# print(type(content))
# print(content['articles'])
# articles = content['articles']
# print(type(articles))
# for article in articles:
#     print('TITLE\n', article['title'], 'DESCRIPTION\n',article['description'])


# Geting all topics for the specific date range
# def get_news(topic, from_date, to_date, language='en', 
#              api_key='36e6f30176404586a22893235b25572c'):
#    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
#    get_Request = requests.get(url)
#    content = get_Request.json()
#    articles = content['articles']
#    results = []
#    for article in articles:
#       results.append(f"TITLE\n{article['title']}, \nDESCRIPTION\n, {article['description']}")
#    return results

# print(get_news(topic='space', from_date='2022-02-27', to_date='2022-02-28'))

# Geting all headlines by the country
def get_news(country, api_key='36e6f30176404586a22893235b25572c'):
   url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
   get_Request = requests.get(url)
   content = get_Request.json()
   articles = content['articles']
   results = []
   for article in articles:
      results.append(f"TITLE\n{article['title']}, \nDESCRIPTION\n, {article['description']}")
   return results

print(get_news(country='us'))

