# ----------------------------------------------------------------------------
# sendEmail Function
# Author: Ren Demeis-Ortiz
# Description: This function sends an email using arguments passed.
#   Sources: https://realpython.com/python-send-email/#getting-started
#            https://www.youtube.com/watch?v=JRCJ6RtE3xU
# ----------------------------------------------------------------------------
import smtplib, ssl
from mcred import address, user, pwd
from email.message import EmailMessage


def sendEmail(recipient, senderName, senderEmail, subject, text, html=None):
    '''
    Sends message to recipient from user using smtp server in mcred.py
    
    Parameters:
        recipient: email address of recipient
        senderName: name of the sender to appear at the end of email message
        senderEmail: email address to appear at the end of email message
        subject: subject of the email
        message: content of the email
    
    Returns: isSent as true if email is sent.
    '''
    
    isSent = True
    port = 587
    context = ssl.create_default_context()
    server = smtplib.SMTP(address, port)
    
    #Create EmailMessage Object 
    footer = f'This message was sent by Dev Send EZ on behalf of {senderName} at {senderEmail}'
    htmlFooter = f'This message was sent by Dev Send EZ on behalf of {senderName} at <a href="mailto:{senderEmail}">{senderEmail}</a>'
    message = EmailMessage()
    message['To'] = recipient
    message['From'] = user
    message['Subject'] = subject
    message.set_content(text+footer)
    
    if html is not None:
        message.add_alternative(html+htmlFooter, subtype='html')
    
    try:
        # Log into server
        server.starttls(context=context)
        server.ehlo()
        server.login(user, pwd)
        
        # Send Email
        server.send_message(message)
      
    except Exception as e:
        isSent=False
        print(e)
    
    finally: 
        server.quit()    
    
    return isSent
    
# To Do
# Try try/except
# Try using enviornment variables instead of cred file
# Try using API for 