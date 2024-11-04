class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo nombre encapsulado
        self._edad = edad      # Atributo edad encapsulado

    @property
    def nombre(self): # Metodo get de nombre
        return self._nombre

    @nombre.setter # Metodo set de nombre
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self): # Metodo get de edad
        return self._edad

    @edad.setter # Metodo set de edad
    def edad(self, valor):
        self._edad = valor

    def __str__(self):
        return f"Persona: [Nombre: {self._nombre} Edad: {self._edad}]"

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # metodo init clase Persona
        self._sueldo = sueldo  # Atributo encapsulado

    @property # Metodo get de sueldo
    def sueldo(self):
        return self._sueldo

    @sueldo.setter # Metodo set de sueldo
    def sueldo(self, valor):
        self._sueldo = valor

    def __str__(self):
        return f"Empleado: [Sueldo: {self._sueldo} ] {super().__str__()}"

empleado1 = Empleado("Melina", 22, 750000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#TAREA: Encapsular los atributos y agregar metodos getter y setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# mostrar los datos, luego modificar y mostrar nuevamente

# Creamos objeto
empleado2 = Empleado("Nelson", 39, 1500000)
print("\nDatos del Empleado 2:")
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

# Modificamos los datos del nuevo objeto
empleado2.nombre = "Ana Paula"
empleado2.edad = 22
empleado2.sueldo = 1200000

# Mostramos los datos modificados
print("\nDatos modificados de Empleado 2:")
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)