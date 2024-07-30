# Sistema de Facturación | Fernando José Cuevas Feliz - 100473839

## Descripción

El Sistema de Facturación es una aplicación que permite gestionar la facturación de productos y servicios. Este sistema está diseñado para facilitar la creación y administración de facturas, clientes y productos. La aplicación permite realizar las siguientes tareas:

- **Gestión de Clientes**: Agregar y mantener información sobre clientes, como nombre y dirección.
- **Gestión de Productos**: Agregar y mantener información sobre productos, incluyendo su ID, nombre y precio.
- **Generación de Facturas**: Crear facturas que incluyan productos seleccionados y calcular el total a pagar.
- **Modularidad**: Utiliza principios de Ingeniería de Software Basada en Componentes (CBSE) para garantizar una estructura modular y reutilizable del código.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos y directorios:

- **`cliente.py`**: Define la clase `Cliente` para gestionar la información de los clientes.
- **`producto.py`**: Define la clase `Producto` para gestionar la información de los productos.
- **`factura.py`**: Define la clase `Factura` para crear y gestionar facturas.
- **`sistema.py`**: Define la clase `Sistema` que integra las funcionalidades de clientes, productos y facturas.
- **`main.py`**: Archivo principal para ejecutar el sistema.
- **`pruebas/`**: Directorio que contiene las pruebas unitarias y de integración para asegurar la calidad del software.

## Pruebas

El proyecto incluye pruebas unitarias y de integración para asegurar que cada componente funcione correctamente y que el sistema completo integre adecuadamente todas sus partes. Las pruebas están ubicadas en el directorio `pruebas/` y se ejecutan con `unittest`.

## Métricas del Software

Se utilizan herramientas y métricas para evaluar:

- **Reutilización de Código**: Medida con herramientas como SonarQube.
- **Complejidad de los Componentes**: Medida con Radon, que evalúa la complejidad ciclomática del código.
- **Mantenibilidad**: Evaluada mediante el Índice de Mantenibilidad proporcionado por SonarQube.
- **Rendimiento**: Analizado usando `cProfile` para identificar cuellos de botella en el rendimiento.

## Cómo Ejecutar las Pruebas

Para ejecutar todas las pruebas unitarias y de integración, navega al directorio `facturacion` y ejecuta:

```sh
python -m unittest discover -s pruebas
```
