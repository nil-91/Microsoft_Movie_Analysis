import pandas as pd
import os 

def prep_imdb(imdb):
    """This function reads in the data from imdb and clean it"""
    imdb.columns = imdb.columns.str.lower().str.replace(' ', '_')
    imdb.drop(columns = ['movie_id','original_title'], inplace=True)
    imdb.rename({'primary_title':'title'}, axis=1, inplace=True)
    imdb['title'] = imdb['title'].str.title()
    imdb.rename({'start_year':'year'},axis=1, inplace=True)
    imdb.rename({'runtime_minutes':'runtime[min]'},axis=1, inplace=True)
    return imdb

def prep_bom(bom):
    """This function reads in the data from bom and clean it"""
    bom.columns = bom.columns.str.lower().str.replace(' ', '_')
    bom.drop(columns = ['studio'], inplace = True)
    bom['title'] = bom['title'].str.title()
    return bom

def merge_imdb_bom(imdb_df, bom_df):
    """This function reads in the data from imdb and bom and merges them based on the title and year"""
    df = pd.merge(imdb_df, bom_df, on=['title', 'year'])
    df.dropna(subset= ['domestic_gross','foreign_gross','genres','runtime[min]'], inplace=True)
    df['total_gross'] = df['domestic_gross'].astype(float) + df['foreign_gross'].str.replace(',', '').astype(float)
    df['foreign_gross'].replace(',','', regex=True, inplace=True)
    df['foreign_gross'] = df['foreign_gross'].astype('float64')
    df.sort_values(by=['total_gross'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df = df.join(df['genres'].str.split(",",expand=True).add_prefix('genre'))
    return df

def full_clean(imdb, bom):
    """
    This is the one function called that will run all the support functions.
    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    imdb_clean = prep_imdb(imdb)
    bom_clean = prep_bom(bom)
    cleaned_data= merge_imdb_bom(imdb_clean, bom_clean)
    if not os.path.exists('data'):
        os.mkdir('data')
    cleaned_data.to_csv('./data/cleaned_dataset.csv')
    
    return cleaned_data