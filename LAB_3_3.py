import pandas as pd
import numpy as np

df = pd.read_excel('Purchase Orders.xlsx', sheet_name='Data')
df_sorted = df.sort_values(by="Cost per order", ascending=False)
print(df_sorted)

OUTPUT:
     Supplier Order No.  Item No. Item Description  Item Cost  \
73      Alum Sheeting  Oct11026      5417    Control Panel     255.00   
61  Durrable Products  Oct11014      5454    Control Panel     220.00   
70  Durrable Products  Oct11023      5454    Control Panel     220.00   
15      Alum Sheeting  Sep11002      5417    Control Panel     255.00   
72      Steelpin Inc.  Oct11025      8008   Machined Valve     645.00   
..                ...       ...       ...              ...        ...   
84       Manley Valve  Nov11001      9977      Panel Decal       1.00   
89       Manley Valve  Nov11006      9967      Hatch Decal       0.85   
12   Hulkey Fasteners  Aug11013      9966      Hatch Decal       0.75   
85       Manley Valve  Nov11002      9955       Door Decal       0.55   
93       Manley Valve  Nov11010      9955       Door Decal       0.55   

    Quantity  Cost per order  A/P Terms (Months) Order Date Arrival Date  
73       500       127500.00                  30 2011-10-20   2011-10-27  
61       550       121000.00                  45 2011-10-09   2011-10-14  
70       500       110000.00                  45 2011-10-15   2011-10-20  
15       406       103530.00                  30 2011-09-01   2011-09-10  
72       150        96750.00                  30 2011-10-15   2011-10-26  
..       ...             ...                 ...        ...          ...  
84       525          525.00                  30 2011-11-01   2011-11-07  
89       550          467.50                  30 2011-11-05   2011-11-11  
12       500          375.00                  30 2011-08-25   2011-08-31  
85       150           82.50                  30 2011-11-01   2011-11-06  
93       125           68.75                  30 2011-11-05   2011-11-10  

[94 rows x 10 columns]
