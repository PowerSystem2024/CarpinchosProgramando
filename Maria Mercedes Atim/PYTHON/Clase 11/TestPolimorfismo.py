from Empleado import Empleado  # Importa la clase Empleado
from Gerente import Gerente      # Importa la clase Gerente

def imprimirDetalles(objeto):
    """Imprime los detalles del objeto pasado como parámetro."""
    print(objeto)  # Llama al método __str__ de Empleado o Gerente
    print(type(objeto))  # Muestra el tipo de dato del objeto
    print(objeto.mostrarDetalles())  # Imprime detalles específicos del objeto
    if isinstance(objeto, Gerente):  # Verifica si el objeto es una instancia de Gerente
        print(objeto.departamento)  # Imprime el departamento del gerente

# Crear una instancia de Empleado
empleado = Empleado("Nicolas", 500000)  # Creamos un empleado
imprimirDetalles(empleado)  # Imprimimos los detalles del empleado

print()

# Crear una instancia de Gerente
gerente = Gerente("Wanda", 900000, "Sistemas")  # Crea un gerente llamado Wanda con un salario y departamento
imprimirDetalles(gerente)  # Imprime los detalles del gerente