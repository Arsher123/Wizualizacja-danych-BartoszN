lista=[]
for i in range(0,100):
    if i%4==0:
        lista.append(i) 
plik = open("zad1.txt","a")
plik.writelines(str(lista))
plik.close()