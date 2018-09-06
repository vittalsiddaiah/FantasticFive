## Team:
* [Varsha Ramachandran](varsharcn@gmail.com)
* [Anastasiia lozano](alexis.filimonova@gmail.com)
* [Jagan Munagala](jagan1301@gmail.com)
* [Jacob Kaplan](j.kaplan814@yahoo.com)
* [Vittal Siddaiah](vittal.siddaiah@gmail.com)

### Analysis of Wine

## Do certain regions create a higher quality wine?	
We found that while most of the regions with a statistically significant amount of wines reviewed hovered around a score of 85-87, some regions slightly distinguished themselves with higher or lower ratings.

 
In this visualization, we chose to only show regions with over 300 wines reviewed. There were many more regions, but without a significant wine count, their average rating isn’t reliable.

## Do certain regions create a higher priced wine?
Similarly to the previous question, many regions hovered around the middle. However, we see many more outliers than we did when analyzing the score. 
 
We expect prices to be more volatile than ratings. These results support that idea. Pricing can vary based on cost of production, demand, and many other factors.

## How do price and rating relate to each other?
When comparing price and rating, we expect to see a positive relationship. As the rating of the wine increases, the price of the wine should also increase. 
We see a very clear trend here confirming our ideas. As the score of the wine increases, the price also increases.

## Do regions specialize in certain wines?
When determining whether regions specialize in specific wines, we chose to sample the largest region in the data set: Napa Valley in California.
 
We can see very clearly here that while Napa Valley produces a wide variety of wines, the production is heavily focused on Cabernet. There are also several other wines that are produced on a large scale, but the region as a whole seems to focus on Cabernet. This makes sense because certain climate and geological factors can favor specific wines. Producing Cabernet in Nappa Valley will produce a better tasting Cabernet than producing it in another region.

## What are the wineries with the highest average wine score?
The wineries with the highest average wine score are:
* Domaine Zind-Humbrecht (France)
* Lynmar (USA, California)
* Williams Selyem (USA, California).
However these wineries have an average wine price in a diapason from 60 to 80$ per bottle. And it’s in the middle of a price range.
![alt text](https://github.com/vittalsiddaiah/FantasticFive/blob/master/Project/src/images/Average_wine_scores.png?raw=true)

## What are the wineries with the most expensive wines on average?
Top 5 wineries with the highest average wine price are:
* Louis Latour (France)
* Louis Jabot (France)
* Albert Bichot (France)
* Chanson Pere et Fils (France)
* Jean-Luc and Paul Aegerter (France)
And, surprisingly, they all are located in France.
 


## What is the correlation between a price and a score of a wine?
While there is a clear trend: the higher an average price the higher a rating of a wine, it could be explained by subjective appreciation, it means people tend to rank higher more expensive wines. As the pleasure people get from consuming wine depends both on its intrinsic qualities such as taste and smell and external attributes such as price and presentation. 
 

## How does wine rating differ by country?
USA has most recorded ratings accounting for 42% of total count of ratings followed by France and Italy. 
 

## Which provinces produce most wine (top 30)?
•	USA tops the list with most provinces that produce wine. The top five provinces are California, Washington, Oregon, New York and Virginia which account for about 41% of total production. 
•	French provinces of Bordeaux, Burgundy, Alsace, Loire Valley, Champagne, Beaujolais, Southwest France, Provence and Rhone Valley account for 16% while the Italian provinces of Tuscany, Piedmont, Veneto, Northeastern Italy, Sicily & Sardinia, Southern Italy and Central Italy comprise about 14.5% of wine production worldwide.   
 

## What is the average rating for most wines?
* For this dataset, average wine rating for most wine varietals is between 85-89 (68,497 ratings accounting for 52%. Wines from major producers like USA, France, Italy, Spain and Portugal fall in this category. 
* Caveat: There are some outliers in the 95-100 rating range (2417 ratings accounting for 1.9%) suggesting that these wine varietals are most coveted and are among the most expensive.

 ![alt text](https://github.com/vittalsiddaiah/FantasticFive/blob/master/Project/src/images/Wine%20rating%20Distribution.png?raw=true)
 
## Does having higher number of wineries/vineyards translate to higher wine ratings?
* Even though there are significantly higher number of wineries in USA, the average wine rating is lower when compared to some other countries. However, the quality of wine produced here is attested to by the higher number of ratings/ upvotes recorded. The same applies to the French and Italian wines.
* Caveat: Despite having significantly low number of ratings in comparison, England still maintains the highest average rating which could suggest production of decent quality wine. But, more datapoints are required to make this conclusion. 
 
 ![alt text](https://github.com/vittalsiddaiah/FantasticFive/blob/master/Project/src/images/Avg_Rating_byCountry.png?raw=true)
 
## How does the type of wine relate to its average score or price?

There are 700+ different varieties of Wines.

The higher the price higher the score.

Most priced wines by Category:
* Champagne Blend
* Nebbiolo
* Cabernet Sauvignon
* Pinot Noir
 ![alt text](https://github.com/vittalsiddaiah/FantasticFive/blob/master/Project/src/images/Average_Wine_Prices_Variety_300.png)

## Highest scored wines by Category:

o	Sangiovese Grosso has the highest score in 300 wines Category (Sangiovese is a red Italian wine grape variety that derives its name from the Latin sanguis Jovis, "the blood of Jupiter")
o	Nebbiolo has the highest score has the highest score in 1000 wines Category. (Nebbiolo, or Nebieul is an Italian red wine grape variety predominantly associated with its native Piedmont region, where it makes the Denominazione di Origine Controllata e Garantita wines of Barolo, Barbaresco, Roero, Gattinara and Ghemme)
 
 ![alt text](https://github.com/vittalsiddaiah/FantasticFive/blob/master/Project/src/images/Average_Wine_Scores_Variety_300.png)
 
## How does vintage affect wine rating and price?
The major trend we expect to see when analyzing the vintage is that prices and ratings will increase and decrease proportionally. If a year had a particularly good climate, both its rating and price should increase.
 

This trend is observable in the analysis. When ratings increase or decrease slightly, the prices increase or decrease at a much larger rate. 

## Some Shortcomings with the Dataset
1.	It’s not clear how many years of data has been recorded in this dataset. More number of unique datapoints are required to glean concrete insights and predict trends. 
2.	No information on how other factors (climate, soil, air quality, inclement conditions like fires or drought etc.) may have played a role in quality of grapes produced to make wine. 
3.	There isn’t a lot of diversity in wine tasters i.e. a lot of repetitive votes have been recorded for most wine varieties, strongly suggesting bias. 
4.	It isn’t clear if all the ratings were recorded in a year or two or over period of time.
5.	Many vineyards/ wineries produce two or more wine varietals in their premises and have been listed multiple times. As a result, we cannot determine the relation between wine rating for every unique vineyard/ winery. 

## For the Future
Since we were cut for time and due to limitations in the dataset, we couldn’t answer some questions adequately. However, if given more time, we would use Google API and Weather API to be able to substantiate our conclusions and glean insights into trends better. 
