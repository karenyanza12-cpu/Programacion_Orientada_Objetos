# Sistema de Gestión de Restaurante

## Estudiante

Karen Anahi Yanza Maza

## Descripción

Este proyecto corresponde a la Semana 6 de Programación Orientada a Objetos. El sistema representa un restaurante donde se administran productos utilizando herencia, encapsulación y polimorfismo.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py
```

## Herencia

Se implementó una clase padre llamada **Producto** y dos clases hijas:

- Platillo
- Bebida

Ambas reutilizan los atributos de la clase padre mediante el uso de `super()`.

## Encapsulación

El atributo `__precio` fue protegido mediante encapsulación.

Para acceder y modificar su valor se utilizaron los métodos:

- `obtener_precio()`
- `cambiar_precio()`

El método `cambiar_precio()` valida que el nuevo precio sea mayor que cero.

## Polimorfismo

Las clases `Platillo` y `Bebida` sobrescriben el método `mostrar_informacion()`.

La clase `Restaurante` recorre una lista de productos y ejecuta el mismo método, obteniendo un comportamiento diferente según el tipo de objeto.

## Reflexión

La Programación Orientada a Objetos permite reutilizar código, proteger la información mediante encapsulación y facilitar el mantenimiento de los programas. La herencia y el polimorfismo ayudan a desarrollar sistemas más organizados y escalables.
