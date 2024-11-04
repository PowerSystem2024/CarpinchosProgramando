from Persona import Persona  # Importa la clase Persona desde el módulo Persona

# Imprime un encabezado centrado para la creación de objetos
print("Creacion de objetos".center(50, "-"))

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    persona5 = Persona("Lionel", "Messi", 36)  # Crea un objeto Persona
    persona5.mostrar_detalles()  # Muestra los detalles del objeto persona5

    print("El codigo anterior es de la clase: ", __name__,"\n")  # Muestra el nombre del módulo

# Imprime un encabezado centrado para la eliminación de objetos
print("Eliminacion de objetos".center(50, "-"))

# Llamamos al metodo eliminar objeto
del persona5