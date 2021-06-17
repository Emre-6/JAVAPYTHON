import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values
from sklearn.preprocessing import Imputer
