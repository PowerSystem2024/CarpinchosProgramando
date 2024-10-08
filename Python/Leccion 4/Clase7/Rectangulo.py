class Rectangulo:
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base

    def calcularArea(self):
        return self.altura * self.base

altura = int(input("Ingrese la altura: "))
base = int(input("Ahora... ingrese la base: "))
rec1 = Rectangulo(altura,base)
rec2 = Rectangulo(3,3)
rec3 = Rectangulo(4,3)

print(rec1.calcularArea())
print(rec2.calcularArea())
print(rec3.calcularArea())