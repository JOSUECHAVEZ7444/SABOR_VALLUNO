# Acta de Consultas al Cliente (Docente)

**Estudiante:** Guimel Josue Mamani Chavez  
**Docente:** Ing. Roy A. Carrasco Aguilar  
**Variante:** A  

| N.º | Fecha | Pregunta realizada al docente | Respuesta oficial del cliente | Impacto en el sistema |
|---|---|---|---|---|
| 1 | 05/11/2026 | Respecto a la Regla 9 (Retraso en delivery): ¿cuándo se considera que un pedido tiene retraso y cuál es la compensación correspondiente para el cliente? | Se considera retraso si el pedido se entrega más de 60 minutos después de haber sido registrado, y la compensación consiste en la devolución del costo de envío. | Se implementaron los métodos `tiene_retraso()` (verificando > 3600 segundos desde `_fecha_hora`) y `calcular_compensacion()` en la clase `PedidoDelivery`. |
| 2 | 12/11/2026 | En la Variante A, si un combo contiene dos platos y se pide para llevar, ¿el costo de envase (Bs 2 por plato) aplica a cada plato dentro del combo? | Sí, el método polimórfico `contar_platos()` debe sumar los platos individuales incluso si están dentro de combos anidados. | `Combo.contar_platos()` recorre sus partes recursivamente y `PedidoParaLlevar.calcular_cargos()` multiplica el total de platos por Bs 2.00. |
| 3 | 16/11/2026 | Para la disponibilidad del plato de chicharrón (solo domingos), ¿cómo debe ordenarse la semana en el sistema? | La semana debe configurarse empezando en domingo y terminando en sábado (Domingo a Sábado). | Se definió el orden de días de domingo a sábado en las validaciones de `Plato` y en el menú de consola de `main.py`. |
