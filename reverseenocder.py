import reverse_geocoder as rg 
import pprint 
from collections import OrderedDict
import pandas as pd
import numpy as np

df = pd.read_csv('3DMassing_2018_WGS84.csv')

for frame in df.head():
  print(rg.search((frame[2], frame[3])))
  
df.to_csv('output.csv')

#coordinates =(43.66030373, -79.59226603) 
#result = rg.search(coordinates)  
#print(dict(result[0])['name'])



#pprint.pprint(json.dumps(result)) 




#print(df)
