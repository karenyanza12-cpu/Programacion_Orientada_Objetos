# restaurante_app - Semana 12

## Datos del estudiante

**Nombre:** Karen Anahi Yanza Maza  
**Asignatura:** Programación Orientada a Objetos  
**Actividad:** Semana 12 - Utilización de colecciones para mejorar el rendimiento

## Descripción

En esta semana se continuó trabajando con el proyecto Amalia Restaurant de la Semana 11.

Se mantuvieron los productos, usuarios, ventas, control de stock y los archivos JSON.

La mejora principal fue utilizar diccionarios para hacer más rápidas algunas búsquedas del sistema.

## Mejoras realizadas

Se mantuvieron las listas de productos, usuarios y ventas porque se utilizan para almacenar, listar y guardar la información.

También se agregaron índices utilizando diccionarios:

- Productos: se utiliza el código como clave.
- Usuarios: se utiliza la identificación como clave.
- Ventas: se agrupan por identificación de usuario.

Con estos índices se pueden realizar búsquedas sin recorrer toda la lista cada vez.

Los índices se actualizan cuando se agregan o eliminan datos y se reconstruyen cuando el programa inicia y recupera la información de los archivos JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
