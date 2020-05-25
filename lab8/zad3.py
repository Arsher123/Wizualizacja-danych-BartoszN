import pandas as pd
import numpy as np 
import xlrd
import openpyxl
import datetime
zamowienia = pd.read_csv("zamowienia.csv",delimiter=";")
#listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
print(zamowienia.Sprzedawca.unique())
#5 najwyższych wartości zamówień
a=zamowienia.sort_values('Utarg',ascending=False)
print(a.iloc[:5])
#ilość zamówień złożonych przez każdego sprzedawcę
print(zamowienia.groupby(['Sprzedawca']).agg({'idZamowienia':['count']}))
#sumę zamówień dla każdego kraju
print(zamowienia.groupby(['Kraj']).agg({"idZamowienia":['count']}))
#sumę zamówień dla roku 2005, dla sprzedawców z Polski
c=zamowienia[(zamowienia['Data zamowienia']>='2005-01-01')&(zamowienia['Data zamowienia']<='2005-12-31')& (zamowienia['Kraj']=='Polska')]
c.groupby(['Kraj']).count
print(c['idZamowienia'])
#średnią kwotę zamówienia w 2004 roku
d = zamowienia[(zamowienia['Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] <= '2004-12-31')].mean()
print(d['Utarg'])
#zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
x2004 = zamowienia[(zamowienia['Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] <= '2004-12-31')]
x2005 = zamowienia[(zamowienia['Data zamowienia'] >= '2005-01-01') & (zamowienia['Data zamowienia'] <= '2005-12-31')]
x2004.to_csv('Ćwiczenia8/zamowienia_2004.csv')
x2005.to_csv('Ćwiczenia8/zamowienia_2005.csv')