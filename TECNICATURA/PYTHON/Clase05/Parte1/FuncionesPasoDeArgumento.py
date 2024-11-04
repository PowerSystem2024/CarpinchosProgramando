# Funciones: Paso de Argumentos
# Definición de función
def miFuncion(name, lastName):
    print("Saludos al profe si lee este archivo de Python. \n")
    print(f'Nombre: {name}, Apellido: {lastName}')

# Parámetros -> Son las variables que se declaren en la función
# Argumentos -> Es el valor que se le envía a la función

# Se manda a llamar la función y se pasan los argumentos
# Para evitar errores, a la hora de llamar a la función hay que pasarle los argumentos
# La función se puede llamar reiteradas veces pero con diferentes argumentos 
miFuncion('Nicolás', 'Mercado')
miFuncion('Wanda', 'Lanatta')
miFuncion('Mariana', 'Aguilera')
