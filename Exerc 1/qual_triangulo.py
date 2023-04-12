class Triangulo: 
    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        self.c = 0
    
    def invalido(self, a,b,c):

        self.a = a
        self.b = b
        self.c = c 

        if self.a < 0 or self.a > 1000000:
            return True
        if self.b < 0 or self.b > 1000000:
            return True
        if self.c < 0 or self.c > 1000000:
            return True
        
        if abs(self.a - self.b) < self.c and abs(self.a - self.c) < self.b and abs(self.b - self.c) < self.a:
            return False
        else:
            return True

    def tipo(self,a,b,c):

        self.a = a
        self.b = b
        self.c = c 

        if (a == b) and (b == c) and (a == c) :
            return "Equilatero"
        if (self.a == self.b) or (self.b == self.c) or (self.a == self.c): 
            return "Isosceles"        
        else:
            return "Escaleno"
    
    def retangulo(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 

        if (self.a**2 == self.b**2 + self.c**2) or (self.b**2 == self.a**2 + self.c**2) or (self.c**2 == self.a**2 + self.b**2):
            return True
        else:
            return False







    
    
    
    
    
