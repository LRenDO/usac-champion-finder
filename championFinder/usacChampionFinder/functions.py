# ----------------------------------------------------------------------------
# Functions
# Author: Ren Demeis-Ortiz
# Description: This file contains helper functions
# ----------------------------------------------------------------------------


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

    print(resultsList)
    return resultsList