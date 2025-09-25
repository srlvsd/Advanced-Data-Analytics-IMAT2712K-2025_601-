import pandas as pd
import numpy as np

df = pd.read_excel("MobiSortIt_data.xlsx")

category_col = ['category', 'Similar_Problems', 'status', 'issuetype', 'privateproperty', 'assignment']
df[category_col] = df[category_col].astype('category')
 
print("        ORIGINAL:")
print(df.dtypes)

categorical_columns = ['category', 'Similar_Problems', 'status', 'issuetype', 'assignment']

for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].astype('category')

print()

if 'privateproperty' in df.columns:
    df['privateproperty'] = df['privateproperty'].astype('bool')

if 'ticketid' in df.columns:
    df['ticketid'] = df['ticketid'].astype('str')

    print("          CHANGED:")
    print(df.dtypes)

            OUTPUT:
 ORIGINAL:
ticketid               int64
category            category
Similar_Problems    category
duration_days        float64
status              category
issuetype           category
privateproperty     category
assignment          category
dtype: object

          CHANGED:
ticketid              object
category            category
Similar_Problems    category
duration_days        float64
status              category
issuetype           category
privateproperty         bool
assignment          category
dtype: object
