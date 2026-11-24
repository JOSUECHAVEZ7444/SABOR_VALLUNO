# Registro Personal de Uso de IA

**Estudiante:** Josué Chávez  
**Variante:** A  
**Fecha de desarrollo asistido:** 23/11/2026  

| N.º | Fecha | Herramienta | Tipo | Consulta textual | Qué acepté | Qué modifiqué y por qué | Archivo / Clase | ¿Explicable? |
|---|---|---|---|---|---|---|---|---|
| 1 | 23/11/2026 | Gemini | Código | "Cómo implementar herencia con clases abstractas ABC para Producto, Pedido y MetodoPago según mi diagrama v2" | Crear tres superclases abstractas (`Producto`, `Pedido`, `MetodoPago`) heredando de `ABC` con `@abstractmethod` y reutilizar atributos mediante `super().__init__()`. | Ajusté los atributos privados (`_nombre`, `_precio`, `_cliente`) con `@property` y las validaciones propias de la Variante A (10 % descuento en combo, chicharrón solo domingo). | `productos.py`, `pedidos.py`, `pagos.py` | Sí |
| 2 | 23/11/2026 | Gemini | Código | "Cómo aplicar polimorfismo real sin usar isinstance para calcular precios, envases de platos, cargos de envío y métodos de pago" | Definir métodos polimórficos comunes: `calcular_precio()`, `esta_disponible()` y `contar_platos()` en `Producto`; `calcular_cargos()` en `Pedido`; y `permite_delivery()` en `MetodoPago`. | Implementé `contar_platos()` de forma recursiva en `Combo` (`Plato` retorna 1, `Bebida` retorna 0) para que `PedidoParaLlevar` cobre Bs 2 por plato real sin verificar tipos con `isinstance`. | `productos.py`, `pedidos.py`, `pagos.py` | Sí |
| 3 | 23/11/2026 | Gemini | Error | "Por qué me aparece TypeError: PedidoParaLlevar.__init__() missing 1 required positional argument: 'cliente' al correr pruebas.py" | La explicación del orden de parámetros en el constructor y la llamada a `super().__init__(cliente)`. | Corregí la firma de `PedidoParaLlevar.__init__(self, cliente, costo_envase=2.0)` para recibir `cliente` como primer argumento. | `pedidos.py` (`PedidoParaLlevar`) | Sí |
| 4 | 23/11/2026 | Gemini | Error | "Por qué sale ModuleNotFoundError: No module named 'modelo' al ejecutar directamente pedidos.py" | Que al ejecutar un archivo interno dentro de `modelo/` Python toma esa subcarpeta como raíz en lugar del directorio principal. | Ejecuté el sistema únicamente desde `main.py` y `pruebas.py` en la raíz del proyecto. | `modelo/pedidos.py` | Sí |
| 5 | 23/11/2026 | Gemini | Revisión | "Verificar cumplimiento de reglas de negocio (Regla 9 retraso delivery, mesas ocupadas y semana domingo a sábado) y sincronizar diagrama UML v2" | Incorporar `tiene_retraso()` y `calcular_compensacion()` en `PedidoDelivery`, métodos polimórficos `mesa_ocupada()` y `tipo_nombre()`, y documentar los cambios entre v1 y v2. | Configuré la semana de domingo a sábado en `main.py` y `Plato`, agregué el registro comparativo v1 vs v2 en `README.md` y validé todo con 8 pruebas en `pruebas.py`. | `pedidos.py`, `restaurante.py`, `main.py`, `README.md` | Sí |

---

## Explicación Técnica: Herencia y Polimorfismo en el Sistema

### 1. ¿Cómo funciona la Herencia?
La herencia permite definir una estructura base común en una clase padre abstracta (`ABC`) y especializar su comportamiento en clases hijas sin duplicar código:
* **Jerarquía `Producto` (`modelo/productos.py`):** `Plato`, `Bebida` y `Combo` heredan de `Producto`. Todas heredan la encapsulación de `_nombre` y `_precio` mediante `super().__init__(nombre, precio)` y están obligadas a implementar sus métodos abstractos.
* **Jerarquía `Pedido` (`modelo/pedidos.py`):** `PedidoLocal`, `PedidoParaLlevar` y `PedidoDelivery` heredan de `Pedido`. Comparten la gestión de items (`agregar_item`, `quitar_item`), estados (`EstadoPedido`), `calcular_subtotal()` y `total()`, delegando únicamente el cálculo de cargos extra a cada subclase.
* **Jerarquía `MetodoPago` (`modelo/pagos.py`):** `PagoEfectivo`, `PagoQR` y `PagoTarjeta` heredan de `MetodoPago`, compartiendo la interfaz de cobro y diferenciando sus validaciones y comisiones.

### 2. ¿Cómo funciona el Polimorfismo?
El polimorfismo permite invocar el **mismo método** sobre objetos de distintas clases y que cada objeto responda según su propia lógica interna, eliminando por completo el uso de `isinstance`:
* **Polimorfismo y recursividad en `Combo` (`productos.py`):** Al llamar a `item.calcular_precio()`, `item.esta_disponible(dia)` o `item.contar_platos()`, un `Plato` devuelve su precio base y `1` plato; una `Bebida` duplica su precio si es jarra y devuelve `0` platos; y un `Combo` recorre su lista `self._partes` invocando esos mismos métodos sobre cada componente (incluso si contiene otro `Combo` anidado) y aplica el 10 % de descuento.
* **Cálculo polimórfico de cargos (`pedidos.py`):** `Pedido.total()` llama a `self.calcular_cargos()`. En `PedidoLocal` retorna `0.0`; en `PedidoParaLlevar` suma `contar_platos()` de cada item y multiplica por Bs 2.00; y en `PedidoDelivery` evalúa el mínimo de Bs 40.00, el envío gratis en Cercado ($\ge$ Bs 150.00) o la tarifa por zona.
* **Validación polimórfica de pago (`pagos.py`):** `PedidoDelivery.cobrar(metodo_pago)` llama a `metodo_pago.permite_delivery()`. `PagoEfectivo` retorna `False` (lanzando error), mientras `PagoQR` y `PagoTarjeta` retornan `True`.

**Declaración:** Declaro que este registro incluye todos mis usos de IA en el proyecto y que puedo explicar el código que entrego.
