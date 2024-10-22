#https://www.geeksforgeeks.org/scraping-reddit-using-python/

import praw, json
from praw.models import MoreComments

import pandas as pd

with open('json/config.json') as config_file:
    data = json.load(config_file)

c_id = data['client_id']
c_s = data['client_s']
u_a = data['user_a']

config_file.close()

# Read-only instance
reddit_read_only = praw.Reddit(client_id=c_id,         # your client id
                               client_secret=c_s,      # your client secret
                               user_agent=u_a)        # your user agent


#----------------------------------------------------------------------------------------------
def grab(url):

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

    #post_dump = json.dumps(post_data)

    with open('json/reddit_post.json', 'w') as f:
        json.dump(post_data, f)
        
    f.close()

    post_comments = []
    
    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue
    
        post_comments.append(comment.body)
    
    # creating a dataframe
    comments = pd.DataFrame(post_comments, columns=['comment'])

    comments.to_csv("csv/reddit_comments.csv", index=True)

grab("https://www.reddit.com/r/steinsgate/comments/15yfxsy/i_made_an_irl_amadeus_wip_code_in_comments/")