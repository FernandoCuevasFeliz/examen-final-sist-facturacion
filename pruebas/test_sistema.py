# pruebas/test_sistema.py

import unittest
from sistema import Sistema
from cliente import Cliente
from producto import Producto
from factura import Factura

class TestSistema(unittest.TestCase):
    
    def setUp(self):
        self.sistema = Sistema()
        self.sistema.agregar_cliente(1, "Juan Pérez", "Calle Falsa 123")
        self.sistema.agregar_cliente(2, "Ana Gómez", "Avenida Siempre Viva 456")
        self.sistema.agregar_producto(101, "Laptop", 1200.00)
        self.sistema.agregar_producto(102, "Teclado", 50.00)
        self.sistema.agregar_producto(103, "Ratón", 30.00)

    def test_generar_factura(self):
        factura = self.sistema.generar_factura(1, [101, 102])
        self.assertIsNotNone(factura)
        self.assertEqual(factura.cliente.id, 1)
        self.assertEqual(len(factura.productos), 2)
        self.assertEqual(factura.calcular_total(), 1250.00)
        
    def test_generar_factura_cliente_inexistente(self):
        factura = self.sistema.generar_factura(999, [101, 102])
        self.assertIsNone(factura)

    def test_generar_factura_producto_inexistente(self):
        factura = self.sistema.generar_factura(1, [999])
        self.assertIsNone(factura)

    def test_crear_factura_y_verificar_productos(self):
        factura = self.sistema.generar_factura(1, [101, 102])
        self.assertEqual(len(factura.productos), 2)
        self.assertTrue(any(p.id == 101 for p in factura.productos))
        self.assertTrue(any(p.id == 102 for p in factura.productos))
    
    def test_factura_total_calculado_correctamente(self):
        factura = self.sistema.generar_factura(1, [101, 103])
        self.assertEqual(factura.calcular_total(), 1230.00)

    def test_factura_cliente_correcto(self):
        factura = self.sistema.generar_factura(2, [101])
        self.assertEqual(factura.cliente.nombre, "Ana Gómez")

if __name__ == '__main__':
    unittest.main()
