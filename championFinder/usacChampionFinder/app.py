# ----------------------------------------------------------------------------
# USA Climbing Champion Finder App
# Author: Ren Demeis-Ortiz
# Description: GUI that allows users to search for USA Climbing Champions 
#              based off of USA Climbing results.  Uses Spencer Neukam's 
#              USA Climbing Champions API.
# Sources:https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
# ----------------------------------------------------------------------------
from tkinter import *
from usacChampionFinder.Query import Query
from usacChampionFinder.functions import *
from usacChampionFinder.ResultsFrame import ResultsFrame
    
years = createYearList(2004,2020)

def topSearch(selection, main, resultDisp=None):
    print('Sending Requests')
    
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
    print('resultDisp:', resultDisp) #DELETE
    if resultDisp is not None:
        resultDisp.end()
        resultDisp.update(results, main)
        resultDisp.packFrame()
    else:
        resultDisp = ResultsFrame(results, main)
        resultDisp.packFrame()
    
    return resultDisp

# -----------
# Set Up Window and Frames
# -----------
root = Tk()
#root.config(bg='white')
topFrame = Frame(root, bg='white')
bottomFrame = Frame(root, bg='gray', pady =20)
resultDisp = topSearch(years[len(years)-1], topFrame)

# -----------
# Titles
# -----------
titleBar = Label(root, text = 'USA Climbing Champion Finder', font=('Arial','40'), pady=20, padx=50)
resultsTitle = Label(root, text = 'Results', font=('Arial',20),  bg='gray', fg='white')

# -----------
# Search Section
# -----------
leftSide = Label(bottomFrame, text = 'Find Champion by Year:', font=('Arial',12),  justify='right', bg='gray', fg='white', padx=5)


#Dropdown Menu
#Sources: https://www.geeksforgeeks.org/dropdown-menus-tkinter/
#         https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
selection = StringVar()
selection.set('Choose a Year')
dropdown = OptionMenu(bottomFrame, selection, *years)
dropdown.config(bg='white')
dropdown['menu'].config(bg='white')

#Top Search Button
topSearchB = Button(bottomFrame, text = 'Search', bg='red', fg='white', command= lambda: topSearch(selection.get(), topFrame, resultDisp))

# -----------
# Pack Sections and Run GUI
# -----------
titleBar.pack()
resultsTitle.pack(side='top', fill='x')
topFrame.pack(side='top',fill='x')
leftSide.pack(side='left')
dropdown.pack(side='left', padx=5)
topSearchB.pack(side='left', padx=5)
bottomFrame.pack(side='bottom', fill='x')


root.mainloop()
