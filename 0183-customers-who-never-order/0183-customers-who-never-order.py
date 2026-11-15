import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_df = customers.copy()
    orders_df = orders.copy()

    res_df = customers_df[~customers_df["id"].isin(orders_df["customerId"])][['name']]
    res_df["Customers"] = res_df["name"]

    return res_df[["Customers"]]
    