# Sistema de Pedidos - Restaurante Sabor Valluno

Proyecto integrador de la asignatura de Programación Orientada a Objetos desarrollado en Python 3 utilizando únicamente la biblioteca estándar. El sistema gestiona el menú del restaurante, clientes, pedidos (en local, para llevar y delivery) y métodos de pago, aplicando encapsulación, herencia, polimorfismo y abstracción.

## Variante Asignada: Variante A

- **Descuento en combos:** 10 % de descuento sobre la suma de sus productos.
- **Envase para llevar:** Bs 2.00 por cada plato (incluidos los platos contenidos dentro de combos o combos anidados).
- **Envío gratis:** Pedidos con subtotal igual o superior a Bs 150.00 únicamente en la zona de Cercado.
- **Pedido mínimo en delivery:** Bs 40.00.
- **Regla adicional:** El plato de chicharrón está disponible únicamente los días domingo (la semana está configurada de domingo a sábado).
- **Regla 9 (Retraso en delivery):** Si un pedido delivery supera los 60 minutos desde su registro, se considera retrasado y se devuelve el costo de envío como compensación.

## Estructura del Repositorio

- `modelo/clientes.py`: Clase `Cliente` con encapsulación y validación de teléfono (8 dígitos, inicia en 6 o 7).
- `modelo/productos.py`: Clase abstracta `Producto` y subclases `Plato`, `Bebida` y `Combo` (soporta composición recursiva).
- `modelo/pedidos.py`: Clase abstracta `Pedido`, `ItemPedido`, enumeración `EstadoPedido` y subclases `PedidoLocal`, `PedidoParaLlevar` y `PedidoDelivery`.
- `modelo/pagos.py`: Clase abstracta `MetodoPago` y subclases `PagoEfectivo`, `PagoQR` y `PagoTarjeta`.
- `restaurante.py`: Clase gestora `Restaurante` que administra catálogo, clientes, mesas ocupadas y reportes de ventas.
- `main.py`: Interfaz de menú interactivo por consola.
- `pruebas.py`: Batería de 8 casos de prueba automatizados con `assert`.
- `docs/`: Contiene los diagramas de clases (`diagrama_v1.png`, `diagrama_v2.png`), `acta_consultas.md`, `bitacora_ia.md` y `registro_ia_<tu_apellido>.md`.

## Instrucciones de Ejecución

Abrir una terminal en la carpeta raíz del proyecto (`SABOR_VALLUNO`) y ejecutar:

- **Iniciar el sistema de consola:**

      python main.py

- **Ejecutar las pruebas unitarias:**

      python pruebas.py

## Cambios del Diagrama v2 respecto al v1

1. **Arquitectura y control de estados:** Se incorporó la clase gestora `Restaurante` y el enumerado `EstadoPedido` para administrar colecciones, mesas ocupadas y el ciclo de vida del pedido.
2. **Refinamiento de atributos y jerarquía:** Se renombró `ParaLlevar` a `PedidoParaLlevar`; en `Bebida` se unificaron `Jarra` y `Vaso` en el booleano `es_jarra` y se añadió `contar_platos()`; en `Combo` se reemplazó `num_platas` por el cálculo recursivo sobre `partes: list[Producto]` con `descuento = 0.10`.
3. **Regla 9 y polimorfismo sin verificación de tipo:** Se añadió `calcular_compensacion()` en `PedidoDelivery` (devolución de envío si retraso > 60 min) y métodos polimórficos auxiliares (`permite_delivery()`, `mesa_ocupada()`, `tipo_nombre()`, `total()`, `cobrar()` y `menu_dia()`) para evitar el uso de `isinstance`.