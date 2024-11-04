from Orden import Orden
from Producto import Producto

producto1 = Producto("Camiseta", 100)  # Creamos nuevos producto
producto2 = Producto("Pantalon", 150)
producto3 = Producto("Medias", 45)
producto4 = Producto("Campera", 250)
producto5 = Producto("Sweater", 95)
producto6 = Producto("Blusa", 75)

productos1 = [producto1, producto2] # Creamos lista de productos
orden1 = Orden(productos1) # Creamos la primera orden con la lista de productos
orden1.agregarProducto(producto5)
orden1.agregarProducto(producto3)
print(orden1) # Mostramos la orden
print(f"El total de la orden1 es: ${orden1.calcularTotal()}") # Mostramos el total de la orden

productos2 = [producto3, producto4] # Agregamos los nuevos productos a la lista nueva
orden2 = Orden(productos2)
orden2.agregarProducto(producto6)
orden2.agregarProducto(producto2)
print(orden2)
print(f"El total de la orden2 es: ${orden2.calcularTotal()}")