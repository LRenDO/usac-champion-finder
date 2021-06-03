# ----------------------------------------------------------------------------
# Functions
# Author: Ren Demeis-Ortiz
# Description: This file contains helper functions for the USA Climbing
#           Champion Finder App.
# ----------------------------------------------------------------------------
from tkinter import *
from usacChampionFinder.Query import Query
from usacChampionFinder.ResultsFrame import ResultsFrame

def createYearList(start, end):
    '''
    Creates a list of years starting with start and ending with end
    
    Parameters:
        start (int) first year to be included in list
        end (int) Last year to be included in list
 
    Returns: List of years between start and end date
    '''
    startYear = start
    endYear = end
    years=[]
    while startYear <= endYear:
        years.append(startYear)
        startYear += 1
    return years
    

def getGoldMedalists(results):
    '''
    Processes the results from a dict to list of gold medal winners
    
    Parameters:
        results (list) list of results

    Returns: Returns gold medal winners for the year in order of
            Women's Bouldering, Men's Bouldering, Women's Sport, 
            Men's Sport, Women's Speed, Men's Speed
    '''
    resultsList=[]
    
    for i in range(len(results)):
        if type(results[i]) is str:
            resultsList.append('Not Listed')
        else:
            resultsList.append(results[i]['gold'])

    return resultsList
    
  
def yearSearch(selection, main, resultDisp=None):
    '''
    Sends query and processes and displays results of search by year function
    
    Parameters:
        selection (int) year passed for query
        main (frame) parent frame for resultDisp to be packed into
        resultDisp (frame) frame for results to be packed into

    Returns: Returns frame that results are displayed in
    '''
    
    args = prepQueryArgs(selection)
    newQuery = Query('http://flip3.engr.oregonstate.edu:6742/api/usa-climbing', args)
    response = newQuery.sendRequest()
    
    results = getGoldMedalists(response)

    if resultDisp is not None:
        resultDisp = displayYearResults(results, selection, main, resultDisp)
    else:
        resultDisp = displayCurrentChampions(results, selection, main)
        
    return resultDisp

def nameSearch(selection, goldMedals, main, medalFrame=None):
    '''
    Displays search parameter and number of medals
    
    Parameters:
        selection (str) name of champion selected
        goldMedals (int) number of gold medals selected champion won
        main (frame) parent frame for medalFrame to be packed into
        medalFrame (frame) frame for results to be packed into

    Returns: Returns frame that results are displayed in
    '''
    if medalFrame is not None:
        medalFrame.grid_forget()
        
    medalText = selection+" has won "+str(goldMedals)+" gold medals"
    topBorder = Label(medalFrame, text="Results for "+selection, font=('Arial',20), bg='gray', fg='white')
    nameResultLabel = Label(medalFrame, text = medalText, font=('Arial',12), bg='blue', fg='white')
    topBorder.grid(row=0, column=0, sticky=NSEW, pady=(5,0))
    nameResultLabel.grid(row=1, column=0, sticky=NSEW)
    medalFrame.grid(row=6, column=0, columnspan=5, sticky=NSEW) 
    medalFrame.grid_columnconfigure(0, weight=1)
    
    return medalFrame 
    
def displayCurrentChampions(results, selection, main):
    '''
    Parameters:
        selection (int) year passed for query
        main (frame) parent frame for resultDisp to be packed into   

    Returns:  Returns frame that results are displayed in
    '''
    resultDisp = ResultsFrame(results, selection, main)
    resultDisp.packFrame()
    
    return resultDisp
    
    
def displayYearResults(results, selection, main, resultDisp):
    '''
    Parameters:
        selection (int) year passed for query
        main (frame) parent frame for resultDisp to be packed into
        resultDisp (frame) frame for results to be packed into    

    Returns: Returns frame that results are displayed in
    '''
    resultDisp.end()
    resultDisp.update(results, selection, main)
    resultDisp.packFrame()
    
    return resultDisp
    

def prepQueryArgs(selection):
    '''
    Prepares get request arguments  to send to API
    
    Parameters:
        selection (int) year passed for query
    

    Returns: Returns list of results for each discipline and category
    '''
    
    boulderingKey = 'Bouldering Open National Championships'
    sportKey = 'Sport Lead Open National Championships'
    speedKey = 'Speed Open National Championships'
    event = [boulderingKey, sportKey, speedKey]
    category = ['Female', 'Male']
    args = []
    for i in range(len(event)):
        for j in range(len(category)):
            args.append({'event':event[i], 'category': category[j], 'year':selection})
            
    return args
    
    
def processData(goldList, dataByYear):
    '''
    Requests saves and processes all data for better performance
    
    Parameters:
        goldList (dict) champions and number of medals won
        dataByYear (dict) to store year and medal winners for all 3 events

    Returns: 
    '''

    saveData(dataByYear)
    countMedals(goldList, dataByYear)
    
    return 
    
def saveData(dataByYear):
    '''
    Requests all data and saves into dict passed as parameter
    
    Parameters:
        dataByYear (dict) to store year and medal winners for all 3 events

    Returns: 
    '''
    for i in createYearList(2004,2020):
        args = prepQueryArgs(i)
        newQuery = Query('http://flip3.engr.oregonstate.edu:6742/api/usa-climbing', args)
        results = newQuery.sendRequest()
        
        dataByYear[i] = results
        
        
def countMedals(goldList, dataByYear):
    '''
    Counts gold medals 
    
    Parameters:
        goldList (dict) champions and number of medals won
        dataByYear (dict) to store year and medal winners for all 3 events

    Returns: 
    '''
    for year in dataByYear:
        for i in range(len(dataByYear[year])):
            if dataByYear[year][i] != 'ERROR: Invalid year':
                if dataByYear[year][i]['gold'] in goldList:
                    goldList[dataByYear[year][i]['gold']] += 1
                else:
                    goldList[dataByYear[year][i]['gold']] = 1
    
    return 

  
