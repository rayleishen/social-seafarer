#from email.message import EmailMessage
#import ssl

import smtplib, json

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

with open('json/config.json') as config_file:
    data = json.load(config_file)

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

def emailsender(site, reciever):

    sender = 'rayleishen@gmail.com'
    password = data['gmail_pass']

    #reciever = 'vaultboy3045@gmail.com'
    
    with open('json/post.json') as p:
        post = json.load(p)
        
        ptitle = post["title"]
        score = post["score"]
        upvote_ratio = post["upvote_ratio"]
        created_utc = post["created_utc"]
        num_comments = post["num_comments"]
         
        p.close()
    
    with open('json/request.json') as r:
        request = json.load(r)
        
        num_top_comments = request["num_top_comments"]
        sens_vadar = request["sens_vadar"]
        sens_rake = request["sens_rake"]
        
        r.close()
    
    
        

    subject = "[BETA] Social Seafarer Sentiment Analysis"
    body = """
    Sentiment analysis of reddit post "{}" with VADAR (Valence Aware Dictionary and sEntiment Reasoner) and 
RAKE-nltk (Rapid Automatic Keyword Extraction algorithm). The post has a total of {} upvotes with an 
upvote ratio of {}. Uploaded to reddit at {} utc with a total of {} parent comments. 

Attached are a pie chart and bar graph representing the ratio of positive, negative and neutral comments 
with VADAR sensitivity set at {}. There is also a list of key phrases sorted with descending relevance 
with RAKE sensitivity set at {}.

Feedback appreciated at contact@socialseafarer.com
    """.format(ptitle, score, upvote_ratio, created_utc, num_comments, sens_vadar, sens_rake)

    em = MIMEMultipart()
    em["From"] = sender
    em["To"] = reciever
    em["Subject"] = subject
    
    em.attach(MIMEText(body, 'plain'))


    filename = 'pie_chart.png'
    attachments = open('dynamic_products/' + filename, 'rb')
    emImage1 = MIMEImage(attachments.read())
    attachments.close()
    emImage1.add_header('Content-Disposition', "attachment; filename= " + filename)
    em.attach(emImage1)

    filename = 'bar_graph.png'
    attachments = open('dynamic_products/' + filename, 'rb')
    emImage2 = MIMEImage(attachments.read())
    attachments.close()
    emImage2.add_header('Content-Disposition', "attachment; filename= " + filename)
    em.attach(emImage2)
    
    filename = 'keywords.txt'
    attachments = open('dynamic_products/' + filename, 'rb')
    emKeywords = MIMEBase('application', 'octet-stream')
    emKeywords.set_payload((attachments).read())
    encoders.encode_base64(emKeywords)
    emKeywords.add_header('Content-Disposition', "attachment; filename= " + filename)
    em.attach(emKeywords)

    # Cast as string
    text = em.as_string()

    # Connect with the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(sender, password)
    print("Succesfully connected to server")
    print()


    # Send emails to "person" as list is iterated
    print(f"Sending email to: {reciever}...")
    TIE_server.sendmail(sender, reciever, text)
    print(f"Email sent to: {reciever}")
    print()
    
    TIE_server.quit()
    
