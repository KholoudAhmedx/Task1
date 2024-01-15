import pandas as pd
import numpy as np
import os 


# Read the data from the file
dataframe = pd.read_excel('Dry_Bean_Dataset.xlsx')
#print(dataframe)

# Extract features
X1 = dataframe.loc[:, 'Area']
X2 = dataframe.loc[:, 'Perimeter']
X3 = dataframe.loc[:, 'MajorAxisLength']
X4 = dataframe.loc[:, 'MinorAxisLength']
X5 = dataframe.loc[:, 'roundnes']
print(X1, X2)
Y = dataframe.loc[:, 'Class']
print(Y)