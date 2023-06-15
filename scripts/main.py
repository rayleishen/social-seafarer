import opwebscrapper, sentimental_analysis, summarizer

#variables
url = "https://www.reddit.com/r/technology/comments/1439n76/apples_vision_pro_is_a_3500_ticket_to_nowhere_a/"
num_top_comments = 99
sens_vadar = 0.2
sens_rake = 5

#products
#png of charts
#csv of comments
#csv of key phrases



if "reddit.com" in url:
    opwebscrapper.grab_reddit(url)
    site = "reddit"
    
elif "youtube.com" in url:
    opwebscrapper.grab_youtube(url)
    site = "youtube"
    
else:
    print("error")
    
    
df = sentimental_analysis.run(site, num_top_comments, sens_vadar)


sentimental_analysis.pie_chart(df)
sentimental_analysis.bar_graph(df)



summarizer.keywords(site, sens_rake)