# ----------------------------------------------------------------------------
# USA Climbing Champion Finder App
# Author: Ren Demeis-Ortiz
# Description: App that allows users to search for USA Climbing Champions 
#              based off of USA Climbing results.  Uses Spencer Neukam's 
#              USA Climbing Champions API. OSU VPN requried for API connection.
# Sources:https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
# ----------------------------------------------------------------------------
from tkinter import *
from usacChampionFinder.functions import *
from usacChampionFinder.HelpBox import HelpBox

def app(goldList):
    # -----------
    # Set Up Window and Frames
    # -----------
    root = Tk()
    root.geometry('1100x800')
    topFrame = Frame(root, bg='gray')
    bottomFrame = Frame(root, bg='gray', pady =20, height=400)
    years = createYearList(2004,2020)  # List of years to check
    resultDisp = yearSearch(years[len(years)-1], topFrame)  # Results frame object
    medalFrame = Frame(topFrame, bg='gray')  # Frame with medal results
    titleBar = Label(root, text = 'USA Climbing Champion Finder', font=('Arial','40'), pady=20, padx=50)
    
    # -----------
    # Year Search Section
    # -----------
    yearSearchLabel = Label(bottomFrame, text = 'Find Champion by Year:', font=('Arial',14),  justify='right', bg='gray', fg='white')


    # Dropdown Option Menu Sources: 
    #         https://www.geeksforgeeks.org/dropdown-menus-tkinter/
    #         https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
    selection = StringVar()
    selection.set('Choose a Year')
    dropdown = OptionMenu(bottomFrame, selection, *years)
    dropdown.config(bg='white', width=20)
    dropdown['menu'].config(bg='white')

    # Help Box Source: 
    #          https://stackoverflow.com/questions/4174575/adding-padding-to-a-tkinter-widget-only-on-one-side
    text = ''
    with open('usacChampionFinder/yearHelp.txt') as file:
        content = file.readlines()
    for line in content:
        text = text + line
    help = HelpBox(text, bottomFrame)
    
    topSearchB = Button(bottomFrame, text = 'Search', font=('Arial', 10), bg='red', fg='white', command= lambda: yearSearch(selection.get(), topFrame, resultDisp))

    # -----------
    # Name Search Section
    # -----------
    nameSearchLabel = Label(bottomFrame, text = 'Find Total Gold Medals by Name:', font=('Arial',14),  justify='right', bg='gray', fg='white')


    # Dropdown Option Menu Sources: 
    #         https://www.geeksforgeeks.org/dropdown-menus-tkinter/
    #         https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
    names = list(goldList.keys())
    names.sort()
    nameSelection = StringVar()
    nameSelection.set('Choose a Champion')
    nameDropdown = OptionMenu(bottomFrame, nameSelection, *names)
    nameDropdown.config(bg='white', width=20)
    nameDropdown['menu'].config(bg='white')

    # Help Box Source: 
    #          https://stackoverflow.com/questions/4174575/adding-padding-to-a-tkinter-widget-only-on-one-side
    text = ''
    with open('usacChampionFinder/nameHelp.txt') as file:
        content = file.readlines()
    for line in content:
        text = text + line
    nameHelp = HelpBox(text, bottomFrame)
    
    nameSearchB = Button(bottomFrame, text = 'Search', font=('Arial', 10), bg='red', fg='white', command= lambda: nameSearch(nameSelection.get(), goldList[nameSelection.get()], topFrame, medalFrame))

    # -----------
    # Pack Sections and Run GUI
    # -----------
    titleBar.grid(row=0, column=0,sticky=EW)
    topFrame.grid(row=1, column=0,sticky=EW)
    yearSearchLabel.grid(row=0, column=0, padx=(10,0), sticky=NE)
    help.label.grid(row=0, column=1, pady=(0, 20), sticky=NW)
    dropdown.grid(row=0, column=2, padx=(20,10), sticky=N)
    topSearchB.grid(row=0, column=3, padx=(15,5), sticky=N)
    nameSearchLabel.grid(row=1, column=0, padx=(10,0), sticky=N)
    nameHelp.label.grid(row=1, column=1, pady=(0, 20), sticky=NW)
    nameDropdown.grid(row=1, column=2, padx=(20,10), sticky=N)
    nameSearchB.grid(row=1, column=3, padx=(15,5), sticky=N)
    medalFrame.grid(row=4, column=0, columnspan=5, sticky=NSEW)
    bottomFrame.grid(row=2, column=0, columnspan='4', sticky=NSEW)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)


    root.mainloop()