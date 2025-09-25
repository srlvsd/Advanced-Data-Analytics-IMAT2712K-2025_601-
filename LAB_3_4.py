import pandas as pd
import numpy as np

df["Cost per unit"] = df["Cost per order"] / df["Quantity"]
print(df.head())

OUTPUT:
  Supplier Order No.  Item No.    Item Description  Item Cost  \
0    Hulkey Fasteners  Aug11001      1122  Airframe fasteners       4.25   
1       Alum Sheeting  Aug11002      1243  Airframe fasteners       4.25   
2  Fast-Tie Aerospace  Aug11003      5462  Shielded Cable/ft.       1.05   
3  Fast-Tie Aerospace  Aug11004      5462  Shielded Cable/ft.       1.05   
4       Steelpin Inc.  Aug11005      5319  Shielded Cable/ft.       1.10   

   Quantity  Cost per order  A/P Terms (Months) Order Date Arrival Date  \
0     19500         82875.0                  30 2011-08-05   2011-08-13   
1     10000         42500.0                  30 2011-08-08   2011-08-14   
2     23000         24150.0                  30 2011-08-10   2011-08-15   
3     21500         22575.0                  30 2011-08-15   2011-08-22   
4     17500         19250.0                  30 2011-08-20   2011-08-31   

   Cost per unit  
0           4.25  
1           4.25  
2           1.05  
3           1.05  
4           1.10  

