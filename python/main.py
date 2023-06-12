import webscrapper, sentimental_analysis, summarizer

#variables
url = "https://www.reddit.com/r/LeagueOfMemes/comments/146ajwe/finally_a_vayne_counter/?utm_source=share&utm_medium=web2x&context=3"
num_top_comments = 100
sens_vadar = 0.2
sens_rating = 5

#products
#png of charts
#csv of comments
#csv of key phrases



if "reddit.com" in url:
    webscrapper.grab_reddit(url)
    
elif "youtube.com" in url:
    webscrapper.grap_youtube(url)
    
else:
    print("error")
    
    
df = sentimental_analysis.run(num_top_comments, sens_vadar)



sentimental_analysis.bar_graph(df)
sentimental_analysis.pie_chart(df)


summarizer.keywords(sens_rating)