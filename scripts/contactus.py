x=1

#gmail stuff

import smtplib, json
from time import sleep

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

with open('json/config.json') as config_file:
    data = json.load(config_file)

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server


#firebase db stuff
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('json/firebase_config.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://social-seafarer-default-rtdb.firebaseio.com"
})

def contactus():

    email_ref = db.reference("/emails/" + str(x) + "/email/")
    name_ref = db.reference("/emails/" + str(x) + "/name/")
    bodyy_ref = db.reference("/emails/" + str(x) + "/body/")

    email = str(email_ref.get())
    name = str(name_ref.get())
    bodyy = str(bodyy_ref.get())


    sender = 'rayleishen@gmail.com'
    password = data['gmail_pass']

    reciever = 'socialseafarer@gmail.com'
    #reciever = 'caleb05w@gmail.com'
    #reciever = 'rayleishen@gmail.com'

    subject = "[!] Social Seafarer Contact Request"
    body = """
    Email request from {} at {}\n
    Message start:
    \n
    {}
    \n
    Message end.
    """.format(name, email, bodyy)

    em = MIMEMultipart()
    em["From"] = sender
    em["To"] = reciever
    em["Subject"] = subject
    
    em.attach(MIMEText(body, 'plain'))

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


url_ref = db.reference("/emails/" + str(x) + "/email/")
new = url_ref.get()
old = new

while True:
    email_ref = db.reference("/emails/" + str(x) + "/email/")
    new = email_ref.get()
    sleep(2.0)
    
    print(".")
    
    if new == old:
        continue
    else:
        print("new request")
        old = new
        contactus()
    
