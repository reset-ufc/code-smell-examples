### Pandas Column Selection
import pandas as pd
df = pd.read_csv('data.csv')
df = df[['col1', 'col2', 'col3']] # +

### Pandas Set DataType
import pandas as pd
# - df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', dtype={'col1': 'str', 'col2': 'int', 'col3': 'float'}) # +