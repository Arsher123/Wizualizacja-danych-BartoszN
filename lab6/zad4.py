import numpy as np
a=input("podaj liczbe : ")
a=int(a)
b=input("podaj liczbe ile liczb ma wyswietlic: ")
b=int(b)
def generuj(a,b):
    y=np.logspace(a-1,b,num=b,base=a,dtype="int64",endpoint=True)
    return y
n=generuj(a,b)
print(n)