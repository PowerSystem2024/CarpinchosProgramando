class Persona:  #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  #se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  #self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Ariel', 'Betancud',32456879, 40)  #necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#Tarea
print(f'El objeto1 de la clase Persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 54879632,45)
print(f'El objeto2 de la clase Persona es: {persona2.nombre} {persona2.apellido} y su edad es:  {persona2.edad}')

#Tarea
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

#Los objetos no comparten los valores, solo comparten los atributos. Y asi asignamos diferentes valores a cada atributo.

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(
    f'El objeto1 MODIFICADO de la clase Persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

#Los atributos son las características
#Los métodos son el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() #La referencia en este caso se pasa de manera automática
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) #debemos pasarle una referencia (ej: persona1)para el self o dará error
persona1.telefono = '154329189'
print(f'Este es el teléfono de: {persona1.nombre}, {persona1.telefono}') #Hemos creado un atributo de un objeto
# print(persona2.telefono) #el objeto persona2 no tiene este atributo (telefono), da error

persona3 = Persona('Mariana', 'Aguilera', 37268602,31, 'Teléfono', '2604333388', 'Calle Int.', 160, 'manzana', 1, 'Casa', 2, Altura=1.68, Peso=72, CFavorito='azul', Auto='Mercedez', modelo=2023)
persona3.mostrar_detalle()
#print(persona3._dni) #al estar encapsulado, python no lo sugiere pero podemos usarlo igual(aunque no deberíamos utilizarlo)

#persona3.__nombre #está totalmente encapsulado, no podemos mostrarlo, y tampoco podrá modificarse su valor












