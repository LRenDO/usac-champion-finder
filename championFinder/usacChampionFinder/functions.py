# ----------------------------------------------------------------------------
# Functions
# Author: Ren Demeis-Ortiz
# Description: This file contains helper functions
# ----------------------------------------------------------------------------
import asyncio
from usacChampionFinder.Query import Query
from usacChampionFinder.ResultsFrame import ResultsFrame

# ----------------------------------------------------------------------------
# createYearList(start,end)
#
#   Parameters:
#       start (int) first year to be included in list
#       end (int) Last year to be included in list
#
#   Returns: List of years between start and end date
# ----------------------------------------------------------------------------
def createYearList(start, end):
    startYear = start
    endYear = end
    years=[]
    while startYear <= endYear:
        years.append(startYear)
        startYear += 1
    return years
    
# ----------------------------------------------------------------------------
# processResults(results)
#
#   Parameters:
#       results (list) list of results
#
#   Returns: Returns gold medal winners for the year in order of
#           Women's Bouldering, Men's Bouldering, Women's Sport, 
#           Men's Sport, Women's Speed, Men's Speed
# ----------------------------------------------------------------------------
def processResults(results):
    resultsList=[]
    
    for i in range(len(results)):
        if type(results[i]) is str:
            resultsList.append('Not Listed')
        else:
            resultsList.append(results[i]['gold'])

    return resultsList
    
# ----------------------------------------------------------------------------
# topSearch(selection, main, resultDisp)
#
#   Parameters:
#       selection (int) year passed for query
#       main (frame) frame for results to be packed into
#       resultDisp (listVar) variable where list will be stored
#
#   Returns: Returns list of results for each discipline and category
# ----------------------------------------------------------------------------    
def topSearch(selection, main, resultDisp=None):
    print('\nSending Requests')
    
    #Prepare Arguments
    event = ['Bouldering Open National Championships', 'Sport Lead Open National Championships', 'Speed Open National Championships']
    category = ['Female', 'Male']
    args = []
    for i in range(len(event)):
        for j in range(len(category)):
            args.append({'event':event[i], 'category': category[j], 'year':selection})
    print('list of queries: ',args)#DELETE
    
    #Send Request
    newQuery = Query('http://flip3.engr.oregonstate.edu:6742/api/usa-climbing', args)
    response = newQuery.sendRequest()
    print('\nraw results:', response) #DELETE
    
    #Process Results
    results = processResults(response)
    
    # Display Results
    if resultDisp is not None:
        resultDisp.end()
        resultDisp.update(results, selection, main)
        resultDisp.packFrame()
    else:
        resultDisp = ResultsFrame(results, selection, main)
        resultDisp.packFrame()
    
    return resultDisp