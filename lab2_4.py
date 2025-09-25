import pandas as pd
import numpy as np

df = pd.read_excel("MobiSortIt_data.xlsx")

missed_v=df.isnull().sum()
percent_v= np.round(df.isnull().sum() / len(df) * 100, 2)

print("Missed values:", missed_v)
print("% missed values:",percent_v)

OUTPUT:
Missed values: ticketid              0
category              0
Similar_Problems      0
duration_days       126
status                7
issuetype             0
privateproperty       0
assignment           27
dtype: int64
% missed values: ticketid            0.00
category            0.00
Similar_Problems    0.00
duration_days       8.61
status              0.48
issuetype           0.00
privateproperty     0.00
assignment          1.84
dtype: float64
