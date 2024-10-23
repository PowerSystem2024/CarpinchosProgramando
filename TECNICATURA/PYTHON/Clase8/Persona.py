class Persona:

    def __init__(self,nombre,apellido,dni,edad,*args,**kwargs):
        self.__nombre = nombre  # Con __ delante, el atributo se vuelve privado
        self.apellido = apellido
        self._dni = dni  # Con un solo _ lo encapsulas pero sigue siendo accesible
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self):
        print(f"Detalles de la Persona: {self.__nombre} {self.apellido} {self._dni} {self.edad}, dirección: {self.args}, datos importantes: {self.kwargs}")

# Instancia de la clase Persona con argumentos y kwargs
p1 = Persona("Wanda","Lanatta",42214977,24,"Teléfono", 1128449525,"Calle falsa",5042,"Manzana",77,"Casa",Altura=1.60, Peso=50,Auto="Volkswagen",Color="Negro")
print(p1.mostrarDetalle())
