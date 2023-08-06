import json

with open('csv/post.json') as p:
        post = json.load(p)
        ptitle = post['title']
        
        print(ptitle)
        