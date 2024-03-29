![director shot](https://github.com/nil-91/Microsoft_Movie_Analysis/blob/main/images/director_shot.jpeg)

# Microsoft Movie Analysis

<b> Author: </b> Niloufar Saharkhiz

## Overview

This project aims to provide insights for the head of Microsoft's new movie studio about successful movie types at the box office. Exploratory data analysis using data from [IMDB](https://www.imdb.com/) and [Box Office Mojo](https://www.boxofficemojo.com/) shows that the top three movie genres in terms of total gross income are Adventure, Action, and Mystery. In addition, Mystery, Documentary, and Biography movie genres have the highest average rating among all the other movie categories. The head of Microsoft movie studio can use this analysis to decide what type of films to create. 

## Buisiness Problem

Microsoft plans to invest in creating movies based on the type of films currently successful at the box office. They may get insights into this by investigating the profit that each movie genre has made. This includes earnings from the domestic and global offices. The average rating for each movie category would also be helpful to consider.

## Data

The first data source for these analyses is the [IMDB](https://www.imdb.com/), an online database of information related to films. The data contains information for 73856 movies, including genres, average rating, and number of votes associated with each movie. The second data source is the [Box Office Mojo](https://www.boxofficemojo.com/) website which contains information on domestic gross and foreign gross for 3387 movies. The information on movie genres, average rating and gross income from domestic and international sources for the movies shared between the two databases will be used for the analysis. 

## Methods

This project uses descriptive analysis, including a description of each genre's existing movie information. This provides a valuable overview of some information about movies in the past and insights for producing successful future movies.


## Results

In terms of profit, the top three main movie genres with the highest total gross income are Adventure ($ 282 M), Action ($ 247 M), and Mystery ($ 238 M). 

![Gross income vs movie genre](https://github.com/nil-91/Microsoft_Movie_Analysis/blob/main/images/genre_vs_income.png)


The top three main movie genres with the highest average ratings were found to be Mystery, Documentary, and Biography. However, the number of movies with Mystery as the primary genre is lower than the other categories. Therefore, more investigation on movies with this main genre category is required. The movie genres with the lowest average rating were Adventure, Comedy, and Horror.

![Rating vs movie genre](https://github.com/nil-91/Microsoft_Movie_Analysis/blob/main/images/genre_vs_rating.png)


## For More Information

Please review my full analysis in [my Jupyter Notebook](./microsoft_movie_analysis.ipynb) or my [Presentation](./microsoft_movie_analysis.pdf).

For any additional questions, please contact Niloufar Saharkhkiz at [niloufar.shkz@gmail.com](mailto:niloufar.shkz@gmail.com)


## Repository Structure

```
├── __init__.py                         
├── README.md                           
├── microsoft_movie_analysis.ipynb  
├── microsoft_movie_analysis.pdf        
├── code
│   ├── __init__.py                     
│   ├── visualizations.py               
│   ├── data_preparation.py            
│   └── eda_notebook.ipynb             
├── data                                
└── images                              
```
