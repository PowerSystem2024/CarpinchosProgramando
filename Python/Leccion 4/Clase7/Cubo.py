class Cubo:
    def __init__(self,ancho,altura,profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
    
    def calcularVolumen(self):
        return self.ancho * self.altura * self.profundidad
    
ancho = int(input("Ingrese ancho: "))
altura = int(input("Ingrese altura: "))
profun = int(input("Ingrese profundidad: "))

c1 = Cubo(ancho,altura,profun)

print(c1.calcularVolumen())