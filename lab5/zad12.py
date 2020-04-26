def miesiace(list):
    for index in range(0,12):
        yield print(list[index])


list = ['Styczen',"Luty", "Marzec", "Kwiecień","Maj","Czerwiec","lipiec",
    "sierpień","Wrzesień","Październik","listopad","grudzień"]

x=miesiace(list)

for i in range(0,12):
    next(x)