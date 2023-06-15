import openai
import json
import pandas as pd

from rake_nltk import Rake
import nltk

#comments below lines out to save processing power
nltk.download('punkt')
nltk.download('stopwords')

import re

#with open('config.json') as config_file:
#    data = json.load(config_file)

#key = data['openai_key']

#openai.api_key = key



def keywords(site, sens_rake):
    # Read the CSV file into a pandas DataFrame
    if site == "reddit":      
        df = pd.read_csv('csv/reddit_comments.csv')
    elif site == "youtube":      
        df = pd.read_csv('csv/youtube_comments.csv')

    # Select the second column and convert it to a text Series
    comments_series = df.iloc[:, 1].astype(str)

    # Join the text Series into a single string
    comments_string = ' '.join(comments_series)



    clean_comments_string = re.sub(r'[^\w\s]', '', comments_string)

    r=Rake()
    r.extract_keywords_from_text(clean_comments_string)

    keywords_file = open("dynamic_products/keywords.txt", "w")    
        
    for rating, keyword in r.get_ranked_phrases_with_scores():
        if rating > sens_rake:
            #print(rating, keyword)
            keywords_file.write(str(rating) + " " + keyword + "\n")
            
    keywords_file.close()
