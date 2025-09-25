import pandas as pd
import numpy as np

df = pd.read_excel("MobiSortIt_data.xlsx")
print("2ND ROW:")
print(df.iloc[[1]]) 
print()

print("1ST COLUMN:")
print(df.iloc[:, 0])  
print()

print("3RD ROW, 2ND COLUMN:")
print(df.iloc[2, 1])  

OUTPUT:
2ND ROW
   ticketid     category Similar_Problems  duration_days    status  \
1         2  Electricity               No            1.0  Assigned   

    issuetype  privateproperty   assignment  
1  Burst Pipe                1  Electricity  

1ST COLUMN
0          1
1          2
2          3
3          4
4          5
        ... 
1459    1460
1460    1461
1461    1462
1462    1463
1463    1464
Name: ticketid, Length: 1464, dtype: int64

3RD ROW, 2ND COLUMN
Electricity

