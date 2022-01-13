import os
import shutil

from Scweet.scweet import scrape
import pandas as pd


def get_tweets_csv(user, start_date, end_date):
    '''
    Downloads CSV to an output directory generated within the current working directory.

    Args:
        user (str): Twitter username to emulate.
        start_date (str): Date to start scraping tweets from (YYYY-MM-DD)
        end_date (str): Date to end scraping tweets at (YYYY-MM-DD)

    Returns:
        tweets_df (Pandas Dataframe): Dataframe of downloaded tweets

    Raises:
        OSError: If an error occurs when trying to delete the CSV directory
    '''

    data = scrape(from_account=user, since=start_date, until=end_date)  # tweet download query

    # generates filepath for output tweets
    out_filename = '_'.join([user,start_date,end_date])
    out_filepath = os.path.join(os.getcwd(), "outputs", out_filename+'.csv')

    tweets_df = pd.read_csv(out_filepath)  # reads CSV as dataframe

    try:
        shutil.rmtree(os.path.join(os.getcwd(), "outputs"))  # deletes output directory and the file within it
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    return tweets_df

