import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

x = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel('imiona.xlsx','Arkusz1')

plec=imiona.groupby(['Plec']).agg(sum)['Liczba']

plt.subplot(1,3,1)
plt.xlabel('x')
plt.ylabel('y')
plt.bar(['K','M'],[plec[0],plec[1]])


K=(imiona.groupby(['Plec','Rok']).agg(sum).loc['K'])['Liczba']
M=(imiona.groupby(['Plec','Rok']).agg(sum).loc['M'])['Liczba']

plt.subplot(1,3,2)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(K.index.values,K.values, label='Kobiety')
plt.plot(M.index.values,M.values, label='Mężczyżni')
plt.legend(loc='lower right')

sumaur = imiona.groupby(['Rok']).agg(sum)['Liczba']

plt.subplot(1,3,3)
plt.xlabel('x')
plt.ylabel('y')
plt.bar(sumaur.index.values,sumaur.values)



plt.show()