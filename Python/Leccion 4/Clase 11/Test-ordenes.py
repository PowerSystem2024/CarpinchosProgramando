from Orden import Orden
from Producto import Producto



producto1 = Producto("Camiseta",100.00)
producto2 = Producto("Pantalon",150.00)
producto3 = Producto("Zapatiilas" 200.00)
producto4 = Producto("Campera",200.00)
producto5 = Producto("Buzo",80.00)
producto6 = Producto("Blusa",75.00)

productos1 = [producto1,producto2] # LISTA
orden1 = Orden(productos1)
orden1.agregar_producto(producto5)
print(orden1)
print(f"Total de la orden: {orden1.calcular_total()}")
productos2 = [producto3,producto4]
orden2 = Orden(productos2)
print(orden2)