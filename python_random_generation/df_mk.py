import pandas as pd
import numpy as np
df = pd.DataFrame({'index1':['a','b','c','d','e'], 'index2':[1,3,5,2,2], 'var1':np.arange(5)})

print(df)

print(f"df의 (var1) 평균 : {df['var1'].mean()}")
# df는 데이터에서 행, 열로 저장하며 database sql과 유사함
# print(f"df의 가로 평균 : {df.mean(axis=1)}")
# 데이터가 숫자로 적용된 경우 사용

# 가로 : axis = 1, 세로 axis = 0

