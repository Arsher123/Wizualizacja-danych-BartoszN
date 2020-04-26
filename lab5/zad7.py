class parzystyindeks:
    def __init__(self, cos):
        self.cos = cos
        self.index = -2
    
    def __iter__(self):
        return self

    def __next__(self):
        a=len(self.cos)
        if a%2 != 0:
            a=a-1
        if self.index>=a:
            raise StopIteration
        self.index=self.index +2 
        return self.cos[self.index]
Bartek=parzystyindeks("2504045")
print(list(Bartek))
