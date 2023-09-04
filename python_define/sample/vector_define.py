import numpy as np

studentA = [96, 80, 76, 96, 88, 75, 78, 89, 92, 70]
studentB = [67, 83, 96, 90, 85, 75, 82, 92, 75, 80]

# append - type = list
score = []
score.append(studentA)
score.append(studentB)
print(score)

# use numpy
score2 = np.array([studentA, studentB])
print(score2)
# 정식문법, np.array([[A], [b]])
# 그러나 위에서 이미 리스트로 정의함 = [] 하나 제거

# use numpy low 
scoreA = np.array(studentA)
scoreB = np.array(studentB)

score3 = np.append(scoreA, scoreB)
print(score3)

# 수평결합 ( 동일한 역할! / append )
sc = np.hstack([studentA, studentB])
print(sc)

# hstack = append