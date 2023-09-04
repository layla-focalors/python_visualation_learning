import numpy as np
# map : 데이터 객체에 대한 특정 함수를 적용한다
x = [1,2,3]
y = [2,5,6]
x = map(len, x, y)

print(x)

