import smtplib
from email.mime.text import MIMEText

def send_email(recipient, subject, body, sender, password):

    msg = MIMEText(body)
    msg['To'] = recipient #', '.join(recipient)
    msg['Subject'] = subject
    msg['From'] = sender
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())
    smtp_server.quit()
    
if __name__ == '__main__':

    recipient = input('Recipient: ')
    subject = input('Subject: ')
    body = input('Message: ')
    sender = input('Sender Email: ')
    password = input('Sender Password (Gmail App Password): ')

    send_email(recipient, subject, body, sender, password)




