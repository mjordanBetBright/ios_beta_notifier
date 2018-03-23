#!/usr/bin/python
import praw
import pdb
# import re
import os
import datetime

reddit = praw.Reddit('bot1')

if not os.path.isfile("stickied_posts.txt"):
    stickied_posts = []
    # stickied_posts.append(str(datetime.datetime.now()))
    # print("first run")
else:
    with open ("stickied_posts.txt", "r") as f:
        stickied_posts = f.read()
        stickied_posts = stickied_posts.split("\n")
        stickied_posts = list(filter(None, stickied_posts))
        # print(stickied_posts)
	
	
subreddit = reddit.subreddit("iOSBeta")

for submission in subreddit.hot(limit=5):
    # stickied_posts.append(str(datetime.datetime.now()))
    if submission.stickied and submission.id not in stickied_posts:
        submission.save(submission.id)
        stickied_posts.append(submission.id)
        # print("Title: ", submission.title)
        # print(stickied_posts)
		
# stickied_posts.append(str(datetime.datetime.now()))

with open("stickied_posts.txt", "w") as f:
    for post_id in stickied_posts:
        f.write(post_id + "\n")
        