### Pandas
import pandas as pd
df = pd.DataFrame([1, 2, 3])
''' - result = []
- for index, row in df.iterrows():
- 	result.append(row[0] + 1)
- result = pd.DataFrame(result)
'''
result = df.add(1) # + 
print(result)