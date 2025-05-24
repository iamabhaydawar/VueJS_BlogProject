import smtplib #python-in-built lib to send emails to scripts
from email.mime.multipart import MIMEMultipart #for creating body or structure of email
from email.mime.text import MIMEText 

SMTP_SERVER="localhost"
SMTP_PORT=8025
SENDER_EMAIL ='blogAdmin@example'
SENDER_PASSWORD=''
def send_email(to,subject,content):
    msg=MIMEMultipart()
    msg['To']=to
    msg['Subject']=subject
    msg['From']=SENDER_EMAIL

    msg.attach(MIMEText(content,'html'))
    with smtplib.SMTP(host=SMTP_SERVER,port=SMTP_PORT) as  client:
        client.send_message(msg)
        client.quit()
send_email('abhay@example','Test Email','<h1>Welcome to AppDev</h1>')