import pandas as pd
import numpy as np
df = pd.read_excel("Purchase Orders.xlsx", sheet_name="Data")

df_grouped = df.groupby("Supplier").agg(
    total_orders=("Order No.", "count"),
    total_cost=("Cost per order", "sum"),
    avg_unit_cost=("Cost per order", "mean")
).reset_index()

print(df_grouped.head())

OUTPUT:
 Supplier  total_orders  total_cost  avg_unit_cost
0       Alum Sheeting             8   427830.00   53478.750000
1   Durrable Products            13   475715.75   36593.519231
2  Fast-Tie Aerospace            15   224450.00   14963.333333
3    Hulkey Fasteners            15   618843.75   41256.250000
4        Manley Valve            11   122838.75   11167.159091
