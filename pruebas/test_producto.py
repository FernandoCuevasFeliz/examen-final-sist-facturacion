import unittest
from producto import Producto

class TestProducto(unittest.TestCase):
    
    def setUp(self):
        self.producto = Producto(101, "Laptop", 1200.00)
    
    def test_actualizar_precio(self):
        self.producto.actualizar_precio(1300.00)
        self.assertEqual(self.producto.precio, 1300.00)

    def test_producto_str(self):
        self.assertEqual(str(self.producto), "Producto ID: 101, Nombre: Laptop, Precio: 1200.0")

if __name__ == '__main__':
    unittest.main()
