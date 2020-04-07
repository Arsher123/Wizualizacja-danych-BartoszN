def lista(**ilosc):
    suma=0;
    for cos in ilosc:
        if isinstance (ilosc[cos],list):
            suma += len(ilosc[cos])
        else:
            suma+=1
    return suma
print(lista(slodycze="cukierki", pieczywo=["chleb","bulki"]))