'''
Definir una clase padre llamada vehiculo y dos clases hijas llamadas Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase padre debe tener los siguientes atributos y metodos:
Vehiculo (Clase Padre)
-Atributos(Color, ruedas)
-Metodos(__init__, (self, color, ruedas) y __str__())

Auto (Clase hija de vehiculo)
-Atributos(velocidad (km/h))
-Metodos(__init__(self, color, ruedas, velocidad) y __str__())

Bicicleta (Clase hija de vehiculo)
-Atributos(tipo (urbana/montaña/etc.))
-Metodos(__init__(self, color, ruedas, tipo) y __str__())

Crear un objeto de cada clase
'''
class Vehiculo: # Clase Padre
    def __init__(self, color, ruedas):
        self._color = color  # Atributo encapsulado
        self._ruedas = ruedas  # Atributo encapsulado

    def __str__(self):
        # Devuelve una cadena del vehículo
        return f"Vehículo - Color: {self._color}, Ruedas: {self._ruedas}"

class Auto(Vehiculo): # Clase Hija
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)  # Inicializamos atributos de la clase padre
        self._velocidad = velocidad  # Atributo encapsulado

    def __str__(self):
        # Devuelve una representación en cadena del auto
        return f"Auto - Color: {self._color}, Ruedas: {self._ruedas}, Velocidad: {self._velocidad} km/h"


class Bicicleta(Vehiculo): # Clase Hija
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)  # Inicializamos atributos de la clase padre
        self._tipo = tipo  # Atributo encapsulado

    def __str__(self):
        # Devuelve una cadena de la bicicleta
        return f"Bicicleta - Color: {self._color}, Ruedas: {self._ruedas}, Tipo: {self._tipo}"


# Crear un objeto de cada clase
vehiculo1 = Vehiculo("Verde", 4)
auto1 = Auto("Rojo", 4, 150)  # Objeto de la clase Auto
bicicleta1 = Bicicleta("Azul", 2, "Urbana")  # Objeto de la clase Bicicleta

# Mostrar los datos de cada objeto
print(vehiculo1)
print(auto1)  # Imprime los datos del auto
print(bicicleta1)  # Imprime los datos de la bicicleta