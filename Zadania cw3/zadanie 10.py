def lista(**ilosc):
    suma=0;
    for cos in ilosc:
        if (ilosc[cos])!=0:
            suma += ilosc[cos]
        else:
            suma+=1
    return suma
print(lista(chleb=2, bulki=2))