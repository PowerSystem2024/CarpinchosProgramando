class Color:
    def __init__(self, color):
        # Inicializa el color de la figura
        self._color = color  # Atributo privado para el color

    @property
    def color(self):
        # Getter para el color
        return self._color

    @color.setter
    def color(self, value):
        # Setter para el color
        self._color = value

    def __str__(self):
        # Devuelve una representación en forma de cadena del color
        return f'Color: {self._color}'