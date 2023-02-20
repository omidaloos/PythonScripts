#!/usr/bin/env python3


import os
import shutil
import sys
import socket
import psutil
import smtplib
from email.mime.text import MIMEText

### CHECKS

def check_reboot():
    """Returns true if the computer has pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full (disk, min_gb, min_percent):
    """Returns true if there isnt enough disk space. False Otherwise"""
    du = shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns true if the root partition is full, false otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_cpu_constrained():
    """Returns true if cpu is having too much usage, false otherwise"""
    return psutil.cpu_percent(1) > 75

def check_no_network():
    """Returns true if it fails to resolve Google's URL, false otherwise."""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True
    
### END OF CHECKS

### EMAIL FUNCTIONALITY 
    
def send_email(subject, body, sender, recipient, password):
    """Used to send an email to a recipient"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient #', '.join(recipient)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())
    smtp_server.quit()

# Get gmail app password from separate file    
with open ('/Users/Omid/Desktop/Portfolio/GitPortfolio/PythonScripts/Email/GmailAppPassword.txt', 'r') as file:
    pswd = file.read()

### END OF EMAIL FUNCTIONALITY 

def main():
    """Preforms all checks and sends an email if any do not pass and exits with status code (1). 
    Exits with status code (0) otherwise. """
    checks = [
        (check_reboot, "Pending reboot."),
        (check_root_full, "Root partition full."),
        (check_cpu_constrained, "CPU load too high."),
        (check_no_network, "No working network.")
    ]
    
    everything_ok = True
    
    for check, msg in checks:
        if check():
            everything_ok = False
            send_email("Issue on server", msg, "omidaloos111@gmail.com", "omidaloos321@gmail.com", pswd)
            print (msg)
            sys.exit(1)
            
        if not everything_ok:
            sys.exit(1)
            
    print ("Everything ok.")
    sys.exit(0)
    
main()
