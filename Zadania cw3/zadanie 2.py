import random
m=[[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]for i in range(4)]
print(m)
lis=[m[i][j]for i in [0,1,2,3] for j in [0,1,2,3] if i==j]
print(lis)
