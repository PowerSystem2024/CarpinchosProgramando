from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0  # Atributo de clase para llevar el conteo de los teclados creados

    def __init__(self, marca, tipoEntrada):
        # Constructor de la clase Teclado, recibe 'marca' y 'tipoEntrada' como parámetros
        Teclado.contadorTeclados += 1  # Incrementa el contador de teclados cada vez que se crea un nuevo objeto
        self._idTeclado = Teclado.contadorTeclados  # Asigna un ID único al teclado basado en el contador
        self._marca = marca  # Asigna la marca del teclado
        self._tipoEntrada = tipoEntrada  # Asigna el tipo de entrada del teclado (ej. USB, inalámbrico)

        # Llama al constructor de la clase base 'DispositivoEntrada' para inicializar los atributos comunes
        super().__init__(marca, tipoEntrada)  # Llama a 'super()' para inicializar los atributos heredados de DispositivoEntrada


    def __str__(self):
        return f"Id Teclado: {self._idTeclado}, Marca: {self._marca}, Tipo entrada: {self._tipoEntrada}"

    # Getters y Setters
    @property
    def idTeclado(self):
        return self._idTeclado

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada


# Realizamos pruebas
if __name__ == "__main__":
    teclado1 = Teclado("Logitech", "USB")
    print(teclado1)
    teclado2 = Teclado("Corsair", "Bluetooth")
    print(teclado2)

    # Usamos los setters para modificar las caracteristicas del teclado
    teclado1.marca = "Microsoft"
    teclado1.tipoEntrada = "Inalámbrico"
    print(teclado1)  # Imprime los cambios de teclado1
