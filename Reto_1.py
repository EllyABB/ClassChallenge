

class mother:
    
    def __init__(self,number):
        self.n=number
    
    def __str__(self):
        return f"The number is {self.n}"
    
    def longitud(self):
        return len(str(self.n))
    
    def split(self):
        return [x for x in str(self.n)]
    
    def Potencia(self,a):
        return self.n**a
    
class SumaDeCubos(mother):
    def __init__(self,number):
        super().__init__(number) 
    
    def suma(self):
        s=0
        for x in self.split():
            self.n=int(x)
            s=s+self.Potencia(3)
        return s
    
class SumaDeCuadrados(mother):
    def __init__(self,number):
        super().__init__(number) 
    
    def suma(self):
        s=0
        for x in self.split():
            self.n=int(x)
            s=s+self.Potencia(2)
        return s
num=input("Choose your number = ")
a=SumaDeCubos(num)
b=SumaDeCuadrados(num)
print(a.suma()+b.suma())