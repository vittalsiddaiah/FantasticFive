##############################################################################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
##############################################################################


class TypeVsScore:
    """
    Author: Jagan
    Project: Wine Review Analysis
    Group: FantasticFive
    """
    wineDF = pd.DataFrame()
    outputFolder = "./"
    ##############################################################################

    def __init__(self, inputDataDF, outputDir):
        self.wineDF = inputDataDF
        self.outputFolder = outputDir
        return

    ##############################################################################

    def Compute(self):
        # Create type of wine DF
        wine_type = self.wineDF.groupby(['variety'])
        average_price = wine_type['price'].mean()
        average_points = wine_type['points'].mean()
        region_count = wine_type['points'].count()

        wine_type_df = pd.DataFrame({
            'Average Price': average_price,
            'Average Points': average_points,
            'Wines in type': region_count
        })

        wine_type_df_100 = wine_type_df[wine_type_df['Wines in type'] > 99].reset_index()
        wine_type_df_300 = wine_type_df[wine_type_df['Wines in type'] > 299].reset_index()
        wine_type_df_1000 = wine_type_df[wine_type_df['Wines in type'] > 999].reset_index()

        plt.scatter(wine_type_df['Average Points'], wine_type_df['Average Price'],
                    color='red', edgecolor='white', alpha=.99)
        plt.xlabel('Wine Score')
        plt.ylabel('Wine Price')
        plt.title('Wine Prices Vs Wine Score')
        plt.tight_layout()
        plt.savefig(self.outputFolder +'winetypes-pirce-score.png')
        plt.grid()

        plt.show()

        plt.figure(figsize=(20, 10))
        plt.xlabel('Wine Score')
        plt.ylabel('Wine Price')
        plt.title('Wine Prices Vs Wine Score(1000 plus wines)')
        plt.tight_layout()
        plt.grid()
        for index, row in wine_type_df_1000.iterrows():
            plt.scatter(row['Average Points'], row['Average Price'], s=row['Wines in type'], alpha=.7)
            plt.annotate(row['variety'], xy=(row['Average Points'], row['Average Price']))

            plt.savefig(self.outputFolder + 'winetypes-pirce-score_1000.png')
        plt.show()

        # Plot Scores 300 plus wines
        wine_type_df_300.sort_values('Average Points').plot.bar(x='variety', y='Average Points', figsize=(20, 5),
                                                                legend=False, rot=90)
        plt.xlabel('Variety')
        plt.ylabel('Average Wine Score')
        plt.ylim(ymin=85)
        plt.ylim(ymax=91)
        plt.title('Average Wine Score per Variety (Over 300 Wines Reviewed)')
        plt.tight_layout()
        plt.savefig(self.outputFolder + 'Average_Wine_Scores_Variety_300.png')
        plt.show()

        # Plot Prices 300 plus wines
        wine_type_df_300.sort_values('Average Price').plot.bar(x='variety', y='Average Price', figsize=(20, 5),
                                                               legend=False, rot=90)
        plt.xlabel('Variety')
        plt.ylabel('Average Wine Price')
        plt.ylim(ymin=10)
        plt.title('Average Wine Price per Variety (Over 300 Wines Reviewed)')
        plt.tight_layout()
        plt.savefig(self.outputFolder + 'Average_Wine_Prices_Variety_300.png')
        plt.show()
        return

    ##############################################################################
    def RenderPlot(self):
        return