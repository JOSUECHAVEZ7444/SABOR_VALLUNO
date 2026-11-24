# Registro Personal de Uso de IA

**Estudiante:** Guimel Josue Mamani Chavez  
**Variante:** A  
**Semanas:** 2, 3 y 4  

### Registro N.º 1 — 10/11/2026
- **Herramienta:** Gemini | **Tipo de uso:** Generación de código | **¿Lo explico sin ayuda?:** Sí
- **Archivo o clase:** `modelo/productos.py`, `modelo/pedidos.py`, `modelo/pagos.py`
- **Consulta textual:** "Cómo estructurar las clases abstractas Producto, Pedido y MetodoPago usando ABC y @property según mi diagrama v2"
- **Qué acepté:** La estructura base con `ABC`, `@abstractmethod` y `@property` para encapsular atributos privados.
- **Qué modifiqué y por qué:** Ajusté las validaciones específicas de la Variante A (descuento 10 %, Bs 2 por plato, Cercado >= 150, chicharrón solo domingo) y simplifiqué los métodos para mantener el código claro.

### Registro N.º 2 — 14/11/2026
- **Herramienta:** Gemini | **Tipo de uso:** Error | **¿Lo explico sin ayuda?:** Sí
- **Archivo o clase:** `modelo/pedidos.py` (`PedidoParaLlevar`)
- **Consulta textual:** "Por qué me aparece TypeError: PedidoParaLlevar.__init__() missing 1 required positional argument: 'cliente' al correr pruebas.py"
- **Qué acepté:** La explicación del orden de parámetros en el constructor `__init__` y la llamada a `super().__init__(cliente)`.
- **Qué modifiqué y por qué:** Corregí la firma de `PedidoParaLlevar.__init__(self, cliente, costo_envase=2.0)` para recibir `cliente` primero.

### Registro N.º 3 — 17/11/2026
- **Herramienta:** Gemini | **Tipo de uso:** Error | **¿Lo explico sin ayuda?:** Sí
- **Archivo o clase:** `modelo/pedidos.py`
- **Consulta textual:** "Por qué sale ModuleNotFoundError: No module named 'modelo' al ejecutar directamente pedidos.py"
- **Qué acepté:** Que al ejecutar un módulo interno directamente Python toma `modelo/` como raíz en lugar de la carpeta del proyecto.
- **Qué modifiqué y por qué:** Ejecuté el proyecto únicamente desde `main.py` y `pruebas.py` en la raíz.

### Registro N.º 4 — 20/11/2026
- **Herramienta:** Gemini | **Tipo de uso:** Revisión | **¿Lo explico sin ayuda?:** Sí
- **Archivo o clase:** `main.py`, `restaurante.py`, `modelo/pedidos.py`, `pruebas.py`
- **Consulta textual:** "Revisar si el código cumple con polimorfismo sin isinstance y las reglas de negocio base y Variante A"
- **Qué acepté:** Eliminar `isinstance` reemplazándolo por métodos polimórficos (`permite_delivery()`, `mesa_ocupada()`, `tipo_nombre()`) y añadir la Regla 9 de retraso > 60 min.
- **Qué modifiqué y por qué:** Adapté el menú de consola en `main.py` con listas numeradas desde 1 y validación de rangos para evitar errores de índice.

### Registro N.º 5 — 23/11/2026
- **Herramienta:** Gemini | **Tipo de uso:** Revisión | **¿Lo explico sin ayuda?:** Sí
- **Archivo o clase:** `docs/diagrama_v2.png`, `README.md`
- **Consulta textual:** "Verificar que el código coincida exactamente con mi diagrama de clases UML v2"
- **Qué acepté:** Sincronizar todos los métodos polimórficos auxiliares (`calcular_compensacion()`, `permite_delivery()`, `menu_dia()`) en el diagrama v2 y documentar la evolución desde el boceto v1.
- **Qué modifiqué y por qué:** Añadí la nota comparativa entre el diagrama v1 hecho a mano y el diagrama v2 digital tanto en `diagrama_v2.png` como en `README.md`.

---

**Declaración:** Declaro que este registro incluye todos mis usos de IA en el proyecto y que puedo explicar el código que entrego.