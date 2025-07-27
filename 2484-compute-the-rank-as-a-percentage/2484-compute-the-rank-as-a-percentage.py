import pandas as pd

def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    df = students.copy()
    
    df["rank"] = df.groupby('department_id')['mark'].rank(method='min', ascending=False)
    
    df["count"] = df.groupby('department_id')['student_id'].transform('count')
    
    df['percentage']=np.where(
        df['count']>1,
        np.round((df['rank']-1)*100/(df['count']-1),2),0.0
    )
    
    result = df[["student_id", "department_id", "percentage"]].sort_values(
        ["department_id", "student_id"], ascending=[True, True]
    )
    
    return result