class Persona:
    def __init__(self,nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad = edad
    
    def __str__(self): # SIRVE PARA SOBREESCRIBIR
        return f"Persona: [ Nombre: {self.nombre}, Edad: {self.edad} ]"

class Empleado(Persona): # EXTIENDE DE PERSONA
    def __init__(self,nombre,edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [ Sueldo: {self._sueldo} ] {super().__str__()}"
    

empleado1 = Empleado("Ale",24,750000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#TAREA: encapsular atributos y agregar metodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar los datos, modificarlos y mostrarlos nuevamente
print("- - - - -  TAREA - - - - - ")
empleadoTarea = Empleado("EmpleadoTarea",100,9999)
print(empleadoTarea.nombre)
print(empleadoTarea.edad)
print(empleadoTarea.sueldo)
empleadoTarea.nombre = "CambioNombre"
empleadoTarea.sueldo = 11111
print(empleadoTarea.nombre)
print(empleadoTarea.edad)
print(empleadoTarea.sueldo)
