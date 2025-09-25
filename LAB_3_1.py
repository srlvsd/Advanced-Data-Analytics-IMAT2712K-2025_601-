import pandas as pd
import numpy as np

df = pd.read_excel('Purchase Orders.xlsx', sheet_name='Data')

print(" ALL COLUMNS", df.columns.tolist())


first_col_name = df.columns[0]
suppliers = df[first_col_name]

print(f"\nData from '{first_col_name}':")
print(suppliers.head())
print(f"Total records: {len(suppliers)}")

print(f"\nFirst 10 values:")
print(suppliers.head(10).tolist())

OUTPUT:
 ALL COLUMNS ['Supplier', 'Order No.', 'Item No.', 'Item Description', 'Item Cost', 'Quantity', 'Cost per order', 'A/P Terms (Months)', 'Order Date', 'Arrival Date']

Data from 'Supplier':
0      Hulkey Fasteners
1         Alum Sheeting
2    Fast-Tie Aerospace
3    Fast-Tie Aerospace
4         Steelpin Inc.
Name: Supplier, dtype: object
Total records: 94

First 10 values:
['Hulkey Fasteners', 'Alum Sheeting', 'Fast-Tie Aerospace', 'Fast-Tie Aerospace', 'Steelpin Inc.', 'Fast-Tie Aerospace', 'Steelpin Inc.', 'Durrable Products', 'Fast-Tie Aerospace', 'Fast-Tie Aerospace']
