#  List Comprehension: Lista de Comprensión
# Este método sirve para tomar solo lo necesario de una lista sin hacer ningúntipo de modificaciones en la misma

# Creación de una lista de nombres (String)
names = ['Mariana', 'Wanda', 'Nicolás', 'Cirano', 'Melina']

# Se realiza la compresión
alongM = [m for m in names if m[0] == 'M'] # Esto regresa una lista nueva
# m -> Cada elemento en singular
# m para m en names -> Se recorre cada uno de los elementos de la lista 'names'
# if m[0] == 'M' -> Condición en la cuál, si los elementos en adelante es igual a la letra 'm', 
# se regresará a una nueva lista que se guardará en 'alongM'

# Mostrar la lista nueva
print(alongM)

# Este proceso se puede hacer en tuplas y diccionarios
# Diccionario
botellaC = {
    {'name': 'Quilmes', 'country': 'Arg'},
    {'name': 'Corona', 'country': 'Mx'},
    {'name': 'Stella Artois', 'country': 'Belgium'}
}

# Diccionario para guardar lo que se desea mantener a parte
Arg = [b for b in botellaC if b[country] == 'Arg']
# Es lo mismo que antes, se recorre elemento por elemento del diccionario
# La condición se cumple si el elemento que se recorre singularmente dentro de 'country' es igual al valor 
# de Arg, entonces se creará el diccionario con el nombre Arg
print(Arg)
print(botellaC)

