from Raton import Raton
from Monitor import Monitor
from Teclado import Teclado

class Computadora:
    contadorComputadoras = 0  # Atributo de clase para llevar un conteo de las computadoras creadas

    def __init__(self, marca, monitor, teclado, raton):
        # Constructor de la clase Computadora, recibe los parámetros: marca, monitor, teclado y raton
        Computadora.contadorComputadoras += 1  # Incrementa el contador de computadoras por cada nuevo objeto creado
        self._idComputadora = Computadora.contadorComputadoras  # Asigna un ID único basado en el contador
        self._marca = marca  # Asigna la marca de la computadora
        self._monitor = monitor  # Asigna el monitor de la computadora
        self._teclado = teclado  # Asigna el teclado de la computadora
        self._raton = raton  # Asigna el ratón de la computadora

    def __str__(self):
        # Método especial __str__ para devolver una representación en cadena (string) de la computadora
        return f'''Computadora:
            Marca: {self._marca}, Id de Computadora: {self._idComputadora}  # Muestra la marca y el ID único
            Monitor: {self._monitor}  # Muestra la información del monitor
            Teclado: {self._teclado}  # Muestra la información del teclado
            Raton: {self._raton}  # Muestra la información del ratón'''

# Si el archivo es ejecutado directamente, el siguiente bloque de código se ejecutará
if __name__ == "__main__":  # Este bloque se usa generalmente para pruebas o para ejecutar un script de ejemplo
    teclado1 = Teclado("Logitech", "USB")
    raton1 = Raton("HP", "USB")
    monitor1 = Monitor("Samsung", "24 pulgadas")
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)
    print(computadora1)
    print("\n-----------------\n")
    teclado2 = Teclado("RedDragon", "inalambrico")
    raton2 = Raton("Corsair", "USB")
    monitor2 = Monitor("RedDragon", "27 pulgadas")
    computadora2 = Computadora("ThermalTake", monitor2, teclado2, raton2)
    print(computadora2)