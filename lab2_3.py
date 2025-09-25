import pandas as pd
import numpy as np

df = pd.read_excel("MobiSortIt_data.xlsx")

category_col = ['category', 'Similar_Problems', 'status', 'issuetype', 'privateproperty', 'assignment']
df[category_col] = df[category_col].astype('category')

print(df.dtypes)

OUTPUT:
ticketid               int64
category            category
Similar_Problems    category
duration_days        float64
status              category
issuetype           category
privateproperty     category
assignment          category
dtype: object
