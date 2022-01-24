import praw
import pandas as pd 

reddit = praw.Reddit('irbot_readonly')

print(reddit.read_only)

for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)

'''
filter for top posts.
 Comments sorted by ’top’. 
tory tl;dr regex everything after ”tl;dr”. 

both the ”top-level” comments
and the replies to these
'''

for submission in reddit.subreddit("relationships").top("year", limit=2):
    print(submission.title)

for top_level_comment in submission.comments[:3]:
    print(top_level_comment.body)
    
    print(submission.num_comments)

# 25k rows
# rick and morty: 1900 rows

submission.selftext

