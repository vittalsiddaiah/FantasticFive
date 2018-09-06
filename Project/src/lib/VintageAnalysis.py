##############################################################################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
##############################################################################


class VintageAnalysis:
    """
    Author: vittal.siddaiah@gmail.com
    Project: Wine Review Analysis
    Group: FantasticFive
    """
    wineDF = pd.DataFrame()
    wineDF_100 = pd.DataFrame()
    wineDF_300 = pd.DataFrame()
    outputFolder = "./"
    ##############################################################################

    def __init__(self, inputDataDF, outputDir):
        self.wineDF = inputDataDF
        self.outputFolder = outputDir
        return

    ##############################################################################

    def Compute(self):
        yearGrouped = self.wineDF.groupby(['Year'])
        medianYearScore = yearGrouped['points'].median()
        medianYearPrice = yearGrouped['price'].median()
        pointCount = yearGrouped['points'].count()
        yearDF = pd.DataFrame({
            'Median Wine Score': medianYearScore,
            'Median Wine Price': medianYearPrice,
            'Point Count': pointCount
        })
        # Drop regions with less than 300 wines reviewed for the bar plots and less than 100 wines reviewed for the scatter plot
        self.wineDF_100 = yearDF[yearDF['Point Count'] > 300].reset_index()
        self.wineDF_300 = yearDF[yearDF['Point Count'] > 100].reset_index()
        return

    ##############################################################################

    ##############################################################################

    def RenderPlot(self):
        # Plot scores
        plt.figure()
        self.wineDF_100.plot.bar(x='Year',
                                    y='Median Wine Score',
                                    figsize=(20, 5),
                                    yticks=np.arange(80, 100, 2),
                                    ylim=(80, 100),
                                    legend=False)
        plt.xlabel('Year')
        plt.ylabel('Median Wine Score')
        plt.title('Median Wine Score per Year (Over 300 Wines Reviewed)')
        plt.savefig(self.outputFolder + 'WineVintageVsScores.png')
        plt.grid(True)
        plt.show()

        # Plot Prices
        plt.figure()
        self.wineDF_300.plot.bar(x='Year',
                                    y='Median Wine Price',
                                    figsize=(20, 5),
                                    legend=False)
        plt.xlabel('Year')
        plt.ylabel('Median Wine Price')
        plt.title('Median Wine Price per Year (Over 300 Wines Reviewed)')
        plt.savefig(self.outputFolder + 'WineVintageVsPrice.png')
        plt.grid(True)
        plt.show()
        return
##############################################################################

