def main():
    """PARAMETRY: ...""" #TZW docstring
# dlugaNazwaFunkcji pisze sie jako dluga_nazwa_funckji
#Guido van Rossum
# pep8 pep0008
#ctrl + "/" -ustaw/usun komentarz
# shift +alt + strzalka do gory do dolu - kopiuje to co na gorze/dole

# łancuch znakow  
imie = "ALa"
imie = "ALa"
imie ="""ALA ma 
kota a 
kot ma ale """
imie = 1
imie = 5.6
print(type(imie))
#<class 'str'>
imie =str("Ala") #poprzez konstruktor
#instance() sprawdzam czy zmienna jest danego typu
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

print(type(5))
print(type(5.6))
print(type(True))
print(type(None))

print("ALA " + "ma kota ")
#print("Ala" + "ma" + 5 + "kotow") - blad
ilosc_kotow = 5 
print("Ala" + "ma {} + kotow".format(ilosc_kotow))
print(f"Ala ma {ilosc_kotow} kotow")
print("Ala ma {1} {0} {2} kotow".format(4, 5, 7))
liczba = 6.87654347
# print(f"liczba {: .2f}") #2 miejsca po przecinku 

#http://pyformat.info

print(imie[1]) #wypisanie 2 litery z ciagu znakow 
# imie[0] = "0" nie jest mutowalny
imie = imie.lower()
print(imie)

# LICZBY 

liczba = 1
liczbaf = 4.5
suma = liczba + liczbaf
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 // 2) #dzielenie bez reszty 
print(1 ** 2) # do potegi 
print(1 % 2) #dzielenie modulo "reszta"

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.30f}")

#LISTA 

lista = []
lista2 = [1, 2, 3] 
lista3 = [1, "ala", 3.4, True, None]
final_list = lista + lista2 + lista3
lista2[2] #wartosc 3 indeks 2 
lista4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lista4[1][1] #zwraca wartosc 5 z listy 4


#slownik 

slownik = {}
slownik2 = {"klucz": "wartosc"}
slownik3= {0: "adam"}
#slownik2{"klucz"} = "costam"
slownik3[0]
slownik2.keys()
slownik2.values()