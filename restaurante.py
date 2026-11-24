from modelo.pedidos import EstadoPedido

class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.pedidos = []

    def registrar_producto(self, prod):
        self.productos.append(prod)

    def registrar_cliente(self, cli):
        self.clientes.append(cli)

    def registrar_pedido(self, ped):
        mesa_nueva = ped.mesa_ocupada()
        if mesa_nueva is not None:
            for p in self.pedidos:
                if p.mesa_ocupada() == mesa_nueva:
                    raise ValueError("Mesa ocupada con pedido abierto")
        self.pedidos.append(ped)

    def menu_dia(self, dia):
        return [p for p in self.productos if p.esta_disponible(dia)]

    def reporte_ventas(self):
        por_tipo = {}
        conteo = {}
        for p in self.pedidos:
            if p.estado != EstadoPedido.CANCELADO:
                tipo = p.tipo_nombre()
                por_tipo[tipo] = round(por_tipo.get(tipo, 0) + p.total(), 2)
                for it in p.items:
                    nom = it.producto.nombre
                    conteo[nom] = conteo.get(nom, 0) + it.cantidad
        top3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
        return por_tipo, top3