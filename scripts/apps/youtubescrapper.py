import os, json

import googleapiclient.discovery
from googleapiclient.discovery import build
import re

import urllib.parse

import pandas as pd

with open('json/config.json') as config_file:
    data = json.load(config_file)

dev_key = data['youtube_dev']

config_file.close()

def grab(video_url):

    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urllib.parse.urlparse(video_url)
    if query.hostname == 'youtu.be':
        video_id = query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urllib.parse.parse_qs(query.query)
            video_id = p['v'][0]
        if query.path[:7] == '/embed/':
            video_id = query.path.split('/')[2]
        if query.path[:3] == '/v/':
            video_id = query.path.split('/')[2]
    
    # empty list for storing reply
    replies = []
 
    api_service_name = "youtube"
    api_version = "v3"

    # creating youtube resource object
    youtube = build(api_service_name, api_version, developerKey=dev_key)
 
    # retrieve youtube video results
    video_response=youtube.commentThreads().list(
    part='snippet,replies',
    videoId=video_id
    ).execute()
    
    #youtube video statistics
    ytstats = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    id=video_id
    ).execute()

    post_data = {
        "title": ytstats['items'][0]['snippet']['title'],
        "video_id": ytstats['items'][0]['id'],
        "publish_date": ytstats['items'][0]['snippet']['publishedAt'],
        "view_count": ytstats['items'][0]['statistics']['viewCount'],
        "like_count": ytstats['items'][0]['statistics']['likeCount'],
        "fav_count": ytstats['items'][0]['statistics']['favoriteCount'],
        "comment_count": ytstats['items'][0]['statistics']['commentCount']
    }
    
    with open('json/yt_post.json', 'w') as f:
        json.dump(post_data, f)
    
    f.close()

    video_comments = []
    
    # iterate video response
    while video_response:
       
        # extracting required info
        # from each result object
        for item in video_response['items']:
           
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            video_comments.append(comment)
            
            
            # counting number of reply of comment
            replycount = item['snippet']['totalReplyCount']
 
            # if reply is there
            #if replycount>0:
               
                # iterate through all reply
                #for reply in item['replies']['comments']:
                   
                    # Extract reply
                    #reply = reply['snippet']['textDisplay']
                     
                    # Store reply is list
                    #replies.append(reply)
 
            # print comment with list of reply
            # print(comment, replies, end = '\n\n')
 
            # empty reply list
            replies = []
 
        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = video_id,
                      pageToken = video_response['nextPageToken']
                ).execute()
        else:
            comments = pd.DataFrame(video_comments, columns=['comment'])
            
            comments.to_csv("csv/youtube_comments.csv", index=True)
            break
        
        
grab('https://youtu.be/UagcwsLlbD0')
