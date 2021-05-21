# ----------------------------------------------------------------------------
# USA Climbing Champion Finder App
# Author: Ren Demeis-Ortiz
# Description: GUI that allows users to search for USA Climbing Champions 
#              based off of USA Climbing results.  Uses Spencer Neukam's 
#              USA Climbing Champions API.
# Sources:https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
# ----------------------------------------------------------------------------
from tkinter import *
from usacChampionFinder.functions import *
from usacChampionFinder.HelpBox import HelpBox
    


def app():
    print('in app')
    # -----------
    # Set Up Window and Frames
    # -----------
    years = createYearList(2004,2020)
    root = Tk()
    #root.config(bg='white')
    topFrame = Frame(root, bg='white')
    bottomFrame = Frame(root, bg='gray', pady =20)
    resultDisp = topSearch(years[len(years)-1], topFrame)

    # -----------
    # Title
    # -----------
    titleBar = Label(root, text = 'USA Climbing Champion Finder', font=('Arial','40'), pady=20, padx=50)
    
    # -----------
    # Search Section
    # -----------
    leftSide = Label(bottomFrame, text = 'Find Champion by Year:', font=('Arial',14),  justify='right', bg='gray', fg='white')


    #Dropdown Menu
    #Sources: https://www.geeksforgeeks.org/dropdown-menus-tkinter/
    #         https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
    selection = StringVar()
    selection.set('Choose a Year')
    dropdown = OptionMenu(bottomFrame, selection, *years)
    dropdown.config(bg='white', width=20)
    dropdown['menu'].config(bg='white')

    #Help Box
    #Source: https://stackoverflow.com/questions/4174575/adding-padding-to-a-tkinter-widget-only-on-one-side
    text = ''
    with open('usacChampionFinder/yearHelp.txt') as file:
        content = file.readlines()
    for line in content:
        text = text + line
    help = HelpBox(text, bottomFrame)
    
    #Top Search Button
    topSearchB = Button(bottomFrame, text = 'Search', font=('Arial', 10), bg='red', fg='white', command= lambda: topSearch(selection.get(), topFrame, resultDisp))

    # -----------
    # Pack Sections and Run GUI
    # -----------
    titleBar.pack()
    topFrame.pack(side='top',fill='x')
    #leftSide.pack(side='left')
    #dropdown.pack(side='left', padx=5)
    leftSide.grid(row=0, column=0, padx=(10,0), sticky=N)
    help.label.grid(row=0, column=1, pady=(0, 20), sticky=NW)
    #help.textBox.grid(row=1, column=1, columnspan=3, pady=(0,0), padx=(0,0),sticky=NW)
    dropdown.grid(row=0, column=2, padx=(20,10), sticky=N)
    topSearchB.grid(row=0, column=3, padx=(15,5), sticky=N)
    #topSearchB.pack(side='left', padx=5)
    bottomFrame.pack(side='bottom', fill='x')


    root.mainloop()