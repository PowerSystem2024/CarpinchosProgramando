print("---- UNION DE CONJUNTOS: ----")
conjunto1 = {"bye", "Hola"}
conjunto2 = {7,"Hola"}
conjunto3 = conjunto1 | conjunto2 # Se usa la pleca para unir dos conjuntos
print(conjunto3)

print("\n---- MUESTRA LOS ELEMENTOS EN COMUN ENTRE LOS DOS CONJUNTOS: ----")
conjunto3 = conjunto1 & conjunto2
print(conjunto3)

print("\n---- MUESTRA LOS ELEMENTOS EN EL CONJUNTO1 Y NO EN EL CONJUNTO2: ----")
conjunto3 = conjunto1 - conjunto2
print(conjunto3)

print("\n---- MUESTRA LOS ELEMENTOS QUE NO COMPARTEN LOS CONJUNTOS: ----")
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)