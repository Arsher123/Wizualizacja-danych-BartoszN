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
    #obsulugje operator <
    def __lt__(self,other):
        return other.x
    #obsulugje operator >=
    def __ge__(self,other):
        return self.x
    #obsluguje operator  >
    def __gt__(self,other):
        return self.x
    #obsulugje operator <=
    def __le__(self,other):
        return self.x

kw=kwadrat(5)
kw1=kwadrat(6)
print(kw)
print(kw1)
print(kw<kw1)
print(kw>kw1)
print(kw>=kw1)
print(kw<=kw1)