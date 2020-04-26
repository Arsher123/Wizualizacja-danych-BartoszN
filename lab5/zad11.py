def fibb(n):
    a = 0 
    b = 1
    for i in range(n):
        a = b 
        b = a + b
        yield a
x=fibb(10)
print(x)
