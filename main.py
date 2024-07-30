from sistema import Sistema

def main():
    sistema = Sistema()

    # Agregar clientes
    sistema.agregar_cliente(1, "Juan Pérez", "Calle Falsa 123")
    sistema.agregar_cliente(2, "Ana Gómez", "Avenida Siempre Viva 456")

    # Agregar productos
    sistema.agregar_producto(101, "Laptop", 1200.00)
    sistema.agregar_producto(102, "Teclado", 50.00)
    sistema.agregar_producto(103, "Ratón", 30.00)

    # Generar una factura
    factura = sistema.generar_factura(1, [101, 102])
    if factura:
        print(factura)
    else:
        print("Error al generar la factura")

if __name__ == "__main__":
    main()
