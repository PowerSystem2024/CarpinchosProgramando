from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho,alto,color):
    #   super().__init__(lado,lado)
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self): # SIRVE PARA SOBREESCRIBIR
        return f"Rectangulo: [{FiguraGeometrica.__str__(self)} {Color.__str__(self)}]"