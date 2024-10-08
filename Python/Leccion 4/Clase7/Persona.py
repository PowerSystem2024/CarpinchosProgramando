class Persona:

    def __init__(self,nombre,apellido,dni,edad,*args,**kwargs): # Se lo llama metodo INIT DUNDER
        self.__nombre = nombre # si uso .__ si q no puede ser modificado
        self.apellido = apellido
        self._dni = dni # con la ._ lo encapsulo, haciendolo PRIVADO, en realidad se puede usar con ._ pero es una SUGERENCIA de no usarlo
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self):
        print(f"La clase Persona: {self.__nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")
        
                                 # - - - - - - - ESTOS SON LOS ARGS - - - - - - - - - -- - - # - - - - - - - - ESTOS SON LOS KWARGS - - - - - - - - #  
p1 = Persona("Ale","Martinez",42214977,24,"Telefono", 1128449525,"Calle falsa",5042,"Manzana",77,"Casa",Altura=1.60, Peso=50,Auto="Volkswagen",Color="Negro")
print(p1.mostrarDetalle())