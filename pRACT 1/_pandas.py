import pandas as pd
import numpy as np  # Corrected import for numpy

# Creating a numpy array of strings
info = np.array(['p', 'a', 'n', 'd', 'a', 's'])
b = pd.Series(info)
print(b)

# a list of strings
x = ['Python', 'Pandas']
# Calling DataFrame constructor on the list
df = pd.DataFrame(x, columns=['Language'])  # Optional column name
print(df)
