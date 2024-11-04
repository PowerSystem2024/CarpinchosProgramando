# En Python el constructor está oculto. Para agregar caracteristicas o atributos a una clase, usamos _init_

class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Parametro por default (self). Lleva double underscore __ init Dunder
        self.nombre = nombre # Si se encapsula con doble guion bajo, se le esta diciendo al sistema que es un atributo privado y protegido solo es accesible por name mangling(modificacion)
        self.apellido = apellido
        self._dni = dni # Atributo encapsulado como private con 1 solo guion bajo
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self): # Self solo se encuentra dentro de los metodos
        print(f"La clase Persona tiene los siguientes datos: {self.nombre}, {self.apellido}, {self._dni}, tiene {self.edad} años, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")

persona1 = Persona("Mercedes", "Atim", 34445464, 36)
print(f"El Objeto 1 de la clase Persona es: {persona1.nombre}, {persona1.apellido}, {persona1._dni} y tiene {persona1.edad} años.")

persona2 = Persona("Ana", "Rios Garin", 54654321, 19)
print(f"El Objeto 2 de la clase Persona es: {persona2.nombre}, {persona2.apellido}, tiene {persona2.edad} años")

persona1.nombre = "Wanda"
persona1.apellido = "Lanatta"
persona1.edad = 20
print(f"El Objeto 1 Modificado, de la clase Persona ahora es: {persona1.nombre}, {persona1.apellido}, {persona1._dni} y tiene {persona1.edad} años.")

# Los atributos son caracteristicas
# Los metodos son el comportamiento que van a tener los objetos. Es igual que una funcion, pero al metodo se lo asocia con una clase. La funcion no.
print("\nINVOCAMOS EL METODO MOSTRARDETALLE():")
persona1.mostrarDetalle() # La referencia se pasa de manera automática.
persona2.mostrarDetalle()
Persona.mostrarDetalle(persona1) # Debemos pasarle una referencia para el self o nos mostrará un error.


print("\nATRIBUTO SIN METODO INIT:")
# Se puede agregar atributos al objeto sin que esten en el metodo init de inicializacion
# Se pueden crear de manera "superficial o local" ya que no se comparten con otros objetos
persona1.telefono = '1131313131' # Este atributo será solamente de persona1, persona2, el otro objeto, no lo tendrá.
print(f"Nuevo atributo de {persona1.nombre} Teléfono: ",persona1.telefono)

print("\nUSAMOS LOS ATRIBUTOS VARIABLES:")
print("Persona 3: ")
persona3 = Persona("Rogelio","Romero", 35789456, 22 ,"Telefono","2614445557","Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura = 1.83, Peso = 105, ColorFavorito = "Azul", Auto = "Citroen", Modelo = 2021)
persona3.mostrarDetalle()
print("\nPersona 4: ")
persona4 = Persona("Leonel","Arancibia", 355554466, 32 ,"Telefono","1114445557","Calle 140", 1780, "Manzana", "B", "Casa", 10, Altura = 1.95, Peso = 90, ColorFavorito = "Rojo", Auto = "Peugeot 208", Modelo = 2021)
persona4.mostrarDetalle()
# print(persona3._dni) No se debe usar de esta manera ya que el atributo está encapsulado