# Ejercicio: Conjunto de Calificaciones
# Suponga que tiene un conjunto de calificaciones de un grupo de 10 alumnos.
# Realizar un algoritmo para calcular la calificacion promedio  y la calificación más baja de todo el grupo.

def calcularPromedio(calificaciones):
    total = sum(calificaciones)
    return total / len(calificaciones)

def calcularCalificacionMasBaja(calificaciones):
    return min(calificaciones)

calificaciones = []

for i in range(1, 11):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    calificaciones.append(calificacion)

promedio = calcularPromedio(calificaciones)

calificacionMasBaja = calcularCalificacionMasBaja(calificaciones)

print("El promedio de calificaciones es: ", promedio)
print("La calificación más baja es: ", calificacionMasBaja)
