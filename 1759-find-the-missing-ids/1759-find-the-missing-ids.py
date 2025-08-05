import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    customers_set = set(customers["customer_id"].value_counts().index.to_numpy())
    num_list = [num for num in range(1, np.max(customers["customer_id"]))] 
    
    data = []
    for num in num_list:
        if num not in customers_set:
            data.append(num)

    return pd.DataFrame({"ids": data})