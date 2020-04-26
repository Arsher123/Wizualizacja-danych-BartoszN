import itertools

def x():
    list = [1,2,3,4,5,6,7,8,9,10]
    for i in itertools.combinations(list,3):
        yield print(i)

x=x()
while(x != 0):
    next(x)