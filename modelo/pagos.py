from abc import ABC, abstractmethod

class MetodoPago(ABC):
    def __init__(self):
        self._monto_total = 0.0

    def permite_delivery(self):
        return True

    @abstractmethod
    def procesar_pago(self, total):
        pass

class PagoEfectivo(MetodoPago):
    def __init__(self, monto_recibido):
        super().__init__()
        self._monto_recibido = monto_recibido
        self._cambio = 0.0

    def procesar_pago(self, total):
        if self._monto_recibido < total:
            raise ValueError("Monto insuficiente")
        self._monto_total = round(total, 2)
        self._cambio = round(self._monto_recibido - total, 2)
        return f"Efectivo: Bs {self._monto_total:.2f} | Cambio: Bs {self._cambio:.2f}"

class PagoQR(MetodoPago):
    def __init__(self, codigo_transaccion):
        super().__init__()
        cod = str(codigo_transaccion)
        if len(cod) != 10 or not cod.isdigit():
            raise ValueError("Codigo QR debe tener 10 digitos")
        self._codigo_transaccion = cod

    def procesar_pago(self, total):
        self._monto_total = round(total, 2)
        return f"QR ({self._codigo_transaccion}): Bs {self._monto_total:.2f}"

class PagoTarjeta(MetodoPago):
    def __init__(self, comision=0.03):
        super().__init__()
        self._comision = comision

    def permite_delivery(self):
        return False

    def procesar_pago(self, total):
        self._monto_total = round(total * (1 + self._comision), 2)
        return f"Tarjeta (inc. 3%): Bs {self._monto_total:.2f}"