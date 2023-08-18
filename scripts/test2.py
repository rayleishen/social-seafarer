import smtplib
from email.mime.text import MIMEText
from jinja2 import Template

sender_email = "rayleishen@gmail.com"
sender_password = "iwuwvdqqyfrlbrbm"
recipient_email = "rayleishen@gmail.com"
with open('email_template.html', 'r') as f:
    template = Template(f.read())
context = {
    'subject': 'Hello from Python',
    'body': 'This is an email sent from Python using an HTML template and the Gmail SMTP server.'
}
html = template.render(context)
html_message = MIMEText(context['body'], 'html')
html_message['Subject'] = context['subject']
html_message['From'] = sender_email
html_message['To'] = recipient_email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
   server.login(sender_email, sender_password)
   server.sendmail(sender_email, recipient_email, html_message.as_string())