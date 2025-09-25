import pandas as pd
import numpy as np

df = pd.read_excel("MobiSortIt_data.xlsx")

dest_stat=df.describe(include='all')
print(dest_stat)

OUTPUT:
  ticketid category Similar_Problems  duration_days    status  \
count   1464.00000     1464             1464    1338.000000      1457   
unique         NaN        6                3            NaN         3   
top            NaN    Water              Yes            NaN  Assigned   
freq           NaN      677              538            NaN      1174   
mean     732.50000      NaN              NaN      11.421525       NaN   
std      422.76471      NaN              NaN      12.506222       NaN   
min        1.00000      NaN              NaN       0.000000       NaN   
25%      366.75000      NaN              NaN       1.000000       NaN   
50%      732.50000      NaN              NaN       4.000000       NaN   
75%     1098.25000      NaN              NaN      30.000000       NaN   
max     1464.00000      NaN              NaN      30.000000       NaN   

         issuetype  privateproperty    assignment  
count         1464      1464.000000          1437  
unique          34              NaN             6  
top     Burst Pipe              NaN  DEIS - Water  
freq           337              NaN           670  
mean           NaN         0.284836           NaN  
std            NaN         0.451491           NaN  
min            NaN         0.000000           NaN  
25%            NaN         0.000000           NaN  
50%            NaN         0.000000           NaN  
75%            NaN         1.000000           NaN  
max            NaN         1.000000           NaN  

