# ----------------------------------------------------------------------------
# Query Class
# Author: Ren Demeis-Ortiz
# Description: This file contains the Query class definitions.
# Sources: https://www.youtube.com/watch?v=nFn4_nA_yk8
# ----------------------------------------------------------------------------
import asyncio
import aiohttp

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
        Starts async requests
    
        Returns: List of responses
        '''
        asyncio.run(self.__sendRequests())
        
        return self.resList
            
    async def __sendRequests(self):
        '''
        Sends get request to url attribute
        '''
        async with aiohttp.ClientSession() as session:
            tasks = self.__getTasks(session)
            responses = await asyncio.gather(*tasks)
            
            for res in responses:
                self.resList.append(await res.json())
            
            return
            
    def __getTasks(self, session):
        '''
        Sends get request for each set of arguments in self.args
        
        Returns: list of responses
        '''
        tasks=[]
        
        for i in range(len(self.args)):
            tasks.append(session.request('get', self.url, params=self.args[i]))
        
        return tasks
        