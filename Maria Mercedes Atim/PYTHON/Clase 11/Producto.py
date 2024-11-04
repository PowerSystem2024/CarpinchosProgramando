class Producto:
    contadorProductos = 0  # Contador estático para llevar el número de productos

    def __init__(self, nombre, precio):
        Producto.contadorProductos += 1  # Incrementa el contador de productos
        self._idProducto = Producto.contadorProductos  # Asigna un ID único al producto
        self._nombre = nombre  # Asigna el nombre del producto
        self._precio = precio  # Asigna el precio del producto

    @property
    def nombre(self):
        return self._nombre  # Getter para el nombre del producto

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre  # Setter para modificar el nombre del producto

    @property
    def precio(self):
        return self._precio  # Getter para el precio del producto

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:  # Si el nuevo precio es negativo
            nuevo_precio = 0  # Establece el precio a cero en lugar de lanzar una excepción
        self._precio = nuevo_precio  # Setter para modificar el precio del producto

    def __str__(self):
        return f"Producto ID: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio:.2f}"  # Representación en cadena del producto

if __name__ == "__main__":  # Solo sera visible si la prueba se ejecuta desde aqui
    producto1 = Producto("Camiseta", 100)  # Creamos un producto de tipo camiseta
    producto2 = Producto("Pantalon", 150)  # Creamos un producto de tipo pantalón
    print(producto1)
    print(producto2)

    producto1.precio = -50  # Establecemos un precio negativo
    print(producto1)  # Imprime el estado del producto, el precio será 0