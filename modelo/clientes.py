class Cliente:
    def __init__(self, nombre, telefono):
        self._nombre = nombre
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        v = str(valor)
        if len(v) != 8 or not v.isdigit() or v[0] not in ("6", "7"):
            raise ValueError("Telefono debe tener 8 digitos y empezar en 6 o 7")
        self._telefono = v