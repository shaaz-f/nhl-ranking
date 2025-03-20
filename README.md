# nhl-ranking

## The goal
After each NHL game, give each player a score on their performance.

## The method
Doing research, it seems as though some sort of Mixture Model is the way to go for clustering.
This will allow us to assign probabilities to each 'cluster', and allow sorts of overlapping within each of the clusters.
- I'm thinking to start with E-M clustering. We can hopefully find around 4-5 clusters regarding performance metrics, then get a score based on their distance from the center of it.
- GMM assumes a gaussian distribution, but in general only some of the features are gaussian populations, whereas others are definitely closer to poisson or exponential. 

03-19-2025

Another potential method is to simply learn the distributions of each feature. Initially can assume normality and learn gaussian mean, variance, and covariances.
Following this, can use some sort of scoring method that takes this into account, one that came into mind was Mahalanobis distance.
- Problem with Mahalanobis distance is firstly, its based on the chi-square distribution.
- Secondly, it doesn't take into account negative and positive distance from centers, only how far away from the means.
- To solve the above issue, we can simply just check each individual feature distance from its mean, and apply a negative or positive scaling to our result.
- More learning (on my end) needs to be done before implementing the above.

Overall, in an ideal world we have different distributions for each feature, but then I'm not sure how we would learn the covariances between each variable.
I'm thinking of starting off by only considering defensive stats such as turnovers, blocks, chances against, goals against, etc... and assuming a normal distribution.
- These features are likely poisson, but since it's also part of the exponential family, there may be a way to apply known methods to these distributions.
- I think firstly it would be best to clean the data and develop some helper functions before continuing much further.

## Utilities
- Python: BeautifulSoup, Numpy, Pandas, Scikit-learn
- To potentially demonstrate data cleaning skills, SQL/Mongo
- Docker for containerization
- Will need something for data visualization eventually.


# Step 1 -- Scraping & Cleaning
Using BeauitfulSoup to scrape game performance from Natural Stat Trick. 
- Decided to only scrape tables to improve runtime.

Will then move data to sqlite database. *Insert DB Structure Graphic*
