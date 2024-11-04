class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __add__(self, other):
        return self._nombre + other.nombre

persona1 = ("Nelson", 42)
persona2 = ("Rios", 5)

# persona1.__add__(persona2) Sintaxis interna y automatica