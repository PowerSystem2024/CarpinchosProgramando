from Producto import Producto

class Orden:

    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes +=1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0 # Variable temporal, despues muere    
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, \nProducto: {productos_str}'
    
if __name__ == '__main__':
    producto1 = Producto("Remera",100.00)
    producto2 = Producto("Pantalon",150.00)

    productos1 = [producto1,producto2] # LISTA
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)

# Tarea: (1) Modificar la orden2, ingresando nuevos productos con sus nombres y precios
#        (2) Crear una nueva lista de productos y agregarla a la orden2

    print("- - - - - TAREA - - - - - -")
#   (1)
    producto3 = Producto("Jeans",250.00)
    producto4 = Producto("Buzo",200.00)
    orden2.agregar_producto(producto3)
    orden2.agregar_producto(producto4)

#   (2)
    pruductos2 = [producto3,producto4]
    for product in pruductos2:
        orden2.agregar_producto(product)

    print(orden2)