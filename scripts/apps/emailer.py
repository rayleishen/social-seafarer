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

    if site=="reddit":
        postdata = "reddit_post"
    elif site=="youtube":
        postdata = "youtube_post"

    
    with open('json/'+ postdata +'.json') as p:
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

    with open('dynamic_products/summary.txt', 'r') as s:
        summary = s.read()

        s.close()

    with open('emailformat.txt', 'r') as e:
        emailformat = e.read()

        e.close()
    
    
        

    subject = "[BETA] Social Seafarer Sentiment Analysis"
    body = """
<html lang = "eng">
<head>

  <script src="//static.filestackapi.com/filestack-js/3.x.x/filestack.min.js"></script>
<script src="https://kit.fontawesome.com/3d577348db.js" crossorigin="anonymous"></script>
<!-- Load icon library -->

<style>

@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&family=Montserrat:wght@100&display=swap');

{}

</style>

</head>

<body>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<div class = "container-text container-border">
  <div class="container-heading">
    <div class= "container-title">
    <h1>Social Seafarer Report</h1>
    <h2> Measuring your Social Impact.</h2> 
  </div>
</div>
<div class= "container-border2">
  <div class = container-content>
        <h1> Name of your post: {} </h1>
    <div class="container-center">
     <h2> Summary of the post's keywords by (OpenAI GPT-3.5 turbo): {} </h2>
     <h2> VADAR Sensitivity: {} </h2>
      <h2> RAKE Sensitivity: {} </h2>
    </div>
    <div class="container-center">
      <h4> Post sentiment attatched in the bottom graphs & charts. </h4>
    </div>
    <div class="container-center">
      <h3>Find another post</h3>
      <a href="https://www.socialseafarer.com"><input type="submit" id="submit" value="Search >>"></a>
    </div>
  </div>
</div>

<div class = "container-center">
<h3>Post was uploaded on {}, with a total of {} parent comments. <br><br>Tools used in this Analysis: <br> VADAR (Valence Aware Dictionary and Sentiment Reasoner) <br> RAKE-nltk (Rapid Automatic Keyword Extraction algorithm)<br><br>Any feedback is appreciated at contact@socialseafarer.com</h3>
</div>
</div>
</meta>
</body>

</html>
    """.format(emailformat, ptitle, summary, sens_vadar, sens_rake, created_utc, num_comments)

    em = MIMEMultipart()
    em["From"] = sender
    em["To"] = reciever
    em["Subject"] = subject
    
    em.attach(MIMEText(body, 'html'))


    filename = 'pie_chart.png'
    attachments = open('dynamic_products/' + filename, 'rb')
    emImage1 = MIMEImage(attachments.read())
    attachments.close()
    emImage1.add_header('Content-Disposition', "attachment; filename= " + filename)
    em.attach(emImage1)

#    filename = 'bar_graph.png'
#    attachments = open('dynamic_products/' + filename, 'rb')
#    emImage2 = MIMEImage(attachments.read())
#    attachments.close()
#    emImage2.add_header('Content-Disposition', "attachment; filename= " + filename)
#    em.attach(emImage2)
    
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
    
#emailsender('reddit', 'vaultboy3045@gmail.com')