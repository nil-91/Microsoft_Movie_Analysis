"""
This module is for your data cleaning.
It should be repeatable.
If you are combining different data sources you might need a few different functions

## Data links:


## SUPPORT FUNCTIONS
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd

def prep_imdb(imdb):
    """This finction reads in the data from imdb and clean it"""
    imdb.columns = imdb.columns.str.lower().str.replace(' ', '_')
    imdb.drop(columns = ['movie_id', 'runtime_minutes','original_title'], inplace=True)
    imdb.rename({'primary_title':'title'}, axis=1, inplace=True)
    imdb['title'] = imdb['title'].str.title()
    imdb.rename({'start_year':'year'},axis=1, inplace=True)
    return imdb

def prep_bom(bom):
    """This function might read in and clean a different data source"""
    bom.columns = bom.columns.str.lower().str.replace(' ', '_')
    bom.drop(columns = ['studio'], inplace = True)
    bom['title'] = bom['title'].str.title()
    return bom

def merge_imdb_bom(imdb_df, bom_df):
    """This one might merge the above two sources and create a few new variables"""
    df = pd.merge(imdb_df, bom_df, on=['title', 'year'])
    df.dropna(subset= ['domestic_gross','foreign_gross'], inplace=True)
    df['total_gross'] = df['domestic_gross'].astype(float) + df['foreign_gross'].str.replace(',', '').astype(float)

    return df

def full_clean():
    """
    This is the one function called that will run all the support functions.
    Assumption: 
        - Your data files will be saved in a data folder and named "dirty_data.csv"
        - OR you might read directly from a few urls
        - this code is guidance, not rules

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    imdb_dirty = pd.read_csv("./data/dirty_data.csv")

    imdb_clean = prep_imdb(imdb_dirty)
    bom_clean = prep_bom(bom_dirty)
    cleaned_data= support_function_three(cleaning_data2)
    cleaned_data.to_csv('./data/cleaned_for_testing.csv')
    
    return cleaned_data