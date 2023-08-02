x = 0

#dbgrab#
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase-config.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://social-seafarer-default-rtdb.firebaseio.com"
})

url_ref = db.reference("/requests/" + str(x) + "/url/")
#print(url_ref.get())
url = url_ref.get()


ntc_ref = db.reference("/requests/" + str(x) + "/num_top_comments/")
sv_ref = db.reference("/requests/" + str(x) + "/sens_vadar/")
sr_ref = db.reference("/requests/" + str(x) + "/sens_rake/")

#email = db.reference("/requests/" + str(x) + "/email/")
email = 'vaultboy3045@gmail.com'

num_top_comments = ntc_ref.get()
sens_vadar = sv_ref.get()
sens_rake = sr_ref.get()


#main#
import opwebscrapper, sentimental_analysis, summarizer, thesenderofemails

###variables###
#url = "https://www.reddit.com/r/technology/comments/1439n76/apples_vision_pro_is_a_3500_ticket_to_nowhere_a/"
#num_top_comments = 99
#sens_vadar = 0.2
#sens_rake = 5

###products###
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

thesenderofemails(email)