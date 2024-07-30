import unittest
from datetime import datetime
from cliente import Cliente
from producto import Producto
from factura import Factura

class TestFactura(unittest.TestCase):
    
    def setUp(self):
        cliente = Cliente(1, "Juan Pérez", "Calle Falsa 123")
        producto1 = Producto(101, "Laptop", 1200.00)
        producto2 = Producto(102, "Teclado", 50.00)
        self.factura = Factura(1, cliente, [producto1, producto2])
    
    def test_calcular_total(self):
        self.assertEqual(self.factura.calcular_total(), 1250.00)
    
    def test_factura_str(self):
        fecha_str = self.factura.fecha.strftime('%Y-%m-%d %H:%M:%S')
        expected_str = (f"Factura ID: 1\nFecha: {fecha_str}\n"
                        f"Cliente: Cliente ID: 1, Nombre: Juan Pérez, Dirección: Calle Falsa 123\n"
                        f"Productos:\nProducto ID: 101, Nombre: Laptop, Precio: 1200.0\n"
                        f"Producto ID: 102, Nombre: Teclado, Precio: 50.0\n"
                        f"Total: 1250.0")
        self.assertEqual(str(self.factura), expected_str)

if __name__ == '__main__':
    unittest.main()
