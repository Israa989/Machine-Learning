import pandas as pd
import numpy as np
array_Number=np.array([[23,5,3],[5,7,9]])
df=pd.DataFrame(array_Number,index=['A','B'],columns=['A1','B1','C1'])
df['D1']="Israa"
print(df)
print(df[['A1','C1']])
print(df.iloc[1:2])
print(df.iloc[1,2])
print(df.shape)
print(df.dtypes)