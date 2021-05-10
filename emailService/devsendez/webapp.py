# ----------------------------------------------------------------------------
# Dev Send EZ Server Routes
# Author: Ren Demeis-Ortiz
# Description: Handles post requests with JSON data to the server.
#              Data sent should be in JSON and must have the following
#              attributes: recipient, senderName,senderEmail, subject, text, 
#              html
# Sources: https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
#          https://stackoverflow.com/questions/45412228/sending-json-and-status-code-with-a-flask-response
# ----------------------------------------------------------------------------

from flask import Flask, request, redirect, jsonify
from devsendez.sendEmail import sendEmail

webapp = Flask(__name__)

@webapp.route('/', methods=['POST'])
def prepSend():
    #Process Request Data
    data = request.get_json()
    isSent = False
    response = {'Status':'error'}

    if 'recipient' in data and 'senderName' in data and 'senderEmail' in data and 'subject' in data and 'text' in data:
        #Send Email
        if 'html' in data:
            isSent = sendEmail(data['recipient'], data['senderName'], data['senderEmail'], data['subject'], data['text'], data['html'])
        else:
            isSent = sendEmail(data['recipient'], data['senderName'], data['senderEmail'], data['subject'], data['text'])
    else:    
        response = {'Status':'invalid request format error'}
    
    if isSent:
        response = {'Status':'sent'}  
    
    
    return jsonify(response)