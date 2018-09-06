##############################################################################
import pandas as pd
import re
##############################################################################


class ReadNCleanData:

    def __init__(self):
        return

    ##############################################################################
    def GetYear(self, strn):
        yearValue = 'Nan'
        try:
            yearValue = int(re.findall('(\d{4})', strn)[0])
        except:
            yearValue = 'Nan'
        return yearValue
    ##############################################################################

    ##############################################################################
    def Get(self, inputCSVFile):
        rawWineDF = pd.read_csv(inputCSVFile)
        rawWineDF['Year'] = ''
        rawWineDF.Year = rawWineDF.apply(lambda row: self.GetYear(row.title), axis=1)
        rawWineDF.to_csv('../Data/WineData.csv')
        wineDF = rawWineDF[
            ['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'title', 'variety',
             'winery', 'Year']]
        wineDF = wineDF.rename(columns={'region_1': 'region'})
        return wineDF
    ##############################################################################

##############################################################################