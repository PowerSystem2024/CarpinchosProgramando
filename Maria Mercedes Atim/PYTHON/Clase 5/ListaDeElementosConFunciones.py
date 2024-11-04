# Si sabemos que por parametro recibimos una lista, dentro de la funcion la tratamos como tal.
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

listaDeNombres = ["Wan", "Marian", "Pauli", "Meli"]

desplegarNombres(listaDeNombres)
desplegarNombres("Nel") # Va a iterar cada caracter del nombre
# desplegarNombres(10) # Un entero es un objeto no es iterable
desplegarNombres((10, 11)) # Se convierte en tupla
desplegarNombres([22, 55]) # Se convierte en lista