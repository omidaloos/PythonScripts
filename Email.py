import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient #', '.join(recipient)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())
    smtp_server.quit()
    
subject = input('Subject: ')
body = input('Message: ')
sender = "My Email"
recipient = input('Recipient: ')
password = "Gmail App Password (special password in settings)"

send_email(subject, body, sender, recipient, password)