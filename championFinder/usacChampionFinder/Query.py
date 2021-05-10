# ----------------------------------------------------------------------------
# Query Class
# Author: Ren Demeis-Ortiz
# Description: This file contains the Query class definitions.
# ----------------------------------------------------------------------------
import requests

class Query:
    '''
    Represents queries to be sent via HTTP get request.
    
    Attributes: url (str), args (list of dicts), res (list of dicts)
    '''

    def __init__(self, url, args):
        self.url = url
        self.args = args
        self.resList = []


    def sendRequest(self):
        '''
        Sends get request to url attribute
    
        Returns: isSent as true if email is sent.
    
        Sources: https://www.datacamp.com/community/tutorials/making-http-requests-in-python
        '''
    
        #For each Discipline and Category Send Request and Add to Results List
        for i in range(len(self.args)):
            response = requests.get(self.url, params=self.args[i])
            self.resList.append(response.json()) 
    
        return self.resList