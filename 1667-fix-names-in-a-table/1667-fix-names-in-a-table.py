import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    
    df = users.copy()

    df["name"] = df["name"].apply(lambda s: s.lower())

    df["name"] = df["name"].apply(lambda s: s[0].upper() + s[1:].lower())

    return df.sort_values(by="user_id", ascending=True)