# Dada la siguiente tupla tupla = (13, 1, 8, 3, 2, 5, 8) Crear una lista que solo incluya los números menos a 5.
# La ejecución debe mostrar: [1, 3, 2]

tupla = (13, 1, 8, 3, 2, 5, 8)

listaMenorA5 = [numero for numero in tupla if numero < 5] # El for va a iterar numero por numero en la tupla y va a guardar todos los numeros menores a 5 en la lista listaMenorA5.
print(listaMenorA5)