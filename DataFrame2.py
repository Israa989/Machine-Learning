import pandas as pd
import numpy as np
arr=np.random.randn(25)
print(arr)
df=pd.DataFrame(arr)
print(df)
df=pd.DataFrame((arr).reshape(5,5))
print(df)
df=pd.DataFrame((arr).reshape(5,5),index=['A','B','C','D','E'],columns=['A1','B1','C1','D1','E1'])
print(df)
print(df.drop('D'))
print(df.drop('B1',axis=1))