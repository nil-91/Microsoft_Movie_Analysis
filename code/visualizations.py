"""
This module is for your final visualization code.
After you have done your EDA and wish to create some visualizations for you final jupyter notebook
A framework for each type of visualization is provided.
"""
# visualization packages
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Standard data manipulation packages
import pandas as pd
import numpy as np


# Set specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")


def genre_vs_income(clean_df):
    genre_vs_rating = clean_df[['averagerating','genre0']]

    ax = genre_vs_rating.groupby('genre0').median().plot(kind='bar', figsize=(10,6), fontsize=13, stacked=True, 
                                                    color = ['royalblue'])
    ax.set_xlabel('Genre of the movie', fontsize = 15)
    ax.set_ylabel("Average rating", fontsize=15);
    ax.set_title("Average rating by movie type", fontsize=22)
    plt.xticks(rotation = 50)
    plt.legend(fontsize=12)
    plt.savefig('./images/genre_vs_rating.png', transparent = True)   
    plt.show()
    pass

def genre_vs_rating(clean_df):
    genre_vs_gross = clean_df[['domestic_gross','foreign_gross','genre0']]

    ax = genre_vs_gross.groupby('genre0').median().plot(kind='bar', figsize=(10,6), fontsize=13, stacked=True, 
                                                    color = ['lightcoral','royalblue'])
    ax.set_xlabel('Genre of the movie', fontsize = 15)
    ax.set_ylabel("Income [$]", fontsize=15);
    ax.set_title("Gross income by movie type", fontsize=22)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(50000000.00))
    ax.yaxis.set_major_formatter(ticker.EngFormatter())
    plt.xticks(rotation = 50)
    plt.legend(fontsize=12)
    plt.savefig('./images/genre_vs_income.png', transparent = True)   
    plt.show()
    pass


def income_vs_year(clean_df): 
    gross_vs_year = clean_df[['domestic_gross','foreign_gross','year']]
    gross_vs_year['foreign_gross'].replace(',','', regex=True, inplace=True)
    gross_vs_year['foreign_gross'] = genre_vs_gross['foreign_gross'].astype('float64')

    ax = gross_vs_year.groupby('year').mean().plot(figsize=(10,6), fontsize=13, stacked=True, 
                                                        color = ['lightcoral','royalblue'])
    ax.set_xlabel('Year', fontsize = 15)
    ax.set_ylabel("Income [$]", fontsize=15);
    ax.set_title("Gross income by year", fontsize=22)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20000000.00))
    ax.yaxis.set_major_formatter(ticker.EngFormatter())
    plt.xticks(rotation = 50)
    plt.legend(fontsize=12)
    plt.grid()
    plt.savefig('./images/income_vs_year.png', transparent = True)   
    plt.show()
    pass

def votes_vs_year(clean_df): 
    votes_vs_year = clean_df[['numvotes','year']]

    ax = votes_vs_year.groupby('year').mean().plot(figsize=(10,6), fontsize=13, stacked=True, 
                                                        color = ['lightcoral','royalblue'])
    ax.set_xlabel('Year', fontsize = 15)
    ax.set_ylabel("Number of votes", fontsize=15);
    ax.set_title("Total votes by year", fontsize=22)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20000000.00))
    ax.yaxis.set_major_formatter(ticker.EngFormatter())
    plt.xticks(rotation = 50)
    plt.legend(fontsize=12)
    plt.grid()
    plt.savefig('./images/votes_vs_year.png', transparent = True)   
    plt.show()
    pass

def sample_plot2():
    """
    This is a sample visualization function to show what one looks like.
    The code is borrowed from https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/

    This function takes no arguments and shows a nice visualization without having all your code in the notebook itself.
    """

    plt.figure(figsize=(16, 10), dpi=80)
    # Import Data
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure(figsize=(16,10), dpi= 80)
    sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade=True, color="g", label="Cyl=4", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade=True, color="deeppink", label="Cyl=5", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade=True, color="dodgerblue", label="Cyl=6", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade=True, color="orange", label="Cyl=8", alpha=.7)

    # Decoration
    plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
    plt.gca().set(xlabel='Mileage per Gallon in the City', ylabel='Kernel Denisty')
    plt.legend()
    plt.savefig('./images/viz2.png', transparent = True)
    plt.show()

    pass


def visualization_one(target_var = None, input_vars= None, output_image_name=None):
    """
    The visualization functions are what is used to create each individual image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    ###
    # Main chunk of code here
    ###

    # Starter code for labeling the image
    plt.xlabel(None, figure = fig)
    plt.ylabel(None, figure = fig)
    plt.title(None, figure= fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'images/{output_image_name}.png', transparent = True, figure = fig)
    return fig