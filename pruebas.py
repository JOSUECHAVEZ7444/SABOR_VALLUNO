from datetime import datetime, timedelta
from modelo.clientes import Cliente
from modelo.productos import Producto, Plato, Bebida, Combo
from modelo.pedidos import PedidoLocal, PedidoParaLlevar, PedidoDelivery, EstadoPedido
from modelo.pagos import PagoEfectivo, PagoQR, PagoTarjeta

# 1. Abstraccion: no deja instanciar Producto
try:
    Producto("X", 10)
    assert False
except TypeError:
    pass

# 2. Validacion telefono cliente (8 digitos, empieza en 6 o 7)
c = Cliente("Juan", "70712345")
assert c.telefono == "70712345"

# 3. Disponibilidad Chicharron solo domingo y jarra x3
chich = Plato("Chicharron", 60, ["Domingo"])
assert chich.esta_disponible("Domingo") == True
assert chich.esta_disponible("Lunes") == False
jarra = Bebida("Jarra Chicha", 8, True)
assert jarra.calcular_precio() == 24.0

# 4. Caso de prueba de referencia (Silpancho 35 + Mocochinchi 6 = 36.90; 2 combos Quillacollo = 88.80)
silp = Plato("Silpancho", 35, ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"])
moco = Bebida("Mocochinchi", 6, False)
combo_ref = Combo("Combo Silpancho", [silp, moco], 0.10)
assert combo_ref.calcular_precio() == 36.90
pdel_ref = PedidoDelivery(c, "Quillacollo", datetime.now() + timedelta(hours=1))
pdel_ref.agregar_item(combo_ref, 2)
assert pdel_ref.total() == 88.80

# 5. Combo dentro de otro combo
combo_doble = Combo("Mega Combo", [combo_ref, moco], 0.10)
assert combo_doble.calcular_precio() == 38.61

# 6. Pedido para llevar cobra Bs 2 por plato (incluyendo platos de combo)
pllevar = PedidoParaLlevar(c)
pllevar.agregar_item(combo_ref, 2)
assert pllevar.calcular_cargos() == 4.0

# 7. Envio gratis Cercado >= 150 y retraso > 60 min (Regla 9)
pdel_cercado = PedidoDelivery(c, "Cercado", datetime.now() + timedelta(hours=1))
pdel_cercado.agregar_item(chich, 3)
assert pdel_cercado.calcular_cargos() == 0.0
pdel_ref._fecha_hora = datetime.now() - timedelta(minutes=65)
assert pdel_ref.tiene_retraso() == True
assert pdel_ref.calcular_compensacion() == 15.0

# 8. Pagos (QR 10 digitos, Tarjeta 3%, Delivery rechaza tarjeta)
ploc = PedidoLocal(c, 5)
ploc.agregar_item(silp, 2)
assert "Bs 72.10" in ploc.cobrar(PagoTarjeta())
assert "QR (1234567890)" in pdel_ref.cobrar(PagoQR("1234567890"))
assert "Cambio: Bs 22.20" in pllevar.cobrar(PagoEfectivo(100))
print("Todas las pruebas pasaron bien!")