# En Python el constructor está oculto. Para agregar caracteristicas o atributos a una clase, usamos _init_

class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad): # Parametro por default (self). Lleva double underscore __ init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self): # Self solo se encuentra dentro de los metodos
        print(f"Persona: {self.nombre}, {self.apellido}, tiene {self.edad} años.")

persona1 = Persona("Mercedes", "Atim", 36)
print(f"El Objeto 1 de la clase Persona es: {persona1.nombre}, {persona1.apellido} y tiene {persona1.edad} años.")

persona2 = Persona("Ana", "Rios Garin", 19)
print(f"El Objeto 2 de la clase Persona es: {persona2.nombre}, {persona2.apellido}, tiene {persona2.edad} años")

persona1.nombre = "Wanda"
persona1.apellido = "Lanatta"
persona1.edad = 20
print(f"El Objeto 1 Modificado, de la clase Persona ahora es: {persona1.nombre}, {persona1.apellido} y tiene {persona1.edad} años.")

# Los atributos son caracteristicas
# Los metodos son el comportamiento que van a tener los objetos. Es igual que una funcion, pero al metodo se lo asocia con una clase. La funcion no.
print("\nINVOCAMOS EL METODO MOSTRARDETALLE():")
persona1.mostrarDetalle() # La referencia se pasa de manera automática.
persona2.mostrarDetalle()
Persona.mostrarDetalle(persona1) # Debemos pasarle una referencia para el self o nos mostrará un error.