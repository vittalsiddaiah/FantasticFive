import pandas as pd
import re

rawWineDF = pd.read_csv("../Data/winemag-data-130k-v2.csv")
rawWineDF['Year'] = ''
##############################################################################
def GetYear(strn):
    yearValue = 'Nan'
    try: yearValue = int(re.findall('(\d{4})', strn)[0])
    except: yearValue = 'Nan' 
    return yearValue
##############################################################################
rawWineDF.Year = rawWineDF.apply(lambda row: GetYear(row.title),axis=1)
##############################################################################
rawWineDF.to_csv('../Data/WineData.csv')
wineDF = rawWineDF[['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery', 'Year']]
wineDF = wineDF.rename(columns={'region_1': 'region'})