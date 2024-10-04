class Persona: #Creamos una clase
   # pass # NO se procesa nada mas
  #  def __init__(self): # CONSTRUCTOR VACIO
    def __init__(self,nombre,apellido,edad): # CONSTRUCTOR con argumentos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad  
    # Los atributos son caracteristicas del objeto
    # Los meotdos son acciones del objeto
    
    # CREAMOS METODOS:
    def mostrar_detalle(self):
        print(f"Persona: {self} Nombre: {self.nombre} Apelllido: {self.apellido} EDAD: {self.edad}")

persona1 = Persona("Wanda","Lanatta",24)
persona2 = Persona("Wanda2","Lanatta2",242)

print(type(persona1))
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print("------------")
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print("---MODIFICO PEROSNA 1---------")
persona1.nombre = "MODIFICADO"
print(persona1.nombre)
persona1.mostrar_detalle()