import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data (Keep middle 95 percentiles)
df = df[df.value.between(df.value.quantile(0.025), df.value.quantile(0.975))]    


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df.values, 'r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).value.mean().unstack()

    # Draw bar plot
    fig, ax = plt.subplots()
    df_bar.plot(ax=ax, kind='bar', figsize=(8, 6), ylabel='Average Page Views', xlabel='Years')
    ax.legend(title='Months', labels=calendar.month_name[1:])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 7))

    sns.boxplot(x=df_box.year, y=df_box.value, ax=ax1)
    sns.boxplot(x=df_box.month, y=df_box.value, ax=ax2, order=calendar.month_abbr[1:] )

    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
