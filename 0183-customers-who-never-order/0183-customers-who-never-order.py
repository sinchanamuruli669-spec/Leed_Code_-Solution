import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Left join
   merge = pd.merge(
    left = customers,right=orders,
    how = 'left',
    left_on='id',right_on='customerId'
   )
   #Based on null value filter & select name col
   result = merge[merge['customerId'].isna()][['name']]
   # Rename col name->coustomers
   result.columns=['Customers']
   return result