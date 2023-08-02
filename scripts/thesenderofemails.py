#from email.message import EmailMessage
#import ssl

import smtplib, json, os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

with open(os.getcwd() + '/config.json') as config_file:
    data = json.load(config_file)

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

def emailsender(reciever):

    sender = 'rayleishen@gmail.com'
    password = data['gmail_pass']

    #reciever = 'vaultboy3045@gmail.com'

    subject = "test"
    body = """
    asdasd
    asdasdsa
    asdasdasds
    asdasdasdada
    asdasdasdasdasd
    """

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
    
    

emailsender('vaultboy3045@gmail.com')