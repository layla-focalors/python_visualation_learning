class Exclass():
    def __init__ (self, data1, data2):
        self.r = data1
        self.i = data2
        # self = return과 비슷한 역할, 단 __init__에서
        # init은 return이 없음

x = Exclass(3.14, 2.73)
print(x.r, x.i)