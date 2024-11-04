from Producto import Producto

class Orden:
    contadorOrdenes = 0  # Contador estático para llevar el número de órdenes

    def __init__(self, productos):
        Orden.contadorOrdenes += 1  # Incrementa el contador de órdenes
        self.idOrden = Orden.contadorOrdenes  # Asigna un ID único a la orden
        self._productos = list(productos)  # Inicializa la lista de productos

    def agregarProducto(self, producto):
        self._productos.append(producto)  # Agrega un producto a la lista de productos

    def calcularTotal(self):
        total = 0  # Variable temporal para almacenar el total
        for producto in self._productos:
            total += producto.precio  # Suma el precio de cada producto al total
        return total  # Retorna el total calculado

    def __str__(self):  # Método para representar la orden como cadena
        productos_str = ""  # Inicializa una cadena para los productos
        for producto in self._productos:
            productos_str += producto.__str__() + " | "  # Agrega la representación de cada producto
        return f"Orden: {self.idOrden}, \nProductos: {productos_str.strip()} "  # Retorna la representación de la orden

if __name__ == "__main__":
    producto1 = Producto("Camiseta", 100)  # Creamos un producto de tipo camiseta
    producto2 = Producto("Pantalon", 150)  # Creamos un producto de tipo pantalón
    productos1 = [producto1, producto2] # Creamos lista de productos
    orden1 = Orden(productos1) # Creamos la primera orden con la lista de productos
    print(orden1)
    producto3 = Producto("Short", 100)  # Creamos nuevos productos
    producto4 = Producto("Camisa", 200)
    producto5 = Producto("Corbata", 100)
    producto6 = Producto("Zapatos", 250)
    productos2 = [producto3, producto4, producto5, producto6] # Agregamos los nuevos productos a la lista nueva
    orden2 = Orden(productos2)
    print("Ahora orden2 tiene los siguientes productos:\n", orden2)
    
# TAREA: Modificar la orden2 ingresando nuevos productos con sus nombres y precios.
# Crear una nueva lista de productos y agregarla a la orden2