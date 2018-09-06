##############################################################################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
##############################################################################


class RegionScore:
    """
    Author: j.kaplan814@yahoo.com
    Project: Wine Review Analysis
    Group: FantasticFive
    """
    wineDF = pd.DataFrame()
    region_df_300 = pd.DataFrame()
    region_df_100 = pd.DataFrame()
    outputFolder = "./"
    ##############################################################################

    def __init__(self, inputDataDF, outputDir):
        self.wineDF = inputDataDF
        self.outputFolder = outputDir
        return

    ##############################################################################

    def Compute(self):
        region_group = self.wineDF.groupby(['region'])
        region_average_score = region_group['points'].mean()
        region_average_price = region_group['price'].mean()
        region_count = region_group['points'].count()
        region_df = pd.DataFrame({
            'Region Average Score': region_average_score,
            'Region Average Price': region_average_price,
            'Wines in Region': region_count
        })
        # Drop regions with less than 300 wines reviewed for the bar plots and less than 100 wines reviewed for the scatter plot
        self.region_df_300 = region_df[region_df['Wines in Region'] > 300].reset_index()
        self.region_df_100 = region_df[region_df['Wines in Region'] > 100].reset_index()
        return

    ##############################################################################

    ##############################################################################

    def RenderPlot(self):
        # Plot scores
        plt.figure()
        self.region_df_100.plot.bar(x='region', y='Region Average Score',
                                         figsize=(20, 5),
                                         yticks=np.arange(80, 100, 2),
                                         ylim=(80, 100), legend=False)
        plt.xlabel('Region')
        plt.ylabel('Average Wine Score')
        plt.title('Average Wine Score per Region (Over 300 Wines Reviewed)')
        plt.savefig(self.outputFolder + 'Average_Wine_Scores.png')
        plt.show()

        # Plot Prices
        plt.figure()
        self.region_df_300.plot.bar(x='region', y='Region Average Price', figsize=(20, 5), legend=False)
        plt.xlabel('Region')
        plt.ylabel('Average Wine Price')
        plt.title('Average Wine Price per Region (Over 300 Wines Reviewed)')
        plt.savefig(self.outputFolder + 'Average_Wine_Prices.png')
        plt.show()

        # Create scatter plot to show trend
        plt.figure()
        plt.scatter(self.region_df_100['Region Average Score'], self.region_df_100['Region Average Price'])
        plt.xlabel('Wine Score')
        plt.ylabel('Wine Price')
        plt.title('Wine Prices per Score')
        plt.savefig(self.outputFolder + 'Price_vs_Scores.png')
        plt.show()
        return
##############################################################################
