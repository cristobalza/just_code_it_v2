import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.copy()

    df = df[df["author_id"] == df["viewer_id"]].drop_duplicates(subset="author_id").sort_values(by="author_id", ascending=True)
    df["id"] = df["author_id"]

    return df[["id"]]