import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    df = tweets.copy()

    df = tweets.groupby("tweet_id").agg(
        count=("content", lambda s: s.str.len().sum())
    ).reset_index()

    return df[df["count"] > 15][["tweet_id"]]