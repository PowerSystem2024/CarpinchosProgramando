class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'

if __name__ == '__main__':
    monitor1 = Monitor('HP', '15 pulgadas')
    print(monitor1)
    monitor2 = Monitor('DELL', '17 pulgadas')
    print(monitor2)