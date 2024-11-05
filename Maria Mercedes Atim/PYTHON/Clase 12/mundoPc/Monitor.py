class Monitor:
    contadorMonitores = 0  # Atributo de clase que lleva el conteo de los monitores creados

    def __init__(self, marca, tamaño):
        # Constructor de la clase Monitor, recibe 'marca' y 'tamaño' como parámetros
        Monitor.contadorMonitores += 1  # Incrementa el contador de monitores cada vez que se crea un nuevo objeto
        self._idMonitor = Monitor.contadorMonitores  # Asigna un ID único al monitor, basado en el contador
        self._marca = marca  # Asigna la marca del monitor
        self._tamaño = tamaño  # Asigna el tamaño del monitor (ej. "24 pulgadas", "27 pulgadas", etc.)


    def __str__(self):
        return f"Id Monitor: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño}"

    # Getter para idMonitor (sin setter, ya que es único y no se debe modificar después de la creación)
    @property
    def idMonitor(self):
        return self._idMonitor

    # Getter y Setter para marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # Getter y Setter para tamaño
    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

# Realizamos pruebas
if __name__ == "__main__":
    monitor1 = Monitor("Samsung", "24 pulgadas")
    print(monitor1)
    monitor2 = Monitor("LG", "27 pulgadas")
    print(monitor2)

    # Usamos los setters con las propiedades
    monitor1.marca = "Dell"
    monitor1.tamaño = "32 pulgadas"
    print(monitor1)  # Imprime los cambios de monitor1
