import csv
import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\jdhus\\OneDrive\\Documents\\3DMassing_2018_WGS84_fixed.csv')

df['UNBLOCKED_HEIGHTS'] = df['MAX_HEIGHT'].rolling(window = 10).max()


df.to_csv('C:\\Users\\jdhus\\OneDrive\\Documents\\3DMassing_2018_WGS84_fixed.csv')
