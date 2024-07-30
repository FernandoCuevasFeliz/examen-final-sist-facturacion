from datetime import datetime
from producto import Producto

class Factura:
    def __init__(self, id, cliente, productos):
        self.id = id
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = productos
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

    def __str__(self):
        productos_str = "\n".join([str(p) for p in self.productos])
        return (f"Factura ID: {self.id}\nFecha: {self.fecha}\n"
                f"Cliente: {self.cliente}\n"
                f"Productos:\n{productos_str}\n"
                f"Total: {self.total}")
