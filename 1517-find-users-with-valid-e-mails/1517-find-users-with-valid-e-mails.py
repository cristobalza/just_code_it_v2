import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    check = r'[a-zA-Z][a-zA-Z0-9\_\.\-]*@leetcode\.com'

    df = users.copy()

    return df[df["mail"].str.fullmatch(check)]