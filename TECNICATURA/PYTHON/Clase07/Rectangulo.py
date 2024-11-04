class Rectangulo:
    """
    Crear una clase llamada Rectangulo,debe tener 2 atributos: altura y base
    el nombre del método será calcular_área utilizando la fórmula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben
    ser tres
    """

    def __init__(self , altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base
#Figura 1
base = int(input('Ingrese la medida de la base del rectángulo: '))
altura = int(input('Ingrese la medida de la altura del rectángulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El área del rectángulo es: {rectangulo1.calcular_area()}')

#Figura 2
base = int(input('Ingrese la medida de la base del rectángulo2: '))
altura = int(input('Ingrese la medida de la altura del rectángulo2: '))
rectangulo2 = Rectangulo(base, altura)
print(f'El área del rectángulo es: {rectangulo2.calcular_area()}')

#Figura3
base = int(input('Ingrese la medida de la base del rectángulo3: '))
altura = int(input('Ingrese la medida de la altura del rectángulo3: '))
rectangulo3 = Rectangulo(base, altura)
print(f'El área del rectángulo es: {rectangulo3.calcular_area()}')
