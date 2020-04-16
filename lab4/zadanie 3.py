with open("zad3.txt","w+") as plik:
    plik.write("Ala ma kota,")
    plik.write("a kot ma Ale")
    for i in plik:
        print(i,end="")
    
with open("zad3.txt","r") as plik:
    odczyt=plik.readline()
    print(odczyt)
        
    