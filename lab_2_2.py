import pandas as pd
import numpy as np

df = pd.read_excel("MobiSortIt_data.xlsx")

categorical_col = ['category', 'Similar_Problems', 'status', 'issuetype', 'privateproperty', 'assignment']
for col in categorical_col:
  print(f"Count of {col}")
  print(df[col].value_counts())
  print()

OUTPUT:
Count of category
category
Water                   677
Electricity             339
Sanitation              282
Roads                   122
Parks and Recreation     24
Other                    20
Name: count, dtype: int64

Count of Similar_Problems
Similar_Problems
Yes         538
No          518
Not Sure    408
Name: count, dtype: int64

Count of status
status
Assigned    1174
Closed       223
Resolved      60
Name: count, dtype: int64

Count of issuetype
issuetype
Burst Pipe                                      337
Leaking Sewage                                  239
Other                                           183
No Water                                        159
Broken street light                             147
No electricity                                  128
Potholes                                         78
Leaking Fire Hydrant                             33
Blocked Sewage                                   23
Low water pressure                               20
Faulty water meter                               14
Exposed electrical cables                        12
Excessive water pressure                         11
Refuse not collected                             10
Stray Animals                                    10
Sinkhole                                          9
Intermittent electricity                          9
Broken/Collapsed electricity pole                 7
Delayed prepaid meter installation                6
Blocked storm-water drainage                      5
Broken/missing road sign                          5
Brown Water                                       4
Dog bites                                         2
Public land fencing                               2
Sewage not collected                              2
Washed away/blocked/flooded portion of road       1
Beautification / planting                         1
Grass cutting                                     1
Broken electricity meter                          1
Bush clearing                                     1
Broken/faulty traffic lights                      1
Smelly water                                      1
No road markings                                  1
Fallen trees                                      1
Name: count, dtype: int64

Count of privateproperty
privateproperty
0    1047
1     417
Name: count, dtype: int64

Count of assignment
assignment
DEIS - Water            670
Electricity             332
DEIS - Sanitation       282
DEIS - Roads            115
Parks and Recreation     29
Fire Department           9
Name: count, dtype: int64

