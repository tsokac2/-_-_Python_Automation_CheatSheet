import praw

reddit = praw.Reddit(user_agent=True, client_id="youur_id", 
                     client_secret="your_secret", username='your_app_name', 
                     password='your_password')

url = "post_url"

post = reddit.submission(url=url)
print(post.title)
print(post.selftext)

print(len(post.coments))
for comment in post.comments:
    print(comment.body)