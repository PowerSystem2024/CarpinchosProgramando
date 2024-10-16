class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f" Vehiculo: [Color: {self._color} Ruedas: {self._ruedas}]"

class Auto(Vehiculo):
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return  f"Auto: [Velocidad: {self.velocidad}] {super().__str__()}"            


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return  f"Bicicleta: [tipo: {self.tipo}] {super().__str__()}" 
    
vehiculo1 = Vehiculo("Negro",8)
auto1 = Auto("Blanco",4,299)
bici1 = Bicicleta("Rojo",2,"Urbana")

print("- - - - - VEHICULO: - - - - - ")
print(vehiculo1.color)
print(vehiculo1.ruedas)

print("- - - - - AUTO: - - - - - ")
print(auto1.color)
print(auto1.ruedas)
print(auto1.velocidad)

print("- - - - - BICI: - - - - - ")
print(bici1.color)
print(bici1.ruedas)
print(bici1.tipo)

