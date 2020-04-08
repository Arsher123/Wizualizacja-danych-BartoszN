lista={"butelka mleka": "sztuki","ziemniaki":"kilogramy","butelka wody":"sztuki","chlebek":"sztuki","bulki":"sztuki"}
print("lista produktow: ")
print(lista)
sztuki=[key for key in lista.keys() if lista[key]=="sztuki"]
print("lista produktow ktore kupujemy tylko na sztuki: ")
print(sztuki)