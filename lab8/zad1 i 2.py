import pandas as pd 
import numpy as np 
import xlrd
import openpyxl
#DataFrame
data = pd.ExcelFile('imiona.xlsx')
imiona= pd.read_excel('imiona.xlsx','Arkusz1')
#wyswietlanie:nadanie imion >1000 w danym roku
print(imiona[imiona.Liczba>1000])
#rekordy gdzie imie jest Bartosz
print(imiona[imiona.Imie=='BARTOSZ'])
#suma wszystkich urodzonych dzieci w calym danym okresie
print(sum(imiona.Liczba))
#sumę dzieci urodzonych w latach 2000-2005
print(sum(imiona.Liczba[imiona.Rok<=2005] & imiona.Liczba[imiona.Rok>=2000]))
#sumę urodzonych chłopców i dziewczynek
print(sum(imiona.Liczba))
#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)    
p=imiona.sort_values("Liczba", ascending=False).groupby(['Rok',"Plec"]) 
for i,g in enumerate(p,start=1):
    print(f"{g[0]}")
    print(f"{g[1].iloc[[0],[1]].values[0][0]}", end=" ")
    print(f"{g[1].iloc[[0],[2]].values[0][0]}")
#najbardziej popularne imię dziewczynki i chłopca w całym danym okresie
dz=imiona[imiona['Plec']=='K']
dz_max=imiona[imiona['Plec']=='K'].max()
print(dz[(dz['Liczba']==dz_max['Liczba'])])
ch=imiona[imiona['Plec']=='M']
ch_max=imiona[imiona['Plec']=='M'].max()
print(ch[(ch['Liczba']==ch_max['Liczba'])])