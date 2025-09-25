
import pandas as pd
import numpy as np

df = pd.read_excel('Purchase Orders.xlsx', sheet_name='Data')

df_filtered = df[df["Cost per order"] > 20000]

print(df_filtered)

OUTPUT:
              Supplier Order No.  Item No.    Item Description  Item Cost  \
0     Hulkey Fasteners  Aug11001      1122  Airframe fasteners       4.25   
1        Alum Sheeting  Aug11002      1243  Airframe fasteners       4.25   
2   Fast-Tie Aerospace  Aug11003      5462  Shielded Cable/ft.       1.05   
3   Fast-Tie Aerospace  Aug11004      5462  Shielded Cable/ft.       1.05   
5   Fast-Tie Aerospace  Aug11006      5462  Shielded Cable/ft.       1.05   
9   Fast-Tie Aerospace  Aug11010      5462  Shielded Cable/ft.       1.05   
15       Alum Sheeting  Sep11002      5417       Control Panel     255.00   
19    Hulkey Fasteners  Sep11006      1122  Airframe fasteners       4.25   
21       Alum Sheeting  Sep11008      1243  Airframe fasteners       4.25   
24    Hulkey Fasteners  Sep11011      1122  Airframe fasteners       4.25   
25    Hulkey Fasteners  Sep11012      5066  Shielded Cable/ft.       0.95   
27    Hulkey Fasteners  Sep11014      1122  Airframe fasteners       4.25   
40   Durrable Products  Sep11027      1369  Airframe fasteners       4.20   
44   Durrable Products  Sep11031      1369  Airframe fasteners       4.20   
45    Hulkey Fasteners  Sep11032      1122  Airframe fasteners       4.25   
47   Durrable Products  Sep11034      1369  Airframe fasteners       4.20   
53    Hulkey Fasteners  Oct11006      1122  Airframe fasteners       4.25   
61   Durrable Products  Oct11014      5454       Control Panel     220.00   
63       Alum Sheeting  Oct11016      1243  Airframe fasteners       4.25   
64       Steelpin Inc.  Oct11017      8008      Machined Valve     645.00   
66        Manley Valve  Oct11019      8148      Machined Valve     655.50   
67    Hulkey Fasteners  Oct11020      1122  Airframe fasteners       4.25   
70   Durrable Products  Oct11023      5454       Control Panel     220.00   
72       Steelpin Inc.  Oct11025      8008      Machined Valve     645.00   
73       Alum Sheeting  Oct11026      5417       Control Panel     255.00   
75       Alum Sheeting  Oct11028      5634          Side Panel     185.00   
76   Durrable Products  Oct11029      5275  Shielded Cable/ft.       1.00   
78  Fast-Tie Aerospace  Oct11031      5689          Side Panel     175.00   
79    Hulkey Fasteners  Oct11032      1122  Airframe fasteners       4.25   
80       Steelpin Inc.  Oct11033      5677          Side Panel     195.00   
81       Steelpin Inc.  Oct11034      8008      Machined Valve     645.00   
83       Alum Sheeting  Oct11036      5634          Side Panel     185.00   
86  Fast-Tie Aerospace  Nov11003      5689          Side Panel     175.00   
88       Steelpin Inc.  Nov11005      5677          Side Panel     195.00   
91  Fast-Tie Aerospace  Nov11008      5689          Side Panel     175.00   
92       Steelpin Inc.  Nov11009      5677          Side Panel     195.00   

    Quantity  Cost per order  A/P Terms (Months) Order Date Arrival Date  
0      19500         82875.0                  30 2011-08-05   2011-08-13  
1      10000         42500.0                  30 2011-08-08   2011-08-14  
2      23000         24150.0                  30 2011-08-10   2011-08-15  
3      21500         22575.0                  30 2011-08-15   2011-08-22  
5      22500         23625.0                  30 2011-08-20   2011-08-26  
9      22500         23625.0                  30 2011-08-25   2011-09-02  
15       406        103530.0                  30 2011-09-01   2011-09-10  
19     15500         65875.0                  30 2011-09-04   2011-09-12  
21      9000         38250.0                  30 2011-09-05   2011-09-12  
24     12500         53125.0                  30 2011-09-05   2011-09-11  
25     25000         23750.0                  30 2011-09-05   2011-09-12  
27     15000         63750.0                  30 2011-09-08   2011-09-15  
40     15000         63000.0                  45 2011-09-25   2011-09-30  
44     14000         58800.0                  45 2011-09-27   2011-10-03  
45     14500         61625.0                  30 2011-09-28   2011-10-03  
47     10000         42000.0                  45 2011-09-29   2011-10-04  
53     18000         76500.0                  30 2011-10-01   2011-10-08  
61       550        121000.0                  45 2011-10-09   2011-10-14  
63     10500         44625.0                  30 2011-10-10   2011-10-17  
64       100         64500.0                  30 2011-10-10   2011-10-21  
66       125         81937.5                  30 2011-10-10   2011-10-17  
67     17000         72250.0                  30 2011-10-11   2011-10-19  
70       500        110000.0                  45 2011-10-15   2011-10-20  
72       150         96750.0                  30 2011-10-15   2011-10-26  
73       500        127500.0                  30 2011-10-20   2011-10-27  
75       150         27750.0                  30 2011-10-25   2011-11-03  
76     25000         25000.0                  45 2011-10-25   2011-10-30  
78       155         27125.0                  30 2011-10-25   2011-11-03  
79     17500         74375.0                  30 2011-10-25   2011-11-03  
80       130         25350.0                  30 2011-10-28   2011-11-07  
81       120         77400.0                  30 2011-10-28   2011-11-04  
83       140         25900.0                  30 2011-10-29   2011-11-04  
86       150         26250.0                  30 2011-11-01   2011-11-09  
88       120         23400.0                  30 2011-11-02   2011-11-13  
91       175         30625.0                  30 2011-11-05   2011-11-15  
92       110         21450.0                  30 2011-11-05   2011-11-17  
/usr/local/lib/python3.12/dist-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
