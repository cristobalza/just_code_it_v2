import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery.copy()
    df["is_immediate"] = np.where(df["order_date"] == df["customer_pref_delivery_date"], 1, 0)

    data = np.round((np.sum(df["is_immediate"]) / len(df)) * 100, 2)

    return pd.DataFrame({"immediate_percentage": [data]})
     