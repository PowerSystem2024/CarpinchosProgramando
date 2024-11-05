class Orden:
    contadorOrdenes = 0  # Variable de clase que lleva el conteo de las órdenes creadas

    def __init__(self, computadoras):
        # Inicializa una nueva instancia de la clase Orden
        Orden.contadorOrdenes += 1  # Incrementa el contador de órdenes
        self._idOrden = Orden.contadorOrdenes  # Asigna un ID único para cada orden (incremental)
        self._computadoras = computadoras  # Asigna la lista de computadoras a la orden

    def agregarComputadoras(self, computadoras):
        # Método para agregar una computadora a la lista de computadoras de la orden
        self._computadoras.append(computadoras)  # Añade una computadora a la lista de computadoras

    def __str__(self):
        # Método para generar la representación en cadena (string) de la orden
        computadorasStr = ""  # Inicializa una cadena vacía para almacenar las computadoras
        for computadora in self._computadoras:  # Recorre la lista de computadoras
            computadorasStr += computadora.__str__()  # Agrega el string de cada computadora a computadorasStr
        # Devuelve un string con el formato de la orden y las computadoras
        return f'''
            Orden: {self._idOrden}  # Muestra el ID de la orden
            Computadoras: {computadorasStr}  # Muestra todas las computadoras en la orden
        '''
