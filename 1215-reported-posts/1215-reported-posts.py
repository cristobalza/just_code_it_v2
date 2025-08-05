import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:

    target_date = pd.to_datetime('2019-07-05') - timedelta(days=1)
    df = actions.copy()
    df= df[(df['action']=='report') & (df['action_date']==target_date)]
    result= df.groupby('extra', as_index=False).agg(report_count=('post_id','nunique'))
    return result.rename(columns={'extra':'report_reason'})
