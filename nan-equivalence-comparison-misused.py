import pandas as pd
# - import numpy as np

df = pd.DataFrame([1, None, 3])
# - df_is_nan = df == np.nan 
df_is_nan = df.isna() # +
