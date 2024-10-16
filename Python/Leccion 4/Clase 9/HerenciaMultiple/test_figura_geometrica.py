from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5,"Azul")
rectangulo1 = Rectangulo(2,6,"Rojo")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"El area es: {cuadrado1.calcular_area()}")

# MRO = METHOD RESOLUTION ORDER
# [<class 'Cuadrado.Cuadrado'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 'Color.Color'>, <class 'object'>]
# nos dice que va a CUADRADO, luego a FIGURA, luego a COLOR, y ultimo obviamente a la CLASE OBJECT
print(Cuadrado.mro()) 

print(cuadrado1)
print(rectangulo1)