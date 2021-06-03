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
from devsendez.functions import *

webapp = Flask(__name__)

@webapp.route('/', methods=['POST'])
def prepSend():
    data = request.get_json()
    isSent = False
    response = {'Status':'error'}

    if isValidData(data):
         isSent = sendEmail(data)

    else:    
        response = {'Status':'invalid request format error'}
    
    if isSent:
        response = {'Status':'sent'}  
    
    
    return jsonify(response)