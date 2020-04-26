class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"
class kwadrat(Ksztalty):
    def __init__(self,x):
        self.x=x
        self.y=x
    def __str__(self):
        return "kwadrat o boku {}".format(self.x)
    def __add__(self,other):
        return kwadrat(self.x+other.x)
kw=kwadrat(5)
kw1=kwadrat(6)
print(kw)
print(kw1)
print (kw +kw1)