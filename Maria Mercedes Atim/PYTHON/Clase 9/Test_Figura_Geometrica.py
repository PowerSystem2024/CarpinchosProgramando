from Cuadrado import Cuadrado # del archivo Cuadrado importa la clase Cuadrado
from Rectangulo import Rectangulo

print("Creacion de objeto clase Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(8, "Azul") # Instanciamos un nuevo objeto Cuadrado
cuadrado1.alto = -10 # Por las validaciones no se va a modificar
cuadrado1.alto = 7
cuadrado1.ancho = 7
print(cuadrado1.ancho) # Mostramos el ancho
print(cuadrado1.alto) # Mostramos el alto
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")
# MRO Method Resolution Order
print(Cuadrado.mro())
print(cuadrado1)
print("")
print("Creacion de objeto clase Rectangulo".center(50, "-"))
# Instanciamos un objeto Rectángulo:
rectangulo1 = Rectangulo(3, 9, "Verde")
rectangulo1.ancho = 15  # Por las validaciones no se va a modificar
rectangulo1.ancho = 8
print(Rectangulo.mro())
print(rectangulo1)

# figura1 = FiguraGeometrica() No se puede instanciar, es abstracta