import praw

reddit = praw.Reddit(user_agent=True, 
                     client_id="your_id", 
                     client_secret="your_secret", username='your_app_name', 
                     password='your_password')

subreddit = reddit.subreddit("subject_title")
subreddit.validate_on_submit = True

title = 'This is my new Python Bot submission'
content = """
Hey, I am just trying out Python!
This is my first post!
"""

subreddit.submit(title=title, selftext=content)