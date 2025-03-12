# nhl-ranking

## The goal
After each NHL game, give each player a score on their performance.

## The method
Doing research, it seems as though some sort of Mixture Model is the way to go for clustering.
This will allow us to assign probabilities to each 'cluster', and allow sorts of overlapping within each of the clusters.
- I'm thinking to start with E-M clustering. We can hopefully find around 4-5 clusters regarding performance metrics, then get a score based on their distance from the center of it.
- GMM assumes a gaussian distribution, but in general only some of the features are gaussian populations, whereas others are definitely closer to poisson or exponential. 

## Utilities
- Python: BeautifulSoup, Numpy, Pandas, Scikit-learn, Pomogranate?
- To potentially demonstrate data cleaning skills, SQL/Mongo
- Docker for containerization
- Will need something for data visualization eventually.
