from etls.reddit_etl import connect_reddit, extract_posts, load_data_to_csv, transform_data
from utils.constants import CLIENT_ID, OUTPUT_PATH, SECRET
import pandas as pd

def reddit_pipeline(filename: str, subreddit: str, time_filter: 'day', limit = None):
    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    #DATA Extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)

    #transformation
    post_df = transform_data(post_df)

    #loading to CSV
    file_path = f'{OUTPUT_PATH}/{filename}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path

