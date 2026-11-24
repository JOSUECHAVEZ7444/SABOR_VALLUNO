# Acta de Consultas y Definiciones del Proyecto

**Estudiante:** Josué Chávez  
**Docente / Cliente:** Ing. Roy A. Carrasco Aguilar  
**Variante:** A  

> **Nota:** No se realizaron consultas directas adicionales al docente durante el desarrollo. Todas las reglas de negocio y casos borde se definieron a partir del documento de especificaciones de la **Variante A** y consultas técnicas con **Gemini** realizadas el **23/11/2026**.

| N.º | Fecha | Fuente de consulta | Criterio definido para el sistema | Impacto en el código |
|---|---|---|---|---|
| 1 | 23/11/2026 | Enunciado oficial + Gemini | Regla 9 (Retraso en delivery): si el pedido se entrega más de 60 minutos después de su registro, se devuelve el costo de envío como compensación. | Se implementaron `tiene_retraso()` (`> 3600` segundos desde `_fecha_hora`) y `calcular_compensacion()` en `PedidoDelivery`. |
| 2 | 23/11/2026 | Enunciado oficial + Gemini | Variante A (Envase para llevar): el costo de envase (Bs 2.00 por plato) aplica a cada plato individual, incluyendo los que están dentro de combos o combos anidados. | `Combo.contar_platos()` recorre sus partes recursivamente y `PedidoParaLlevar.calcular_cargos()` multiplica el total por Bs 2.00. |
| 3 | 23/11/2026 | Enunciado oficial + Gemini | Disponibilidad semanal: la semana se maneja de domingo a sábado para restringir la venta de chicharrón únicamente a los domingos. | Se configuró el orden de días de domingo a sábado en `Plato` y en el menú de consola de `main.py`. |
