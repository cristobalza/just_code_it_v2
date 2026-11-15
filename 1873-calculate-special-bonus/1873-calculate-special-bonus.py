import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    
    df = employees.copy()

    df['bonus'] = np.where((df["employee_id"] % 2 != 0) & (df["name"].str[0] != "M"), df["salary"], 0)

    return df[["employee_id", "bonus"]].sort_values(by="employee_id", ascending=True)