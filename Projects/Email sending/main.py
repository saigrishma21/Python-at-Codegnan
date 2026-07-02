import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# loading dotenv file
load_dotenv()
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
SENDER_EMAIL= os.getenv("SENDER_EMAIL")
SENDER_PASSKEY=os.getenv("SENDER_PASSKEY")


def singleEmailSent(to_Email:str,subject:str,body:str):
    msg=MIMEMultipart()
    msg['Subject']=subject
    msg['to']=to_Email
    msg['From']=SENDER_EMAIL
    msg.attach(MIMEText(body,'plain'))
    try:
        #start server configuration
        server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        #start server
        server.starttls()
        #login to server
        server.login(SENDER_EMAIL,SENDER_PASSKEY)
        #sending email
        server.sendmail(from_addr=SENDER_EMAIL,
                        to_addrs=to_Email,
                        msg=msg.as_string())
        #stopping server
        server.quit()
        return f'Successfully email send to {to_Email}'
    except Exception as e:
        return f"Something wrong while  send email an error occured:{e}"
    

#calling Function
to_addr=input("enter to email address:")
subject=input("enter email Subject:")
body =input("enter email body")
print(singleEmailSent(to_Email=to_addr,subject=subject,body=body))



