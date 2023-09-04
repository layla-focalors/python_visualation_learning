import pandas as pd
import numpy as np

# np.nan = 데이터가 존재하지 않음
df = pd.DataFrame({'name': ['Noa', 'Artsnoa', 'ARIS', 'layla', 'focalors'], 'age': [20, 20, 10, 15, np.nan], 'height': [160, 170, 175, 165, 166]})
print(df)

df['rank_avr'] = df['age'].rank(method='min', ascending=False, na_option='bottom')
print(df)
# 나이가 적은 순서대로 붙이기

df['rank_height'] = df['height'].rank(method='min', ascending=False, na_option='top')
print(df)

# df 추가 , df[칼럼] = 데이터
df['hello_level'] = [29,10,19,11,11]
print(df)

# 이때, 데이터의 양은 반드시 위의 정의값과 동일해야 함
# ascending = 오름차순