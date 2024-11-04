# Argumentos variables para un diccionario
# Definición de función
# El parámetro para poder recibir el diccionario completo es **. 
# Lo más utilizado es **kwargs para recibir argumentos
# kwargs -> key word argument
def listarTerminos(**terminos):
    for llave, valor in terminos.itrms():
        print(f'{llave} : {valor}')

# No se mostrará nada
listarTerminos()

# Se pueden iniciar varios tipos de datos (menos números)
listarTerminos(IDE = 'Integrated Develoment Enviroment', PK = 'Primary Key')
listarTerminos(Nombre = 'Leonel Messi')
