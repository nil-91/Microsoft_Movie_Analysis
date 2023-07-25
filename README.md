# Microsoft Movie Analysis

<b> Author: </b> Niloufar Saharkhiz

## Overview

This project aims to provide insights for the head of Microsoft's new movie studio about successful movie types at the box office. Exploratory data analysis using data from [IMDB](https://www.imdb.com/) and [Box Office Mojo](https://www.boxofficemojo.com/) shows that the top three movie genres in terms of total gross income are Adventure, Action, and Mystery. In addition, Mystery, Documentary, and Biography movie genres have the highest average rating among all the other movie categories. The head of Microsoft movie studio can use this analysis to decide what type of films to create. 

## Buisiness Problem

Microsoft plans to invest on creating movies based on the type of the films that are currently successful at the box office. They may get insights on this by investigating the profit that each movie genre has made. This includes earnings from the domestic and global offices. The average rating for each movie category would also helpful to take into consideration.

## Data

The first sourse of data for these analysis is [IMDB](https://www.imdb.com/) website which is an online database of information related to films. The data contains infromation for 73856 movies, including genres,average rating and number of votes associated with each movie. The second source of the data is [Box Office Mojo](https://www.boxofficemojo.com/) website which contains information on domestic gross and foreign gross for 3387 movies. The information on movies genres, average rating and gross income both from domestic and international sources for the movies shared between the two databases will be used for the analysis. 

## Methods

This project usees descriptive analysis, including description of exsisting movies informarion for each movie genre. This provides a useful overview of some informations about movies in the past and insights for producing successsful future movies. 


## Results

In terms of profit, the top three main movies geners with highest total gross income are Adventure ($\$$ 282 M), Action ($\$$ 247 M), and Mystery ($\$$ 238 M). 

![https://github.com/nil-91/Microsoft_Movie_Analysis/blob/main/images/genre_vs_income.png](image_url

Below is a list of the contents of this repository.

- `README.md`: The README for this repo branch explaining it's contents - you're reading it now
- `TEMPLATE_README.md`: An example of a project README that provides a brief overview of your whole project
- `dsc-phase1-project-template.ipynb`: A starter Jupyter Notebook with headings, code examples and guiding questions
- `DS_Project_Presentation_Template.pdf`: A starter slide deck presenting your project - here is an [editable version](https://docs.google.com/presentation/d/1PaiH1bleXnhiPjTPsAXQSiAK0nkaRlseQIr_Yb-0mz0/copy)
- `__init__.py`: Python helper file that tells Python that there are packages in the repository that can be imported
- `zippedData` folder: A folder for the data you reference with your code
- `images` folder: A folder for the images you reference in your files
- `code` folder: A folder for the python scripts that your Jupyter Notebook imports
  - `__init__.py`: Python helper file that tells Python that there are packages in this folder that can be imported
  - `data_cleaning.py`: Code to prepare data for analysis
  - `visualizations.py`: Code to produce visualizations
  - `eda_notebook.ipynb`: Notebook with any messy EDA so the main notebook can be more readable
- `.gitignore`: A hidden file that tells git to not track certain files and folders
