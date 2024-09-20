import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(user_agent=True, 
                     client_id="your_id", 
                     client_secret="your_secret", username='your_app_name', 
                     password='your_password')

subreddit = reddit.subreddit("glassblowing")

post24h = []

with open('output.txt', 'w') as file:
    for post in subreddit.new():
        current_time = datetime.now(datetime.timezone.utc)
        post_time = datetime.utcfromtimestamp(post.created)
        print(current_time, post_time)

        delta_time = current_time - post_time
        print(delta_time)
        if delta_time <= timedelta(hours=24):
            print(post.title, post.selftext)
            post24h.append((post.title, post.selftext, post_time))

print(post24h)