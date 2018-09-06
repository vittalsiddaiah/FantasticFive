##############################################################################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
##############################################################################


class RegionRating:
    """
    Author: varsharcn@gmail.com
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
        dropped_rows_list = self.wineDF[self.wineDF['country'].isnull()].index
        wine_df = self.wineDF.replace(np.nan, 'Unlisted', regex=True)
        wine_df.fillna("Unlisted")

        # Extract specific columns pertaining to analysis

        specific_columns = wine_df.loc[:, ["country", "province", "region", "points", "winery"]]

        specific_columns_df = specific_columns.rename(
            columns={"country": "Countries", "province": "Province", "region": "Appellation", "points": "Wine Rating",
                     "winery": "Winery"})
        country_province_specific = specific_columns.iloc[0:, [0, 1]]
        wine_rating_country = specific_columns_df.loc[:, ["Countries", "Wine Rating"]]
        wine_rating_province = specific_columns_df.loc[:, ["Province", "Wine Rating"]]

        # Wine rating grouped and counted by country
        wine_score_country = wine_rating_country.groupby(["Countries"]).count()
        wine_score_country_df = wine_score_country.rename(
            columns={"Countries": "Countries", "Wine Rating": "Total Wine Rating per Country"})

        # Use DataFrame.plot() in order to create a bar chart of the data
        wine_score_country.plot(kind="bar", color="g", figsize=(20, 10))

        # Set a title for the chart
        plt.title("Total Wine Rating by Country")

        plt.xlabel("Country")
        plt.ylabel("Total Points/Score")

        plt.savefig(self.outputFolder  +  'Total_Wine_Rating_byCountry.png')

        plt.show()
        plt.tight_layout()

        avg_wine_rating_country = wine_rating_country.groupby(["Countries"]).mean()

        # Repetition of Appellation/geographic regions within a Province in dataset (grouped and counted by province name)
        # implies 'x' number of wineries/geographic regions in a particular province etc..
        # Breakdown for most popular provinces making wine
        # Most popular wineries making wine

        wine_score_province = wine_rating_province.groupby(["Province"]).count()

        wine_score_province_df = wine_score_province.rename(
            columns={"Province": "Province", "Wine Rating": "Appellations within Province"})

        specific_columns_df["Province"].value_counts().head(30).plot.bar(figsize=(20, 10))
        plt.title(" Top 30 Provinces producing Wine")

        plt.xlabel("Provinces")
        plt.ylabel("Number of wineries")

        # plt.legend("popularity", loc="best")

        plt.savefig(self.outputFolder  +  'Top30producers.png')

        plt.show()
        plt.tight_layout()

        # Wineries grouped and counted by country and province
        # Counts number of wineries/vineyards in the region and number of times its wine has been scored.

        winery_grouped_province = specific_columns_df.groupby(["Countries", "Province", "Winery"]).count()

        # wine rating distribution
        # number of votes for particular rating in dataset

        specific_columns_df["Wine Rating"].value_counts().sort_index().plot.bar(figsize=(20, 10))

        plt.title("Wine Rating Distribution")

        plt.xlabel("Wine Rating")
        plt.ylabel("Number of Votes")

        # plt.legend("popularity", loc="best")

        plt.savefig(self.outputFolder  +  'WineRatings.png')

        plt.show()
        plt.tight_layout()

        # Previous graph results can be corroborated by subsequent graph
        # Wine ratings bins....

        df = specific_columns_df[["Province", "Wine Rating"]]

        # Score count

        score_80 = df[(df["Wine Rating"] >= 80) & (df["Wine Rating"] <= 84)].count()[0]
        score_85 = df[(df["Wine Rating"] >= 85) & (df["Wine Rating"] <= 89)].count()[0]
        score_90 = df[(df["Wine Rating"] >= 90) & (df["Wine Rating"] <= 94)].count()[0]
        score_95 = df[(df["Wine Rating"] >= 95) & (df["Wine Rating"] <= 100)].count()[0]
        scores = [score_80, score_85, score_90, score_95]

        # Creating the dictionary
        wine_rating_dict = {
            "Avg. Wine Ratings": scores
        }

        # Creating DataFrame & setting index
        wine_rating_dict = pd.DataFrame(wine_rating_dict)
        wine_rating_dict.index = (["80-84", "85-89", "90-94", "95-100"])

        # Use DataFrame.plot() in order to create a bar chart of the data
        wine_rating_dict.plot(kind="bar", color="c", figsize=(20, 10))

        # Set a title for the chart
        plt.title("Wine Rating Distribution")

        plt.xlabel("Classes")
        plt.ylabel("Ratings Counts")

        plt.savefig(self.outputFolder  +  'Wine rating Distribution.png')

        plt.show()
        plt.tight_layout()

        # Use DataFrame.plot() in order to create a bar chart of the data

        avg_wine_rating_country.plot(kind="bar", color="c", figsize=(20, 10))

        # Set a title for the chart

        plt.ylim(ymin=80)
        plt.ylim(ymax=100)
        plt.title("Average Wine Rating by Country")

        plt.xlabel("Country")
        plt.ylabel("Avg. Ratings")

        plt.savefig(self.outputFolder  +  'Avg_Rating_byCountry.png')

        plt.show()
        plt.tight_layout()
        return

    ##############################################################################
    def RenderPlot(self):
        return