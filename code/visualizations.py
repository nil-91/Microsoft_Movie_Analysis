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
    genre_vs_gross = clean_df[['domestic_gross','foreign_gross','genre0']]

    ax = genre_vs_gross.groupby('genre0').mean().plot(kind='bar', figsize=(10,6), fontsize=13, stacked=True, 
                                                         color = ['#894da3','#8c7dba'])
    ax.set_xlabel('Genre of the movie', fontsize = 15)
    ax.set_ylabel("Income [$]", fontsize=15);
    ax.set_title("Gross income by movie type", fontsize=17)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(50000000.00))
    ax.yaxis.set_major_formatter(ticker.EngFormatter())
    plt.xticks(rotation = 50)
    plt.legend(labels=['Domestic gross', 'Foreign gross'], fontsize=12)
    plt.savefig('./images/genre_vs_income.png', transparent = True)    
    plt.show()
    pass

def genre_vs_rating(clean_df):
    genre_vs_rating = clean_df[['genre0', 'averagerating', 'numvotes']]
      
    fig, ax = plt.subplots(figsize=(25,6), ncols=1)
    labels = list(genre_vs_rating['genre0'].unique())
    sns.boxplot(x="genre0",
                    y="averagerating",
                    data=genre_vs_rating,
                    ax=ax,
                    #palette="BuPu_r",
                    color = '#8c7dba',
                    #dodge=False
    )
    sns.stripplot(x="genre0",
                  y="averagerating",
                  data=genre_vs_rating,
                  #palette="BuPu_r",
                  color = '#821580'
    )
    sns.set_style(
        "darkgrid")
    ax.set_title("Average movie rating per category", fontsize=32)
    ax.set_xlabel("Movie category", fontsize=30)
    ax.set_ylabel("Average rating", fontsize=30)
    ax.set_xticklabels(labels= labels, size=25, rotation=65)
    ax.tick_params(axis='y', labelsize=30)
    handles, labels = ax.get_legend_handles_labels()

    ax.legend().remove()
    plt.savefig('./images/genre_vs_rating.png', transparent = True)    

    plt.show()
    pass

def genre_vs_vote(clean_df):
    genre_vs_numvotes = clean_df[['genre0','numvotes']]
    df = genre_vs_numvotes.groupby('genre0').agg('mean')
    df = df.reset_index()
    mean_by_genre = genre_vs_numvotes.groupby('genre0')['numvotes'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10,6))
    labels = mean_by_genre.index
    sns.barplot(
        x="genre0",
        y="numvotes",
        data=df,
        ax=ax,
        #palette='BuPu_r',
        #hue = df["numvotes"].values.astype(int),
        #hue_order = np.sort(df["numvotes"].values.astype(int))[::-1],
        dodge=False,
        color = '#894da3',
        order = mean_by_genre.index
    )
    sns.set_style(
        "darkgrid")
    ax.set_title("Mean number of votes per category", fontsize=17)
    ax.set_xlabel("Movie category", fontsize=15)
    ax.set_ylabel("Number of votes", fontsize=15)
    ax.set_xticklabels(labels= labels, size=15, rotation=65)
    ax.tick_params(axis='y', labelsize=15)
    handles, labels = ax.get_legend_handles_labels()
    plt.tight_layout()
    plt.savefig('./images/genre_vs_vote.png', transparent = True)    
    plt.show()
    pass


def income_vs_year(clean_df): 
    income_vs_year = clean_df[['year','domestic_gross','foreign_gross']]
    df = income_vs_year[['domestic_gross','year']].groupby('year').agg('count')
    df.reset_index()
    df.rename(columns={'domestic_gross':'count'}, inplace=True)
    income_vs_year = pd.merge(income_vs_year, df, on='year')

    fig, axes = plt.subplots(figsize=(25,6), ncols=2)
    sns.boxplot(x="year",
                    y="domestic_gross",
                    data=income_vs_year,
                    ax=axes[0],
                    palette="BuPu_r",
                    hue="count",
                    dodge=False
    )
    sns.boxplot(x="year",
                    y="foreign_gross",
                    data=income_vs_year,
                    ax=axes[1],
                    palette="BuPu_r",
                    hue="count",
                    dodge=False    
    )
    axes[0].set_title('Domestic gross across years', fontsize=15)
    axes[0].set_xlabel('Year', fontsize=15)
    axes[0].set_ylabel('Domestic gross [$]', fontsize=15)
    axes[0].set_ylim((-50000, 970000000))
    axes[0].tick_params(axis='y', labelsize=15)
    axes[0].tick_params(axis='x', labelsize=15)
    axes[0].yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    axes[0].yaxis.set_major_locator(ticker.MultipleLocator(100000000.00))
    axes[0].yaxis.set_major_formatter(ticker.EngFormatter())
    axes[0].legend(title="Number of movies",loc=2, fontsize=15, fancybox=True)
    
    axes[1].set_title('Foreign gross across years', fontsize=15)
    axes[1].set_xlabel('Year', fontsize=15)
    axes[1].set_ylabel('Foreign gross [$]', fontsize=15)
    axes[1].set_ylim((-50000, 970000000))
    axes[1].tick_params(axis='y', labelsize=15)
    axes[1].tick_params(axis='x', labelsize=15)
    axes[1].yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    axes[1].yaxis.set_major_locator(ticker.MultipleLocator(100000000.00))
    axes[1].yaxis.set_major_formatter(ticker.EngFormatter())
    axes[1].legend().remove()
    plt.savefig('./images/income_vs_year.png', transparent = True)   
    plt.show()
    pass

def income_vs_rating(clean_df): 
    income_vs_vote = clean_df[['averagerating','total_gross','numvotes']]
    fig, ax = plt.subplots(figsize=(15,6))
    sns.scatterplot(
                    x="averagerating",
                    y="total_gross",
                    data=income_vs_vote,
                    alpha=0.9,
                    color=['#894da3']
    )
    ax.set_title('Total gross with repect to average rating for all the movies', fontsize=15)
    ax.set_xlabel('Average rating', fontsize=15)
    ax.set_ylabel('Total gross [$]', fontsize=15)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(100000000.00))
    ax.yaxis.set_major_formatter(ticker.EngFormatter())
    ax.legend().remove()
    ax.autoscale_view()
    plt.tight_layout()
    plt.savefig('./images/income_vs_rating.png', transparent = True)   
    plt.show()
    pass

