import scipy as sp
import numpy as np
import statistics as st
import math
# 특이점, sp는 "a"가 붙음

data = np.array([96, 80, 79, 96, 88, 75, 78, 89, 92, 70])
# 평균
print(f"mean : {sp.mean(data)}")
# 주의, mean은 2.0.0에서 삭제, 즉 numpy mean, math mean 권장

print(f"numpy_mean : {np.mean(data)}")
print(f"statistics_mean : {st.mean(data)}")

# 최대값
print(f"max : {sp.amax(data)}")
print(f"numpy_max : {np.max(data)}")
print(f"default_max : {max(data)}")

# 최소값
print(f"min : {sp.amin(data)}")
print(f"min : {np.amin(data)}")
print(f"default_min : {min(data)}")

# 분산 
print(f"var : {sp.var(data)}")
print(f"numpy_var : {np.var(data)}")

# 분산 세부,
# ddof가 0이면, 최대우도분산추정량, ddof가 1이면, 분편분산추정량

# 표준편차
print(f"std : {sp.std(data)}")
print(f"numpy_std : {np.std(data)}")

# 뮤(mu)
addon = np.sum(data)
mx = addon / (len(data))
print(f"mu : {mx}")

# 시그마 (sigma)
sigma2 = np.var(data)
sigma = np.sqrt(sigma2)
print(f"sigma : {sigma}")