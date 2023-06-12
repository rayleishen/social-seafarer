#https://www.geeksforgeeks.org/scraping-reddit-using-python/

import praw, json
import pandas as pd
from praw.models import MoreComments

with open('config.json') as config_file:
    data = json.load(config_file)

c_id = data['client_id']
c_s = data['client_s']
u_a = data['user_a']

# Read-only instance
reddit_read_only = praw.Reddit(client_id=c_id,         # your client id
                               client_secret=c_s,      # your client secret
                               user_agent=u_a)        # your user agent

url = "https://www.reddit.com/r/Animemes/comments/13yuisl/i_said_what_i_said_moments/"



#----------------------------------------------------------------------------------------------
def grab_reddit(url):

    # URL of the post
    
    # Creating a submission object
    submission = reddit_read_only.submission(url=url)

    post_data = {
        "title": submission.title,
        "url": submission.url,
        "score": submission.score,
        "upvote_ratio": submission.upvote_ratio,
        "created_utc": submission.created_utc,
        "num_comments": submission.num_comments
    }

    post_dump = json.dumps(post_data)

    with open('post.json', 'w') as f:
        json.dump(post_data, f)



    post_comments = []
    
    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue
    
        post_comments.append(comment.body)
    
    # creating a dataframe
    comments = pd.DataFrame(post_comments, columns=['comment'])
    comments

    comments.to_csv("comments.csv", index=True)

def grab_youtube():
    print("###")
