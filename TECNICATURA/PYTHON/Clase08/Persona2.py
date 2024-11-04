class Persona2:

    def __init__(self,nombre,apellido,edad): # se lo llama metodo INIT DUNDER
        self._nombre = nombre # si uso .__ si q no puede ser modificado
        self._apellido = apellido
        self._edad = edad

    def mostrarDetalle(self):
        print(f"La clase Persona: {self._nombre} {self._apellido} {self._edad}")
        
    # GETTERS and SETTERS
    @property # decorador
    def nombre(self): # Metodo Getter
        print("Usando getter")
        return self._nombre
    @nombre.setter # Metodo Setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self): # Metodo Getter
        print("Usando getter")
        return self._apellido
    @apellido.setter # Metodo Setter
    def apellido(self,apellido):
        self._apellido = apellido
    
    @property
    def edad(self): # Metodo Getter
        print("Usando getter")
        return self._edad
    @edad.setter # Metodo Setter
    def edad(self,edad):
        self._edad = edad

    # DESTRUCTOR DE OBJETOS
    def __del__(self):
        print(f"Persona2: {self.mostrarDetalle} se borro")
    
    
if __name__ == "__main__":
    p1 = Persona2("ale","martinez",24)

    # TAREA - Crear 3 objetos mas, modificar con setters y mostrar detalles
    p2 = Persona2("PRUEBA2","Lanatta",4)
    p3 = Persona2("PRUEBA3","Lanatta",2)
    p4 = Persona2("PRUEBA4","Lanatta",224)

    print(p2.nombre)
    p2.nombre = "CAMBIONOMBRE2"
    p2.mostrarDetalle()

    print(p3.apellido)
    p3.apellido = "CAMBIOAPELLIDO3"
    p3.mostrarDetalle()

    print(p4.edad)
    p4.edad = 0
    p4.mostrarDetalle()

    print(__name__)