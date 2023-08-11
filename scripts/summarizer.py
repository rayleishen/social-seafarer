import openai
import json
import pandas as pd

from rake_nltk import Rake
import nltk

#comments below lines out to save processing power
#nltk.download('punkt')
#nltk.download('stopwords')

import re
import os
import math


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
            
            #rating = int(rating*100)/100
            #keywords_file.write(str(rating) + " " + keyword + "\n")
            keywords_file.write(keyword + "\n")
            
    keywords_file.close()



def compile_summary():
    with open('json/config.json') as config_file:
        data = json.load(config_file)

    key = data['openai_key']

    openai.api_key = key

    # Define file paths
    input_file_path = 'dynamic_products/keywords.txt'
    output_file_path = 'dynamic_products/summary.txt'

    # Read keywords and weights from the input file
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Parse the lines into weights and messages
    data = []
    total_tokens = 0  # To keep track of the total tokens
    for line in lines:
        message = line.strip()
        message_tokens = len(message.split())  # Calculate the tokens in the message
        if total_tokens + message_tokens + 1 <= 3750:  # Check if adding the line exceeds the limit
            data.append(message)  # Only store the message content
            total_tokens += message_tokens + 1  # Add 2 for the space

    # Generate a summary using OpenAI
    keywords = '\n'.join(data)
    prompt = f'Summarize the general sentiment of the following keywords into one cohesive paragraph:\n{keywords}'
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=250  # You can adjust this value to control the length of the summary
    )
    summary = response.choices[0].text.strip()  # Remove leading/trailing whitespace
    
    newline_index = summary.find('\n')

    # Extract the portion of text after the newline
    extracted_text = summary[newline_index + 1:]
    # print(extracted_text) For debugging purposes

    # Create the folder if it doesn't exist
    folder_path = os.path.dirname(output_file_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Write the summary to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(extracted_text)

    print(f"Summary saved to '{output_file_path}'")

    # Rest of your existing code follows...

# Call the function to compile the summary
compile_summary()
