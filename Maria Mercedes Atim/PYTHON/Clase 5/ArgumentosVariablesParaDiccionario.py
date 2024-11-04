# Argumentos variables para diccionario **kvargs = un asterisco para cada variable kwargs: keyWord argumentos
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

listarTerminos() # No recibe nada. No muestra nada
listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Key")