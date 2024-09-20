import praw
from datetime import datetime, timedelta


reddit = praw.Reddit(user_agent=True, 
                     client_id="your_id", 
                     client_secret="your_secret", username='your_app_name', 
                     password='your_password')

subreddit = reddit.subreddit("post_title")

for post in subreddit.new():
    current_time = datetime.now(datetime.timezone.utc)
    post_time = datetime.fromtimestamp(datetime.timezone.utc(post.created))
    delta_time = current_time - post_time

    if delta_time <= timedelta(hours=24):
        if "christmas" in post.title.lower():
            post.reply('Hey, Christmas is coming!')
            for comment in post.comments:
                if 'is coming' in comment.body.lower():
                    comment.reply("Yeah, it's comming!")        