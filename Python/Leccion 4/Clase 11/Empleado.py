class Empleado: # No hereda sino sola de la clase object
    def __init__(self, nombre, sueldo): # constructor con nombre y sueldo
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self): # toString con datos del Empleado
        return f"Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]"

    def mostrarDetalles(self):
        return self.__str__()