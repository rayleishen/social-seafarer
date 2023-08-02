x = 2

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
email_ref = db.reference("/requests/" + str(x) + "/email/")
key_ref = db.reference("/requests/" + str(x) + "/key/")
ntc_ref = db.reference("/requests/" + str(x) + "/num_top_comments/")
sv_ref = db.reference("/requests/" + str(x) + "/sens_vadar/")
sr_ref = db.reference("/requests/" + str(x) + "/sens_rake/")


url = url_ref.get()
email = email_ref.get()
key = key_ref.get()
num_top_comments = int(ntc_ref.get())
sens_vadar = int(sv_ref.get())
sens_rake = int(sr_ref.get())

if num_top_comments == 0:
    num_top_comments = 99
if sens_vadar == 0:
    sens_vadar = 0.2
if sens_rake == 0:
    sens_rake = 5


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

thesenderofemails.emailsender(email)