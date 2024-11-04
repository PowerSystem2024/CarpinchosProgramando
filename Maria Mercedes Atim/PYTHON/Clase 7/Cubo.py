class Cubo:
    """
    Creae clase cubo con los atributos, ancho, largo y profundidad, con un método calcularVolumen() que tendrá la formula:
    volumen = ancho * altura * profundidad
    Los valores deberan ser ingresados por el usuario.
    """
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
    
    def calcularVolumen(self):
        volumen = self.ancho * self.altura * self.profundidad
        return volumen
    
# Solicitamos al usuario los valores e instanciamos un objeto:

ancho = int(input("Ingrese el ancho del cubo: "))
altura = int(input("Ingrese la altura del cubo: "))
profundidad = int(input("Ingrese la profundidad del cubo: "))

cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo, ancho: {ancho} x altura: {altura} x profundidad: {profundidad} es: {cubo1.calcularVolumen()}")