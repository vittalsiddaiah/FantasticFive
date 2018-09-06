##############################################################################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
##############################################################################


class WineryPriceVsScore:
    """
    Author: alexis.filimonova@gmail.com
    Project: Wine Review Analysis
    Group: FantasticFive
    """
    wineDF = pd.DataFrame()
    processedDF = pd.DataFrame()
    outputFolder = "./"
    ##############################################################################

    def __init__(self, inputDataDF, outputDir):
        self.wineDF = inputDataDF
        self.outputFolder = outputDir
        return

    ##############################################################################

    def Compute(self):
        winery_group = self.wineDF.groupby(["winery"])
        winery_average_score = winery_group["points"].mean()
        winery_average_price = winery_group["price"].mean()
        winery_count = winery_group["points"].count()

        winery_df = pd.DataFrame(
            {"Winery average score": winery_average_score, "Winery average price": winery_average_price,
             "Wines by winery": winery_count})

        # Remove from calculations wineries with less than 100 wines reviewed
        self.processedDF = winery_df[winery_df["Wines by winery"] > 100].reset_index()
        winery_df.head()
        return

    ##############################################################################
    def RenderPlot(self):
        winery_df_100 = self.processedDF
        winery_df_100.plot.bar(x="winery", y="Winery average score", figsize=(20, 5), yticks=np.arange(80, 100, 2),
                               ylim=(80, 100), legend=False)
        plt.xlabel("Winery")
        plt.ylabel("Average wine score")
        plt.title("Average wine score per winery with over 100 wines reviewed")
        plt.tight_layout()
        plt.savefig(self.outputFolder + "Average_wine_scores.png")
        plt.show()

        # Plot prices
        winery_df_100.plot.bar(x="winery", y="Winery average price", figsize=(20, 5), legend=False, rot=90)
        plt.xlabel("Winery")
        plt.ylabel("Average wine price")
        plt.title("Average wine price per winery with over 100 wines reviewed")
        plt.tight_layout()
        plt.savefig(self.outputFolder + "Average_wine_prices.png")
        plt.show()

        # Create a scatter plot to show the correlation between average scores and average prices per winery
        plt.scatter(winery_df_100["Winery average score"], winery_df_100["Winery average price"])
        plt.xlabel("Wine score")
        plt.ylabel("Wine price")
        plt.title("Average wine prices per score")
        plt.tight_layout()
        plt.savefig(self.outputFolder + "Prices_scores_correlation.png")
        plt.show()


        return