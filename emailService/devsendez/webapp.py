# ----------------------------------------------------------------------------
# Dev Send EZ Server Routes
# Author: Ren Demeis-Ortiz
# Description: Handles post requests with JSON data to the server.
#              Data sent should be in JSON and must have the following
#              attributes: recipient, senderName,senderEmail, subject, text, 
#              html
# Source: https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
# ----------------------------------------------------------------------------

from flask import Flask, request, redirect
from devsendez.sendEmail import sendEmail
import json

webapp = Flask(__name__)

@webapp.route('/', methods=['POST'])
def prepSend():
    #print(request)
    #Process Request Data
    data = request.get_json()
    print(data) #DELETE

    #Send Email
    sendEmail(data['recipient'], data['senderName'], data['senderEmail'], data['subject'], data['text'], data['html'])
    #DELETE sendEmail('demeisol@oregonstate.edu', 'me', 'test@test.com', 'testing', 'test message body', "<!DOCTYPE html><html><body><h1>Test Header</h1></body></html>")
    
    return ('it worked')