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
        self.frame = Frame(main)
        
        # Title Frame
        self.titleFrame = Frame(main)
        
        # Column Frames
        frameAtts = {'bg':'white', 'bd':1}
        self.leftFrame = Frame(main, **frameAtts)
        self.centerFrame = Frame(main, **frameAtts)
        self.rightFrame = Frame(main, **frameAtts)

        # Labels
        headAtts = {'font':('Arial',12),  'bg':'blue', 'fg':'white', 'width':40}
        labelAtts = {'font':('Arial',10),  'bg':'blue', 'fg':'white', 'width':40}
        self.resultsTitle = Label(self.titleFrame, text = 'Results for '+self.year, font=('Arial',20),  bg='gray', fg='white')
        self.left = Label(self.leftFrame, text='Bouldering', **headAtts)
        self.center = Label(self.centerFrame, text='Sport', **headAtts)
        self.right = Label(self.rightFrame, text='Speed', **headAtts)
        self.left1 = Label(self.leftFrame, text= self.bouldering['Female'], **labelAtts)
        self.left2 = Label(self.leftFrame, text = self.bouldering['Male'], **labelAtts)
        self.center1 = Label(self.centerFrame, text = self.sport['Female'], **labelAtts)
        self.center2 = Label(self.centerFrame, text = self.sport['Male'], **labelAtts)
        self.right1 = Label(self.rightFrame, text = self.speed['Female'], **labelAtts)
        self.right2 = Label(self.rightFrame, text = self.speed['Male'], **labelAtts)

    def update(self, results, year, main):
        '''
        Updates Attributes
        '''        
        self.bouldering = {'Female': results[0], 'Male': results[1]}
        self.sport = {'Female': results[2], 'Male': results[3]}
        self.speed = {'Female': results[4], 'Male': results[5]}
        self.year = str(year)
        self.main = main
        self.frame = Frame(main)
        
        # Title Frame
        self.titleFrame = Frame(main)
        
        # Column Frames
        frameAtts = {'bg':'white', 'bd':1}
        self.leftFrame = Frame(main, **frameAtts)
        self.centerFrame = Frame(main, **frameAtts)
        self.rightFrame = Frame(main, **frameAtts)

        # Labels
        headAtts = {'font':('Arial',12),  'bg':'blue', 'fg':'white', 'width':40}
        labelAtts = {'font':('Arial',10),  'bg':'blue', 'fg':'white', 'width':40}
        self.resultsTitle = Label(self.titleFrame, text = 'Results for '+self.year, font=('Arial',20),  bg='gray', fg='white')
        self.left = Label(self.leftFrame, text='Bouldering', **headAtts)
        self.center = Label(self.centerFrame, text='Sport', **headAtts)
        self.right = Label(self.rightFrame, text='Speed', **headAtts)
        self.left1 = Label(self.leftFrame, text= self.bouldering['Female'], **labelAtts)
        self.left2 = Label(self.leftFrame, text = self.bouldering['Male'], **labelAtts)
        self.center1 = Label(self.centerFrame, text = self.sport['Female'], **labelAtts)
        self.center2 = Label(self.centerFrame, text = self.sport['Male'], **labelAtts)
        self.right1 = Label(self.rightFrame, text = self.speed['Female'], **labelAtts)
        self.right2 = Label(self.rightFrame, text = self.speed['Male'], **labelAtts) 
 
    def end(self):
        '''
        Removes Frame
        '''
        self.resultsTitle.pack_forget()
        self.titleFrame.pack_forget()
        self.left.pack_forget()
        self.left1.pack_forget()
        self.left2.pack_forget()
        self.center.pack_forget()
        self.center1.pack_forget()
        self.center2.pack_forget()
        self.right.pack_forget()
        self.right1.pack_forget()
        self.right2.pack_forget()
        self.leftFrame.pack_forget()
        self.centerFrame.pack_forget()
        self.rightFrame.pack_forget()
        
    def packFrame(self):
        '''
        Packs sections into main
        '''
        resultArgs = {'side':'top', 'fill':'x'}
        self.resultsTitle.pack(**resultArgs)
        self.titleFrame.pack(**resultArgs)
        self.left.pack(side='top')
        self.left1.pack(**resultArgs)
        self.left2.pack(**resultArgs)
        self.center.pack(side='top')
        self.center1.pack(**resultArgs)
        self.center2.pack(**resultArgs)
        self.right.pack(side='top')
        self.right1.pack(**resultArgs)
        self.right2.pack(**resultArgs)
        self.leftFrame.pack(side='left')
        self.centerFrame.pack(side='left')
        self.rightFrame.pack(side='left')
