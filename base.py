# Author : Prityush Bansal
# May 26, 2022 : 16:24

import numpy as np
import pandas as pd

df = pd.read_csv("dataset.csv")
print("Dataframe head is \n", df.head())
print("\n\nInfo for dataframe is as follows : ")
print(df.info())
print("\n\nCount for each type :\n", df['type'].value_counts())
# so there are no null values in the dataset, but our dataset is very
# imbalanced which can be seen through the value count
