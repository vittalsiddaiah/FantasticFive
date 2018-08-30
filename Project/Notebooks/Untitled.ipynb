{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "63"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import re\n",
    "\n",
    "rawWineDF = pd.read_csv(\"../Data/winemag-data-130k-v2.csv\")\n",
    "rawWineDF['Year'] = ''\n",
    "##############################################################################\n",
    "def GetYear(strn):\n",
    "    yearValue = 'Nan'\n",
    "    try: yearValue = int(re.findall('(\\d{4})', strn)[0])\n",
    "    except: yearValue = 'Nan' \n",
    "    return yearValue\n",
    "##############################################################################\n",
    "rawWineDF.Year = rawWineDF.apply(lambda row: GetYear(row.title),axis=1)\n",
    "##############################################################################\n",
    "rawWineDF.to_csv('../Data/WineData.csv')\n",
    "wineDF = rawWineDF[['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery', 'Year']]\n",
    "wineDF = wineDF.rename(columns={'region_1': 'region'})\n",
    "\n",
    "wineDF.head()\n",
    "\n",
    "temp = wineDF.country.dropna()\n",
    "\n",
    "wineDF.country.unique()\n",
    "\n",
    "temp.unique()\n",
    "\n",
    "len(wineDF) -len(temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
