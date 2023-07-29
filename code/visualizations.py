# visualization packages
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Standard data manipulation packages
import pandas as pd
import numpy as np

def genre_vs_income(all_movies):
    """
    This function will plot the primary genre of the movies in the all_movies dataframe by the domestic and foreign gross income 
    """
    genre_vs_gross = all_movies[['domestic_gross','foreign_gross','genre0']]

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

def genre_vs_rating(all_movies):
    """
    This function will plot the primary genre of the movies in the all_movies dataframe by the average rating 
    """
    genre_vs_rating = all_movies[['genre0', 'averagerating', 'numvotes']]
      
    fig, ax = plt.subplots(figsize=(10,6), ncols=1)
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
    sns.set_style("white")
    ax.set_title("Average movie rating per category", fontsize=15)
    ax.set_xlabel("Movie category", fontsize=15)
    ax.set_ylabel("Average rating", fontsize=15)
    ax.set_xticklabels(labels= labels, size=15, rotation=65)
    ax.tick_params(axis='y', labelsize=15)
    handles, labels = ax.get_legend_handles_labels()

    ax.legend().remove()
    plt.savefig('./images/genre_vs_rating.png', transparent = True)    

    plt.show()
    pass

def runtime_vs_income_rating(all_movies):
    """
    This function will plot the runtime of the movies in the all_movies dataframe by the domestic and foreign gross income, as       well as the average ratings 
    """
    runtime_vs_gross = all_movies[['total_gross','runtime[min]']]
    runtime_vs_rating = all_movies[['averagerating','runtime[min]']]
    time_intervals = pd.cut(runtime_vs_gross["runtime[min]"], bins=5)
    runtime_vs_gross["Runtime"] = time_intervals

    fig, [ax1,ax2] = plt.subplots(1,2,figsize=(15,6))
    sns.histplot(
        data = runtime_vs_gross,
        x="total_gross",
        hue="Runtime",
        palette="BuPu_r",
        bins=10,
        kde=False,
        ax=ax1,
        multiple="dodge",
        linewidth=1,
        edgecolor='black'
    )
    sns.set_style("white")
    #ax1.set_title("Total gross income vs movie runtime", fontsize=17)
    ax1.set_xlabel("Total gross income [$]", fontsize=15)
    ax1.set_ylabel("Number of movies", fontsize=15)
    ax1.set_xlim([-0.5e8, np.max(runtime_vs_gross["total_gross"])])
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(np.max(runtime_vs_gross["total_gross"])/10))
    ax1.xaxis.set_major_formatter(ticker.EngFormatter())
    legend = ax1.legend(title="Runtime [min]", labels=['Very short', 'Short', 'Average', 'Long', 'Very Long'], fontsize=12)
    legend.get_title().set_fontsize(12)
    ax1.tick_params(axis='x', labelsize=12, rotation=65)
    ax1.tick_params(axis='y', labelsize=15)
    ax1.set_yscale('log', nonposy='clip')

    time_intervals = pd.cut(runtime_vs_rating["runtime[min]"], bins=5)
    runtime_vs_rating["Runtime"] = time_intervals

    sns.histplot(
        data = runtime_vs_rating,
        x="averagerating",
        hue="Runtime",
        palette="BuPu_r",
        bins=10,
        kde=False,
        ax=ax2,
        multiple="dodge",
        linewidth=1,
        edgecolor='black'
    )
    sns.set_style("white")
    #ax1.set_title("Total gross income vs movie runtime", fontsize=17)
    ax2.set_xlabel("Average rating", fontsize=15)
    ax2.set_ylabel("Number of movies", fontsize=15)
    legend = ax2.legend(title="Runtime [min]", labels=['Very short', 'Short', 'Average', 'Long', 'Very Long'],fontsize=12)
    legend.get_title().set_fontsize(12)
    ax2.set_yscale('log', nonposy='clip')
    ax2.tick_params(axis='x', labelsize=15)
    ax2.tick_params(axis='y', labelsize=15)
    ax2.set_xticks([1,2,3,4,5,6,7,8,9,10])
    plt.tight_layout()
    plt.savefig('./images/runtime_vs_income.png', transparent = True)    
    plt.show()     
    pass

def income_vs_rating(all_movies): 
    """
    This function will plot the income of the movies in the all_movies dataframe by their average ratings
    """
    income_vs_vote = all_movies[['averagerating','total_gross','numvotes']]
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

