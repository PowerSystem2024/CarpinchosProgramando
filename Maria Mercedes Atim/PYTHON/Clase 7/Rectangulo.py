class Rectangulo:
    """
    Crear una clase Rectangulo. Debe tener como atributo: altura y base.
    El nombre del metodo sera calcularArea() usando la formula:
    area= base * altura.
    Base y altura deben ser ingresados por el usuario.
    Se deben crear 3 objetos
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = self.base * self.altura
        return area
    
# Solicitamos los datos al usuario e Instanciamos 3 objetos.

base = int(input("Ingrese la base del rectángulo 1: "))
altura = int(input("Ingrese la altura del rectángulo 1: "))

rectangulo1 = Rectangulo(base, altura)
print(f"El calculo del área de {base} x {altura} del rectangulo1 es: ", rectangulo1.calcularArea())

base = int(input("\nIngrese la base del rectángulo 2: "))
altura = int(input("Ingrese la altura del rectángulo 2: "))

rectangulo2 = Rectangulo(base, altura)
print(f"El calculo del área de {base} x {altura} del rectangulo2 es: ", rectangulo2.calcularArea())

base = int(input("\nIngrese la base del rectángulo 3: "))
altura = int(input("Ingrese la altura del rectángulo 3: "))

rectangulo3 = Rectangulo(base, altura)
print(f"El calculo del área de {base} x {altura} del rectangulo 3 es: ", rectangulo3.calcularArea())