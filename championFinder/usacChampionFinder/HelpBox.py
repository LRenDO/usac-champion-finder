# ----------------------------------------------------------------------------
# HelpBox Class
# Author: Ren Demeis-Ortiz
# Description: This file contains the HelpBox class definitions.
# Sources: https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# ----------------------------------------------------------------------------
from tkinter import *

class HelpBox:
    '''
    Creates a small label with question mark that shows a box with text on
        mouse hover.
    
    Parameters: text (str), main (Frame object)
    '''

    def __init__(self, text, main):
        self.text = text
        self.main = main
        self.label = Label(main, text = '?', font=('Arial',9, 'bold'), padx=0, pady=1, bd=1, relief='groove')    
        self.textBox = Label(main, text = text, font=('Arial',12), padx=3, pady=4, justify='left')


        
        self.label.bind('<Enter>', self.__onEnter)
        self.label.bind('<Leave>', self.__onLeave)
        
    def __onEnter(self, event):
        '''
        Adds box with text on mouse hover
        '''
        self.textBox.grid(row=0, column=1, columnspan=3, pady=(20,0), padx=(0,0),sticky=NW)
        
    def __onLeave(self, event):
        '''
        Removes box with text when mouse moves out of label
        '''
        self.textBox.grid_forget()