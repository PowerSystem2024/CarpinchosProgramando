from abc import ABC, abstractmethod
# ABC significa Abstract Base Class, convierte una clase en abstracta
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        # Inicializa el ancho y alto de la figura
        if self._validar_valores(ancho): # Esta línea verifica si el valor de ancho está en el rango válido (mayor que 0 y menor que 10).
            self._ancho = ancho  # Si el ancho es válido, se asigna a _ancho, que es un atributo privado.
        else:
            self._ancho = 0 # Si el ancho no es válido, se establece en 0
            print(f"Valor erroneo para el ancho {ancho}")
        if self._validar_valores(alto): # verifica si alto está en el rango válido.
            self._alto = alto    # Si el alto es válido, se asigna a _alto.
        else:
            self._alto = 0 # Si el alto no es válido, se establece en 0
            print(f"Valor erroneo para el alto {alto}")

    @property
    def ancho(self):
        # Getter para el ancho
        return self._ancho

    @ancho.setter
    def ancho(self, ancho): # Setter para el ancho
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo para el alto {ancho}")

    @property
    def alto(self):
        # Getter para el alto
        return self._alto

    @alto.setter
    def alto(self, alto): # Setter para el alto
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f"Valor erroneo para el alto {alto}")

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        # Devuelve una representación en forma de cadena de la figura
        return f'\nFiguraGeometrica de {self.ancho} de ancho x {self.alto} de alto.'
    
    # Este es un método que recibe un parámetro, valor, y se utiliza generalmente para validar entradas. El prefijo _ indica que es un método privado.
    def _validar_valores(self, valor):
        return True if 0 < valor < 10 else False # Esta expresión comprueba si valor es mayor que 0 y menor que 10.
