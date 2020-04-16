class Slowa:
    def __init__(self,x,y):
        self.wyraz1=x
        self.wyraz2=y
    def sprawdz_czy_palindrom(self):
        if (len(self.wyraz1)%2==0):
            for i in range(0,int(len(self.wyraz1)/2-1)):
                if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                    return print("slowa nie jest palindromem")
        else:
            for i in range(0,int((len(self.wyraz1)-1)/2)):
                if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                    return print("slowa nie jest palindromem")
        return print("slowo jest palindromem")
    def sprawdz_czy_metagramy(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print("slowa nie sa metagramami")
        else:
            licz=0
            for i in range(0,len(self.wyraz1)-1):
                if(self.wyraz1[i]!=self.wyraz2[i]):
                    licz+=1
                    if(licz>1):
                        return print("slowa nie sa metagramami")
            if (licz!=1):
                return print("slowa nie sa metagramami")
        return print("slowa sa metagramami")
    def sprawdz_czy_anagram(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print("slowa nie sa anagramami")
        else:
            for i in range(0,len(self.wyraz2)):
                if (self.wyraz1.count(self.wyraz1[i])!=self.wyraz1.count(self.wyraz1[i])):
                    return print("slowa nie sa anagramami")
        return print("slowa sa anagramami")
    def wyswietl_wyraz(self):
        print(self.wyraz1)
        print(self.wyraz2)
slowo=Slowa("kajak","tata")
slowo.sprawdz_czy_palindrom()
slowo.sprawdz_czy_metagramy()
slowo.sprawdz_czy_anagram()
slowo.wyswietl_wyraz()