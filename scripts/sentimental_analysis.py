from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')


nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


import csv
import os

#can be changed by user
num_top_comments=999 #how many of the top comments default=99
sens=0.2 #how sensative is VADER default=0.2


#add parameters
def run(site, num_top_comments, sens):
    if num_top_comments == 0:
        num_top_comments = 999
    if sens == 0:
        sens = 0.2
            
    sia=SIA()
    results = []
    comments = []
    
    if site == "reddit":
        site_csv = os.getcwd() + '/csv/reddit_comments.csv'
        site_csv_labels = os.getcwd() + '/csv/reddit_comments_labels.csv'
    if site == "youtube":
        site_csv = os.getcwd() + '/csv/youtube_comments.csv'
        site_csv_labels = os.getcwd() + '/csv/youtube_comments_labels.csv'
    
    with open(site_csv, errors="ignore") as file_obj:
        reader_obj = csv.reader(file_obj)
        for line in reader_obj:
            #a=sia.polarity_scores(str(line))
            #print(a)
            pol_score=sia.polarity_scores(str(line))
            pol_score['comment']=line
            results.append(pol_score)
                    
            
    #pprint(results[:num_top_comments], width=100)

    df = pd.DataFrame.from_records(results)
    df.head()

    #ADJUST 0.2 as SENSATIVITY
    df['label'] = 0
    df.loc[df['compound'] > sens, 'label'] = 1
    df.loc[df['compound'] < -sens, 'label'] = -1
    df.head()


    #Clears csv and saves data
    f = open(site_csv_labels, "w+")
    f.close()
    df2 = df[['comment', 'label']]
    df2.to_csv(site_csv_labels, mode='a', encoding='utf-8', index=False)


    #print("Positive comments:\n")
    #pprint(list(df[df['label'] == 1].comment)[:5], width=200)

    #print("\nNegative comments:\n")
    #pprint(list(df[df['label'] == -1].comment)[:5], width=200)

    #print(df.label.value_counts())

    #print(df.label.value_counts(normalize=True) * 100)
    
    return df
    

################################################################


def bar_graph(df):
    fig, ax = plt.subplots(figsize=(8, 8))

    data = df.label.value_counts(normalize=True) * 100

    sns.barplot(x=data.index, y=data, ax=ax)

    ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
    ax.set_xlabel("Opinion")
    ax.set_ylabel("Percentage")

    #plt.show()
    #plt.savefig('bar_graph.png', bbox_inches='tight')
    
    plt.savefig('dynamic_products/bar_graph.png')


def pie_chart(df):   
    data = df.label.value_counts(normalize=True) * 100
    labels = ['Neutral', 'Negative', 'Positive']

    colors = sns.color_palette('pastel')[0:5]

    #create pie chart
    plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
    
    plt.savefig('dynamic_products/pie_chart.png')
