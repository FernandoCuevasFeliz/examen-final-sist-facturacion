import unittest
from cliente import Cliente

class TestCliente(unittest.TestCase):
    
    def setUp(self):
        self.cliente = Cliente(1, "Juan Pérez", "Calle Falsa 123")
    
    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), "Cliente ID: 1, Nombre: Juan Pérez, Dirección: Calle Falsa 123")

if __name__ == '__main__':
    unittest.main()
