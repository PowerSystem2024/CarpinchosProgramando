class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre  # Inicializa el nombre
        self._apellido = apellido  # Inicializa el apellido
        self._edad = edad  # Inicializa la edad

    def mostrar_detalles(self):
        # Muestra los detalles de la persona
        print(f"\nLos datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property
    def nombre(self):  # Método getter para el nombre
        print("\nEstamos usando el método get de nombre")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método setter para el nombre
        print("\nEstamos usando el método set de nombre")
        self._nombre = nombre

    @property
    def apellido(self):  # Método getter para el apellido
        print("\nEstamos usando el método get de apellido")
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Método setter para el apellido
        print("\nEstamos usando el método set de apellido: ")
        self._apellido = apellido

    @property
    def edad(self):  # Método getter para la edad
        print("\nEstamos usando el método get de edad: ")
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método setter para la edad (actualmente comentado)
        print("\nEstamos usando el método set de edad: ")
        self._edad = edad
        
    def __del__(self): # Metodo para eliminar un objeto
        print(f"\nPersona: {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    persona1 = Persona("Melina", "Aguilar", 20)  # Crea el primer objeto Persona
    print(persona1.nombre)  # Llamamos al método get para el nombre
    print(persona1.apellido)  # Llamamos al método get para el apellido
    print(persona1.edad)  # Llamamos al método get para la edad

    persona1.apellido = "Lopez"  # Cambia el apellido usando el setter

    # Al no tener método set, edad se convierte en un atributo de solo lectura (read-only)
    # persona1.edad = 21  # Esto generaría un error, ya que no hay setter para edad

    persona1.mostrar_detalles()  # Muestra los detalles actualizados

    print("\nTAREA: Crear 3 objetos más. Utilizando getters y setters para modificar y mostrar los cambios con el método mostrar_detalles()")

    # Crea tres objetos Persona adicionales
    persona2 = Persona("Mariana", "Aguilera", 24)
    persona3 = Persona("Nelson", "Rios", 39)
    persona4 = Persona("Nicolas", "Mercado", 22)

    persona2.apellido = "Garin"  # Cambia el apellido de persona2
    print("Ahora el apellido de persona2 es: ", persona2.apellido)  # Muestra el nuevo apellido
    persona3.nombre = "Omar"  # Cambia el nombre de persona3
    print("Ahora el nombre de persona3 es: ", persona3.nombre)  # Muestra el nuevo nombre
    persona4.apellido = "Aguilar"  # Cambia el apellido de persona4
    print("Ahora el apellido de persona4 es: ", persona4.apellido)  # Muestra el nuevo apellido

    # Muestra los detalles de cada una de las nuevas personas
    persona2.mostrar_detalles()
    persona3.mostrar_detalles()
    persona4.mostrar_detalles()

    print("El código anterior es de la clase: ", __name__)  # Muestra el nombre del módulo
