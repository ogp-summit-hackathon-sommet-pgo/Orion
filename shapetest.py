import shapefile
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sf = shapefile.Reader("3DMassing_2018_WGS84")

shapes = sf.shapes()
records = sf.records()

print(len(shapes))
print(len(records))

print(len(records[0]))

for rec in records[0]:
    print(rec)

totalArea = 0

columns = ["MAX_HEIGHT", "X", "Y", "SHAPE_AREA"]
           
df = pd.DataFrame(columns = columns, index = range(len(records)))

for index, record in enumerate(records):
    totalArea += record[12]
    #df.iloc[index] = record
    df.at[index, "MAX_HEIGHT"] = record[1]
    df.at[index, "X"] = record[7]
    df.at[index, "Y"] = record[8]
    df.at[index, "SHAPE_AREA"] = record[12]
    print(index)
    
print(totalArea)
print(df)

df1 = df.sample(n = 10000)

threedee = plt.figure().gca(projection = '3d')
threedee.scatter(df1["X"].head(10000), df["Y"].head(10000), df["SHAPE_AREA"].head(1000))
threedee.set_xlabel('X')
threedee.set_ylabel('Y')
threedee.set_zlabel('SHAPE_AREA')
plt.show()

#df.to_csv("3DMassing_2018_WGS84.csv")