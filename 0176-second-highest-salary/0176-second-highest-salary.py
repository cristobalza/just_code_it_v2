import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    salaries = employee.drop_duplicates(subset="salary").sort_values(by="salary", ascending=False)["salary"]
    if len(salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    return pd.DataFrame({"SecondHighestSalary": [salaries.iloc[1]]})