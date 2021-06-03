# ----------------------------------------------------------------------------
# Results Class
# Author: Ren Demeis-Ortiz
# Description: This file contains the ResultsFrame class definitions.
# Sources:https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
# ----------------------------------------------------------------------------
from tkinter import *

class ResultsFrame:
    '''
    Builds tkinter frame to display results
    
    Parameters: results (list), main (tkinter object)
    '''

    def __init__(self, results, year, main):
        self.bouldering = {'Female': results[0], 'Male': results[1]}
        self.sport = {'Female': results[2], 'Male': results[3]}
        self.speed = {'Female': results[4], 'Male': results[5]}
        self.year = str(year)
        self.main = main

        # Labels
        headAtts = {'font':('Arial',12),  'bg':'blue', 'fg':'white'}
        labelAtts = {'font':('Arial',10),  'bg':'blue', 'fg':'white'}
        
        self.resultsTitle = Label(self.main, text = 'Results for '+self.year, font=('Arial',20),  bg='gray', fg='white')
       
        # Left Column          
        self.left = Label(self.main, text='Bouldering', **headAtts)     
        self.left1 = Label(self.main, text= self.bouldering['Female'], **labelAtts)
        self.left2 = Label(self.main, text = self.bouldering['Male'], **labelAtts)
        
        # Center Column        
        self.center = Label(self.main, text='Sport', **headAtts)
        self.center1 = Label(self.main, text = self.sport['Female'], **labelAtts)
        self.center2 = Label(self.main, text = self.sport['Male'], **labelAtts)
        
        # Right Column
        self.right = Label(self.main, text='Speed', **headAtts)
        self.right1 = Label(self.main, text = self.speed['Female'], **labelAtts)
        self.right2 = Label(self.main, text = self.speed['Male'], **labelAtts)
        
        # Borders
        self.borderL = Label(self.main, bg='gray', bd=.1)
        self.borderR = Label(self.main, bg='gray', bd=.1)
        
        
    def update(self, results, year, main):
        '''
        Updates Attributes
        '''        
        self.bouldering = {'Female': results[0], 'Male': results[1]}
        self.sport = {'Female': results[2], 'Male': results[3]}
        self.speed = {'Female': results[4], 'Male': results[5]}
        self.year = str(year)
        self.main = main
        
        # Labels
        headAtts = {'font':('Arial',12),  'bg':'blue', 'fg':'white'}
        labelAtts = {'font':('Arial',10),  'bg':'blue', 'fg':'white'}
        
        self.resultsTitle = Label(self.main, text = 'Results for '+self.year, font=('Arial',20),  bg='gray', fg='white')
       
        # Left Column          
        self.left = Label(self.main, text='Bouldering', **headAtts)     
        self.left1 = Label(self.main, text= self.bouldering['Female'], **labelAtts)
        self.left2 = Label(self.main, text = self.bouldering['Male'], **labelAtts)
        
        # Center Column        
        self.center = Label(self.main, text='Sport', **headAtts)
        self.center1 = Label(self.main, text = self.sport['Female'], **labelAtts)
        self.center2 = Label(self.main, text = self.sport['Male'], **labelAtts)
        
        # Right Column
        self.right = Label(self.main, text='Speed', **headAtts)
        self.right1 = Label(self.main, text = self.speed['Female'], **labelAtts)
        self.right2 = Label(self.main, text = self.speed['Male'], **labelAtts)
        
        # Borders
        self.borderL = Label(self.main, bg='gray', bd=.1)
        self.borderR = Label(self.main, bg='gray', bd=.1)
        
        
    def end(self):
        '''
        Removes grid
        '''
        self.resultsTitle.grid_forget()
        
        # Left Column
        self.left.grid_forget()
        self.left1.grid_forget()
        self.left2.grid_forget()
        
        # Center Column        
        self.center.grid_forget()
        self.center1.grid_forget()
        self.center2.grid_forget()
        
        # Right Column       
        self.right.grid_forget()
        self.right1.grid_forget()
        self.right2.grid_forget()

        # Borders        
        self.borderL.grid_forget()
        self.borderR.grid_forget()

        
    def packFrame(self):
        '''
        Packs labels into main grid
        '''
        self.resultsTitle.grid(row=0, column=0, columnspan=5, pady=(5,0), sticky=NSEW)
        
        # Left Column
        self.left.grid(row=1, column=0, sticky=NSEW)
        self.left1.grid(row=2, column=0, sticky=NSEW)
        self.left2.grid(row=3, column=0, sticky=NSEW)

        
        # Center Column
        self.center.grid(row=1, column=2, sticky=NSEW)
        self.center1.grid(row=2, column=2, sticky=NSEW)
        self.center2.grid(row=3, column=2, sticky=NSEW)
        
        # Right Column
        self.right.grid(row=1, column=4, sticky=NSEW)
        self.right1.grid(row=2, column=4, sticky=NSEW)
        self.right2.grid(row=3, column=4, sticky=NSEW)
        
        # Borders
        self.borderL.grid(row=1, column=1, rowspan=3, sticky=NSEW)         
        self.borderR.grid(row=1, column=3, rowspan=3, sticky=NSEW) 
        
        # Configure Column Responsiveness (weigth)
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_columnconfigure(2, weight=1)
        self.main.grid_columnconfigure(4, weight=1)
        self.main.grid_rowconfigure(2, weight=1)