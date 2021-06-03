# ----------------------------------------------------------------------------
# USA Climbing Champion Finder App
# Author: Ren Demeis-Ortiz
# Description: Runs Desktop App that allows users to search for USA Climbing 
#              champions.
# ----------------------------------------------------------------------------
from usacChampionFinder.app import app
from usacChampionFinder.functions import processData
    
def main():
    dataByYear = {}
    goldList = {}
    processData(goldList, dataByYear)
    app(goldList, dataByYear)

if __name__ == '__main__':
    main()