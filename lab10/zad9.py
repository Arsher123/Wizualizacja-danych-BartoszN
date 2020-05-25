import pandas as pd 
import matplotlib.pyplot as plt

a = pd.read_csv('zamowienia.csv', delimiter=';')
ile=a.groupby(['Sprzedawca']).count()['idZamowienia']

plt.pie(ile, labels=ile.index.values, autopct = lambda pct: "{:.1f}%".format(pct), shadow = True, explode =(0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,))
plt.legend(title='Sprzedawcy', loc = 4, framealpha=0.5)
plt.show()