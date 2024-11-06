import pandas as pd
import seaborn as sns
import yfinance as yf
import plotly.express as px

def load_ticker_data(ticker, date_range = ('2019-11-01', None)):
    # Download ticker data from Yahoo! Finance
    start, end = date_range
    df = yf.download(ticker, start=date_range[0], end=date_range[1], progress=False)

    return df

def normalize(df):
    """
    Normalizes a DataFrame by adjusting index and column naming conventions.
    
    The function performs the following transformations:
      - Converts the index name to lowercase.
      - Drops the second level of the column MultiIndex, if present.
      - Strips whitespace from column names.
      - Converts column names to lowercase.
      - Replaces spaces in column names with underscores.
      
    Parameters:
        df (pd.DataFrame): The DataFrame to normalize.
        
    Returns:
        pd.DataFrame: A new DataFrame with normalized column and index names.
    """

    result_df = df.copy()

    # Normalize index name
    if result_df.index.name is not None:
        result_df.index.name = result_df.index.name.lower()

    # Drop the second level in the column MultiIndex if it exists
    if isinstance(result_df.columns, pd.MultiIndex) and result_df.columns.nlevels > 1:
        result_df.columns = result_df.columns.droplevel(1)

    # Normalize column names
    result_df.columns = result_df.columns.str.strip()
    result_df.columns = result_df.columns.str.lower()
    result_df.columns = result_df.columns.str.replace(' ', '_', regex=False)

    # Normalize column index name, if it exists
    if result_df.columns.name is not None:
        result_df.columns.name = None

    return result_df

def create_date_column(df):
    """
    Creates a 'date' column in a DataFrame if not there already. If date was the index, reset the index to an integer.

    Parameters:
        df (pd.DataFrame): The DataFrame where the date column will be created

    Returns:
        result_df (pd.DataFrame): The updated DataFrame with the date column and integer index.
    """
    
    result_df = df.copy()

    #If the dataframe's index is a date, it needs to be put in a column
    if isinstance(result_df.index, pd.DatetimeIndex) :
        result_df['date'] = result_df.index.strftime("%Y-%m-%d")
        result_df['date'] = pd.to_datetime(result_df['date'])
        
        
    #If the index is not a date, just make sure date column has the same format.
    else:
        #result_df['date'] = result_df['date'].strftime("%Y-%m-%d")
        result_df['date'] = pd.to_datetime(result_df['date'])
        
    #Reset the index     
    result_df = result_df.reset_index(drop=True)
    
    return result_df

def plot_plotly(data, title, x='date', y='adj_close', labels=('Date', 'Adjusted Closing Price')):
    """
    Plots an interactive line graph with optional event markers and export functionality.
    
    Parameters:
        data (pd.DataFrame): The dataframe where the data to plot (e.g., closing prices) is.
        x (str): The column name to be plotted on the x axis. By default, it is the date column.
        y (str): The column name to be plotted on the y axis. By default, it is the adj_close column.
        labels (tuple): A tuple containing two strings: 
                        - labels[0]: The label for the x-axis (typically "Date").
                        - labels[1]: The label for the y-axis (e.g., "Closing Price ($)").
        title (str): Title of the graph to be plotted
                                     
    Returns:
        None. Displays the plot and optionally saves it if export_path is provided.
    """

    # Plot graph from input data and labels
    fig = px.line(data, x=x, y=y, labels={x : labels[0], y : labels[1]}, title=title)
    fig.show()  

def monthly_and_annual_returns_stats(df):

    result_df=df.copy()
    # Calculate monthly returns using the last available 'adj_close' within each month
    monthly_returns = result_df.set_index('date').resample("ME")['adj_close'].last().pct_change() * 100
    annual_returns = result_df.set_index('date').resample("YE")['adj_close'].last().pct_change() * 100

    mean_monthly_returns = monthly_returns.mean()
    std_monthly_returns = monthly_returns.std()
    mean_annual_returns = annual_returns.mean()
    std_annual_returns = annual_returns.std()

    return mean_monthly_returns, std_monthly_returns, mean_annual_returns, std_annual_returns

def analysis_df(df, company, export=False):

    result_df = df.copy()
    
    result_df['daily_returns'] = result_df.adj_close.pct_change() * 100
    result_df['daily_returns'] = result_df['daily_returns'].bfill()
    result_df['daily_range'] = result_df.high - result_df.low

    summary = {}
    
    for column in ['open', 'high', 'low', 'close', 'adj_close', 'volume', 'daily_returns', 'daily_range']:
        column_mean = round(result_df[column].mean(), 3)
        column_std = round(result_df[column].std(), 3)
        summary[column] = [column_mean, column_std]
    
    summary['monthly_returns'] = [round(monthly_and_annual_returns_stats(result_df)[0], 3), round(monthly_and_annual_returns_stats(result_df)[1], 3)]
    summary['annual_returns'] = [round(monthly_and_annual_returns_stats(result_df)[2], 3), round(monthly_and_annual_returns_stats(result_df)[3], 3)]

    analysis_df = pd.DataFrame(summary, index=['mean', 'std'])

    if export:
        analysis_df.to_csv(f'../data/clean/analysis_{company}.csv', index=False)
    
    return result_df, analysis_df

def plot(data, labels, events=[], export_path=None):
    """
    Plots a time series data with optional event markers and export functionality.
    
    Parameters:
        data (pd.Series): The time series data to plot (e.g., closing prices).
        labels (tuple): A tuple containing two strings: 
                        - labels[0]: The label for the x-axis (typically "Date").
                        - labels[1]: The label for the y-axis (e.g., "Closing Price ($)").
        events (list of dicts, optional): List of events to mark on the plot. 
                                           Each event should be a dictionary with:
                                           - "name" (str): Event label (e.g., "COVID").
                                           - "date" (datetime): Date of the event.
        export_path (str, optional): File path to save the plot as an image. If provided,
                                     the plot will be saved at this location.
                                     
    Returns:
        None. Displays the plot and optionally saves it if export_path is provided.
    """

    # Plot graph from input data and labels
    ax = data.plot(figsize=(12, 6), label=labels[1])
    
    # Draw event markers
    for event in events:
        ax.axvline(event["date"], color="red", linestyle="--", linewidth=0.8)
        ax.text(event["date"] + pd.Timedelta(days=10), data.max(), event["name"], color="red", ha="left", va="top")

    # Set additional plot information
    ax.set_title(labels[1])
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.legend()

    # Save plot to file, if provided
    if export_path:
        ax.get_figure().savefig(export_path)

def plot_ticker(ticker, series, date_range = ('2019-11-01', None), events=[], plot_figure=True):
    """
    Fetches historical stock data for a specified ticker and date range, normalizes the data,
    and plots a specified series with optional event markers.
    
    Parameters:
        ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple).
        series (str): The name of the data series to plot, must be one of the following:
                      - "adj_close": Adjusted closing price
                      - "close": Closing price
                      - "high": Highest price during the day
                      - "low": Lowest price during the day
                      - "open": Opening price
                      - "volume": Trading volume
        date_range (tuple of datetime): A tuple with two datetime objects representing 
                                        the start and end dates (start, end) for the data.
        events (list of dicts, optional): List of events to mark on the plot. 
                                          Each event should be a dictionary with:
                                          - "name" (str): Event label (e.g., "COVID").
                                          - "date" (datetime): Date of the event.
                                          
    Returns:
        None. Calls the `plot` function to display the specified series from the historical
        stock data with event markers.
    """

    # Download ticker data from Yahoo! Finance
    start, end = date_range
    df = yf.download(ticker, start=start, end=end, progress=False)

    # Normalize fetched DataFrame
    df = normalize(df)

    # Create a 'date' column in the DataFrame
    df = create_date_column(df)

    # Plot specific series or list of series from DataFrame
    if plot_figure:
        plot(df[series], (df.index.name, series), events)

    return df
