import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients.copy()

    check = r'(^|\s)DIAB1'

    return df[df["conditions"].str.contains(check)]