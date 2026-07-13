# Sistema de Gestión de Restaurante

## Estudiante

Karen Anahi Yanza Maza

## Descripción

Este proyecto fue desarrollado para la tarea de la Semana 7 de la asignatura Programación Orientada a Objetos. El sistema representa la gestión básica de un restaurante, permitiendo registrar, listar y buscar productos y clientes mediante un menú interactivo en consola.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py
```

## Relación entre las clases

La clase **Producto** representa la información de los productos del restaurante y utiliza un constructor para crear los objetos. Además, mediante los decoradores **@property** y **@setter** se controla el acceso a los atributos y se validan los datos ingresados.

La clase **Cliente** fue desarrollada utilizando **@dataclass**, lo que permite crear objetos de una forma más sencilla.

La clase **Restaurante** administra las listas de productos y clientes, además de realizar el registro, la búsqueda y el listado de la información.

## Funcionalidades

El sistema permite:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Salir del programa mediante un menú interactivo.

## Reflexión

Con esta actividad pude comprender mejor cómo crear objetos utilizando constructores y cómo aplicar los decoradores **@property**, **@setter** y **@dataclass** para organizar mejor el código. También entendí la importancia de trabajar con una estructura modular, ya que facilita el mantenimiento y la organización del proyecto cuando este va creciendo.