import pandas as pd
import numpy as np

df=pd.read_csv("hmeq.csv")


col_row=df.shape
col_name=df.columns
col_type=df.dtypes
non_null=df.notna().sum()

print("Data info:")  
df.info()
print ("Column and rows count:", col_row)
print("Columns' names:", col_name)
print("Columns types:", df.dtypes)
print("Not null count:", non_null)
