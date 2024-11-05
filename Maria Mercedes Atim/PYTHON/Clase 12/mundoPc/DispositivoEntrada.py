class DispositivoEntrada: # Clase Padre de Raton y Teclado
    def __init__(self, marca, tipoEntrada):
        # Constructor de la clase base 'DispositivoEntrada', que inicializa los atributos comunes
        self._marca = marca  # Atributo que almacena la marca del dispositivo
        self._tipoEntrada = tipoEntrada  # Atributo que almacena el tipo de entrada (ej. USB, inalámbrico)