# Argumentos, variables en funciones
def listarNombres(*nombres): # Se utiliza *args
    for nombre in nombres: # El parametro se convierte en tupla
        print(nombre)
listarNombres("Pauli", "Mariana", "Cirano", "Nelson", "Wanda")
listarNombres("Nicolas", "Melina", "Mercedes", "Enzo", "Florencia", "Adriel")