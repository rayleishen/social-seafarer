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
    

    subject = "[BETA] Social Seafarer Sentiment Analysis"
    body = """

<head>

<script src="https://kit.fontawesome.com/3d577348db.js" crossorigin="anonymous"></script>
<!-- Load icon library -->

<style>

@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&family=Montserrat:wght@100&display=swap');


h1,h2,h3,h4 {
  color:white;
}

* {
  margin:0px;
  padding: 0px;
}

h1 {
  font-size: 60px;
  font-family: 'Comfortaa';
}

h2 {
  font-size: 20px;
  font-weight: 100;
  margin-top: 3%;
  font-family: "Montserrat";
}

h3 {
  font-size: 15px;
  font-weight: 100;
  margin-bottom: 1%;
  font-family: "Montserrat";
}

h4 {
  font-size: 15px;
  font-weight: 100;
  margin-bottom: 1%;
  font-family: "Comfortaa";
}

body {
  background: #D9D9D9;
  background-size: fill;
  margin:0px;
  padding:0px;
  margin:auto;
}

.container-text {
  text-align: center;
  width: 70%;
  height:100vh;
}

.container-border{
  text-align: center;
  width: 70%;
  background-color:#096A7A;
  padding-bottom: 1%;
  margin:auto;
  height:100%;
}

.container-border2{
  text-align: center;
  background-color:#062D40;
  width:100%;
  padding-top:20px;
}

.container-heading{
  display: flex;
  flex-direction: row;
  position: relative;
  left: 5%;
  padding: 5%;
}

.container-center{
  margin-top: 5%;
  margin-bottom: 5%;
  text-align: center;
}

.container-content{
  text-align: center;
  width:100%;
}

.container-title{
  display:flex;
  flex-direction: column;
  text-align: left;
  margin-left:5%;
}

.container-image{
  position:relative;
  height: 200px;
}

input[type="submit"],
	button,
	.button {
    font-family:"Comfortaa";
    font-size: 15px;
    background: none;
    color: white;
    border: white 3px solid;
    padding: 15px;
    border-radius: 15px; 
    margin-bottom: 5%; 
    cursor: pointer;
    transition: all 0.3s ease-in-out; /* animation stuff dw abt it */
  }
  
  /* Hover button */
	input[type="submit"]:hover,
	button:hover,
	.button:hover {
    background-color: #023B53;
    border: 3px solid #023B53;
    color: #fff;
    transform: scale(1.1);
  }

@media only screen and (max-width: 800px) {

.container-border{
  text-align: center;
  width: 80%;
  background-color:#096A7A;
  padding-bottom: 1%;
  margin:auto;
  height:100%;
}

  .container-heading{
  display: flex;
  flex-direction: column;
  position: relative;
  left:0%;
  margin: 5%;
}

.container-title{
  display:block;
  text-align: center;
  margin-top: 5%;
}

.container-image{
  text-align: center;
  margin:auto;
}

h1 {
  font-size: 50px;
}

h2{
  font-size: 10px;
}

h2{
  font-size: 15px;
}

.container-center{
  margin: 5%;
  text-align: center;
}

}

</style>

</head>

<body>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<div class = "container-text container-border">
  <div class="container-heading">
    <img class="container-image" src="assets/css/images/logo.png" alt="Logo" style="object-fit: contain; overflow:visible;">
  <div class= "container-title">
    <h1>Social Seafarer <br> Report</h1>
    <h2> Measuring your Social Imapct</h2> 
  </div>
</div>
<div class= "container-border2">
  <div class = container-content>
        <h1> Name of your post </h1>
    <div class="container-center">
     <h2> This post was analyzed with:</h2>
     <h2> VADAR Sensitivity:</h2>
      <h2> RAKE Sensitivity:</h2>
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
<h3>Post was uploaded on (date), with a total of (number) parent comments. <br><br>Tools used in this Analysis: <br> VADAR (Valence Aware Dictionary and Sentiment Reasoner)  RAKE-nltk (Rapid Automatic Keyword Extraction algorithm)<br><br>Any feedback is appreciated at contact@socialseafarer.com</h3>
</div>
</div>
</meta>
</body>

</html>

    """

    em = MIMEMultipart()
    em["From"] = sender
    em["To"] = reciever
    em["Subject"] = subject
    
    em.attach(MIMEText(body, 'html'))


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
    
emailsender(0, 'caleb05w@gmail.com')