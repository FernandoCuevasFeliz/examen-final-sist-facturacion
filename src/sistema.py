from cliente import Cliente
from producto import Producto
from factura import Factura

class Sistema:
    def __init__(self):
        self.clientes = {}
        self.productos = {}
        self.facturas = []

    def agregar_cliente(self, id, nombre, direccion):
        cliente = Cliente(id, nombre, direccion)
        self.clientes[id] = cliente

    def agregar_producto(self, id, nombre, precio):
        producto = Producto(id, nombre, precio)
        self.productos[id] = producto

    def generar_factura(self, cliente_id, producto_ids):
        cliente = self.clientes.get(cliente_id)
        productos = [self.productos.get(pid) for pid in producto_ids if self.productos.get(pid)]
        if cliente and productos:
            factura = Factura(len(self.facturas) + 1, cliente, productos)
            self.facturas.append(factura)
            return factura
        else:
            return None
