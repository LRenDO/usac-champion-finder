# ----------------------------------------------------------------------------
# Helper Functions
# Author: Ren Demeis-Ortiz
# Description: These are the helper functions for the DevSendEZ send email API
#   Sources: https://realpython.com/python-send-email/#getting-started
#            https://www.youtube.com/watch?v=JRCJ6RtE3xU
# ----------------------------------------------------------------------------
import smtplib, ssl
from devsendez.mcred import address, user, pwd
from email.message import EmailMessage

def isValidData(data):
    '''
    Checks to make sure data contains correct keys
    
    Parameters:
        data (dict)

        
    Returns: True if data contains correct keys below, False if it doesn't
            data['recipient']: email address of recipient
            data['senderName']: name of the sender to appear at the end of email message
            data['senderEmail']: email address to appear at the end of email message
            data['subject']: subject of the email
            data['message']: content of the email
    '''

    for key in data.keys():
        if key != 'html' && key not in data:
            return False
    return True
    
def sendEmail(data):
    '''
    Sends message to recipient from user using smtp server in mcred.py
    
    Parameters:
        data (dict) with key value pairs:
            data['recipient']: email address of recipient
            data['senderName']: name of the sender to appear at the end of email message
            data['senderEmail']: email address to appear at the end of email message
            data['subject']: subject of the email
            data['message']: content of the email
    
    Returns: isSent as true if email is sent and false if not
    '''
    
    isSent = True
    port = 587
    context = ssl.create_default_context()
    server = smtplib.SMTP(address, port)
    message = prepMessage(data)
    
    try:
        server.starttls(context=context)
        server.login(user, pwd)
        server.send_message(message)
      
    except Exception as e:
        isSent=False
    
    finally: 
        server.quit()    
    
    return isSent

   
def prepMessage(data):
    '''
    Prepares email by assigning data passed to EmailMessage object attributes
    
    Parameters: 
        data (dict) with key value pairs:
            data['recipient']: email address of recipient
            data['senderName']: name of the sender to appear at the end of email message
            data['senderEmail']: email address to appear at the end of email message
            data['subject']: subject of the email
            data['message']: content of the email
        Requires mcred.py file with appropriate credentials for user
        
        
    Returns: EmailMessage Object
    '''
    footer = f'\n\nThis message was sent by Dev Send EZ on behalf of {data['senderName']} at {data['senderEmail']}'
    htmlFooter = f'This message was sent by Dev Send EZ on behalf of {data['senderName']} at <a href="mailto:{senderEmail}">{data['senderEmail']}</a>'
    message = EmailMessage()
    message['To'] = data['recipient']
    message['From'] = user
    message['Subject'] = data['subject']
    message.set_content(data['text']+footer)    
    
    if 'html' in data:
        message.add_alternative(data['html']+htmlFooter, subtype='html')
        
    return message