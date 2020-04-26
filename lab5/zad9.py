class it:
    def __init__(self,data):
        self.data=data
        self.index = -1
        self.sam = ['a','e','i','o','u','y']
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.data)-1:
            raise StopIteration
        self.index=self.index + 1
        if self.data[self.index] in self.sam:
            return self.data[self.index]
bartek=it("bartek")
print(list(bartek))
print(isinstance(bartek,it))
b="qertgbhlnjlkjugtcvfy"
ciag=(litera for litera in b if litera in ['a','e','i','o','u','y'])