import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6]])
col = 1
x = 0
# - df[col][x] = 42
df.loc[x, col] = 42 # +