##############################################################################
from lib.ReadNCleanData import ReadNCleanData
from lib.RegionScore import RegionScore
from lib.VintageAnalysis import VintageAnalysis
from lib.TypeVsScore import TypeVsScore
from lib.RegionRating import RegionRating
from lib.WineryPriceVsScore import WineryPriceVsScore
from lib.Timer import Timer
import os
##############################################################################

##############################################################################
def main():
    timer = Timer("Wine Review Analysis Completed in ")
    print("Wine Review Analysis")
    inputFile = r"../Data/winemag-data-130k-v2.csv"
    if os.path.isfile(inputFile) and os.access(inputFile, os.R_OK):
        print("File exists and is readable")
    else:
        print("Either the file is missing or not readable")

    print("Parsing Wine Data ...: ", inputFile)

    wineDF = ReadNCleanData().Get(inputFile)

    outputDir = "./images/"

    print("Computing Scores Please wait ...")
    regionDF = RegionScore(wineDF, outputDir)
    regionDF.Compute()
    regionDF.RenderPlot()

    vintageDF = VintageAnalysis(wineDF, outputDir)
    vintageDF.Compute()
    vintageDF.RenderPlot()

    typeVsScore = TypeVsScore(wineDF, outputDir)
    typeVsScore.Compute()

    regionRating = RegionRating(wineDF, outputDir)
    regionRating.Compute()

    winePriceVsScore = WineryPriceVsScore(wineDF, outputDir)
    winePriceVsScore.Compute()
    winePriceVsScore.RenderPlot()

    print("Computing Region Scores ...: DONE")
    print(timer.delta_str())

    #Cleanup from Memory
    regionDF = None
    vintageDF = None
    typeVsScore = None
    regionRating = None
    winePriceVsScore = None
##############################################################################

main()