from FiguraGeometrica import FiguraGeometrica #Primero va el modulo/archivo y despues del import va la clase
from Color import Color

class Cuadrado(FiguraGeometrica, Color): # La clase Cuadrado es hija de FiguraGeometrica y Color
    def __init__(self, lado, color):
        # super().__init__(lado, color)
        FiguraGeometrica.__init__(self, lado, lado) # Inicializa la clase FiguraGeometrica con lado como ancho y alto
        Color.__init__(self, color) # Inicializa la clase Color con el color especificado

    def calcular_area(self):
        return self.alto*self.ancho # Calcula y retorna el área del cuadrado
    
    def __str__(self):
        # Devuelve una representación en forma de cadena del cuadrado con el calculo de area
        return f'Cuadrado de lado {self.ancho}, color: {self.color}, área: {self.calcular_area()}'