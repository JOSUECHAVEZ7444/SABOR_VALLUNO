from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("Precio debe ser mayor a cero")
        self._precio = round(float(valor), 2)

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def esta_disponible(self, dia):
        pass

    @abstractmethod
    def contar_platos(self):
        pass

class Plato(Producto):
    def __init__(self, nombre, precio, dias_venta):
        super().__init__(nombre, precio)
        self._dias_venta = dias_venta

    def calcular_precio(self):
        return self._precio

    def esta_disponible(self, dia):
        return dia.lower() in [d.lower() for d in self._dias_venta]

    def contar_platos(self):
        return 1

class Bebida(Producto):
    def __init__(self, nombre, precio, es_jarra=False):
        super().__init__(nombre, precio)
        self._es_jarra = es_jarra

    def calcular_precio(self):
        return round(self._precio * 3 if self._es_jarra else self._precio, 2)

    def esta_disponible(self, dia):
        return True

    def contar_platos(self):
        return 0

class Combo(Producto):
    def __init__(self, nombre, partes, descuento=0.10):
        super().__init__(nombre, 1)
        if len(partes) < 2 or self in partes:
            raise ValueError("Combo requiere 2 o mas productos distintos a si mismo")
        self._partes = partes
        self._descuento = descuento

    def calcular_precio(self):
        suma = sum(p.calcular_precio() for p in self._partes)
        return round(suma * (1 - self._descuento), 2)

    def esta_disponible(self, dia):
        return all(p.esta_disponible(dia) for p in self._partes)

    def contar_platos(self):
        return sum(p.contar_platos() for p in self._partes)