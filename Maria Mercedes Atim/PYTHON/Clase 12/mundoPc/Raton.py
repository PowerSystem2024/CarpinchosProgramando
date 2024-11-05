from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0  # Atributo de clase para llevar el conteo de los ratones creados

    def __init__(self, marca, tipoEntrada):
        # Constructor de la clase Raton, recibe 'marca' y 'tipoEntrada' como parámetros
        Raton.contadorRatones += 1  # Incrementa el contador de ratones por cada nuevo objeto creado
        self._idRaton = Raton.contadorRatones  # Asigna un ID único al ratón, basado en el contador
        self._marca = marca  # Asigna la marca del ratón
        self._tipoEntrada = tipoEntrada  # Asigna el tipo de entrada (ej. USB, inalámbrico, etc.)

        # Llama al constructor de la clase base 'DispositivoEntrada' para inicializar los atributos comunes
        super().__init__(marca, tipoEntrada)  # Llama a 'super()' para inicializar los atributos heredados de DispositivoEntrada

    def __str__(self):
        return f"Id Raton: {self._idRaton}, Marca: {self._marca}, Tipo entrada: {self._tipoEntrada}"

    # Getter para idRaton (sin setter, ya que es único y no se debe modificar después de la creación)
    @property
    def idRaton(self):
        return self._idRaton

    # Getter y Setter para marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # Getter y Setter para tipoEntrada
    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

# Realizamos pruebas
if __name__ == "__main__":
    raton1 = Raton("HP", "USB")
    print(raton1)
    raton2 = Raton("Acer", "Bluetooth")
    print(raton2)

    # Usamos los setters con las propiedades
    raton1.marca = "Logitech"
    raton1.tipoEntrada = "Inalámbrico"
    print(raton1)  # Imprime los cambios de raton1
