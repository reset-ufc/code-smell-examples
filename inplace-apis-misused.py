import pandas as pd
df = pd.DataFrame([-1])
# - df.abs()
df = df.abs() # +

### NumPy
import numpy as np
zhats = [2, 3, 1, 0]
# - np.clip(zhats, -1, 1)
zhats = np.clip(zhats, -1, 1) # +