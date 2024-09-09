# Se solicita calcular el área y el perímetro de un rectángulo. Para ello, es necesario crear las siguientes variables:
#   alto (int)
#   ancho (int)
# El usuario debe proporcionar los valores de alto y ancho, después se debe imprimir el resultado en el siguiente formato:
#   Proporciona el alto del rectángulo: 5
#   Proporciona el ancho del rectángulo: 3
#   Área: 15
#   Perímetro: 16
#FÓRMULAS NECESARIAS
#   Área = Alto * Ancho y Perímetro = (Alto+Ancho)*2

alto = int(input("Escriba del ALTO del rectángulo:"))
ancho = int(input("Escriba del ANCHO del rectángulo:"))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"El el área del rectángulo es de: {area}")
print(f"El el perímetro del rectángulo es de: {perimetro}")
