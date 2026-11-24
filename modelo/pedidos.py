from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

class EstadoPedido(Enum):
    REGISTRADO = "REGISTRADO"
    EN_PREPARACION = "EN_PREPARACION"
    LISTO = "LISTO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"

class ItemPedido:
    def __init__(self, producto, cantidad):
        if not (1 <= cantidad <= 20):
            raise ValueError("Cantidad debe estar entre 1 y 20")
        self._producto = producto
        self._cantidad = cantidad

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

    def subtotal(self):
        return round(self._producto.calcular_precio() * self._cantidad, 2)

class Pedido(ABC):
    def __init__(self, cliente):
        self._estado = EstadoPedido.REGISTRADO
        self._items = []
        self._cliente = cliente
        self._fecha_hora = datetime.now()
        self._pago = None

    @property
    def estado(self):
        return self._estado

    @property
    def items(self):
        return tuple(self._items)

    def mesa_ocupada(self):
        return None

    def tipo_nombre(self):
        return "Pedido"

    def agregar_item(self, prod, cant):
        if self._estado != EstadoPedido.REGISTRADO:
            raise ValueError("Solo se modifica en REGISTRADO")
        self._items.append(ItemPedido(prod, cant))

    def quitar_item(self, prod):
        if self._estado != EstadoPedido.REGISTRADO:
            raise ValueError("Solo se modifica en REGISTRADO")
        antes = len(self._items)
        self._items = [i for i in self._items if i.producto != prod]
        if len(self._items) == antes:
            raise ValueError("El producto no esta en el pedido")

    def cambiar_estado(self, nuevo):
        transiciones = {
            EstadoPedido.REGISTRADO: [EstadoPedido.EN_PREPARACION, EstadoPedido.CANCELADO],
            EstadoPedido.EN_PREPARACION: [EstadoPedido.LISTO],
            EstadoPedido.LISTO: [EstadoPedido.ENTREGADO]
        }
        if nuevo not in transiciones.get(self._estado, []):
            raise ValueError("Transicion invalida")
        self._estado = nuevo

    def calcular_subtotal(self):
        return round(sum(i.subtotal() for i in self._items), 2)

    @abstractmethod
    def calcular_cargos(self):
        pass

    def total(self):
        return round(self.calcular_subtotal() + self.calcular_cargos(), 2)

    def cobrar(self, metodo_pago):
        if not self._items:
            raise ValueError("El pedido no tiene productos")
        self._pago = metodo_pago
        return metodo_pago.procesar_pago(self.total())

class PedidoLocal(Pedido):
    def __init__(self, cliente, mesa):
        super().__init__(cliente)
        if not (1 <= mesa <= 15):
            raise ValueError("Mesa debe ser entre 1 y 15")
        self._mesa = mesa

    def mesa_ocupada(self):
        if self._estado not in (EstadoPedido.ENTREGADO, EstadoPedido.CANCELADO):
            return self._mesa
        return None

    def tipo_nombre(self):
        return "PedidoLocal"

    def calcular_cargos(self):
        return 0.0

class PedidoParaLlevar(Pedido):
    def __init__(self, cliente, costo_envase=2.0):
        super().__init__(cliente)
        self._costo_envase = costo_envase

    def tipo_nombre(self):
        return "PedidoParaLlevar"

    def calcular_cargos(self):
        platos = sum(i.producto.contar_platos() * i.cantidad for i in self._items)
        return round(platos * self._costo_envase, 2)

class PedidoDelivery(Pedido):
    def __init__(self, cliente, zona, hora_entrega):
        super().__init__(cliente)
        self._zona = zona
        self._hora_entrega = hora_entrega

    def tipo_nombre(self):
        return "PedidoDelivery"

    def calcular_cargos(self):
        sub = self.calcular_subtotal()
        if sub < 40:
            raise ValueError("Pedido minimo delivery es Bs 40")
        tarifas = {"cercado": 8.0, "quillacollo": 15.0, "sacaba": 15.0, "vinto": 20.0}
        z = self._zona.lower()
        if z not in tarifas:
            raise ValueError("Zona no cubierta")
        if z == "cercado" and sub >= 150:
            return 0.0
        return tarifas[z]

    def tiene_retraso(self):
        return (datetime.now() - self._fecha_hora).total_seconds() > 3600

    def calcular_compensacion(self):
        return self.calcular_cargos() if self.tiene_retraso() else 0.0

    def cobrar(self, metodo_pago):
        if not metodo_pago.permite_delivery():
            raise ValueError("Delivery solo acepta efectivo o QR")
        return super().cobrar(metodo_pago)