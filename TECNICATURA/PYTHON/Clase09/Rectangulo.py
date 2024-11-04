from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        # Inicializa el ancho, alto y color del rectángulo
        FiguraGeometrica.__init__(self, ancho, alto)  # Inicializa la parte de FiguraGeometrica
        Color.__init__(self, color)  # Inicializa la parte de Color

    def calcular_area(self):
        # Calcula el área del rectángulo
        return self.ancho * self.alto

    def __str__(self):
        # Devuelve una representación en forma de cadena del rectángulo
        return f'Rectángulo de {self.ancho} de ancho x {self.alto} de alto, Color: {self.color}, Area: {self.calcular_area()}'