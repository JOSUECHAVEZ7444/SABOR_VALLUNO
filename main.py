from datetime import datetime, timedelta
from restaurante import Restaurante
from modelo.clientes import Cliente
from modelo.productos import Plato, Bebida, Combo
from modelo.pedidos import PedidoLocal, PedidoParaLlevar, PedidoDelivery, EstadoPedido
from modelo.pagos import PagoEfectivo, PagoQR, PagoTarjeta

rest = Restaurante()
todos_dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
p1 = Plato("Silpancho", 35, todos_dias)
p2 = Plato("Pique Macho", 70, todos_dias)
p3 = Plato("Chicharron", 60, ["Domingo"])
p4 = Plato("Sopa de Mani", 15, todos_dias)
b1 = Bebida("Mocochinchi", 6, False)
b2 = Bebida("Jarra Chicha", 8, True)
c1 = Combo("Combo Silpancho", [p1, b1], 0.10)
for x in [p1, p2, p3, p4, b1, b2, c1]:
    rest.registrar_producto(x)

opciones = [
    "1. Ver menu del dia",
    "2. Registrar producto o combo",
    "3. Registrar cliente",
    "4. Crear pedido",
    "5. Quitar producto de pedido",
    "6. Cambiar estado pedido",
    "7. Cobrar pedido",
    "8. Reporte de ventas",
    "0. Salir"
]
tipos_prod = ["1. Plato", "2. Bebida", "3. Combo"]
tipos_pedido = ["1. Local", "2. Para llevar", "3. Delivery"]
metodos_pago = ["1. Efectivo", "2. QR", "3. Tarjeta"]

while True:
    print("MENU PRINCIPAL")
    for op_texto in opciones:
        print(op_texto)
    op = input("Opcion: ")
    print()
    try:
        if op == "1":
            dia = input("Dia: ")
            for p in rest.menu_dia(dia):
                print(f"- {p.nombre}: Bs {p.calcular_precio():.2f}")
        elif op == "2":
            for tp in tipos_prod:
                print(tp)
            t = input("Tipo: ")
            print()
            if t not in ("1", "2", "3"):
                raise ValueError("Tipo de producto invalido")
            nom = input("Nombre: ")
            if t == "1":
                dias = input("Dias (separados por coma): ").split(",")
                rest.registrar_producto(Plato(nom, float(input("Precio: ")), [d.strip() for d in dias]))
            elif t == "2":
                jarra = input("Es jarra? (s/n): ").lower() == "s"
                rest.registrar_producto(Bebida(nom, float(input("Precio vaso: ")), jarra))
            elif t == "3":
                for idx, p in enumerate(rest.productos, 1):
                    print(f"{idx}. {p.nombre}")
                nums = input("Numeros separados por coma (Ejemplo: 1,5): ").split(",")
                partes = []
                for n in nums:
                    pos = int(n.strip())
                    if not (1 <= pos <= len(rest.productos)):
                        raise ValueError("Numero de producto fuera de rango")
                    partes.append(rest.productos[pos - 1])
                rest.registrar_producto(Combo(nom, partes, 0.10))
            print("Producto registrado")
        elif op == "3":
            rest.registrar_cliente(Cliente(input("Nombre: "), input("Telefono (8 digitos): ")))
            print("Cliente guardado")
        elif op == "4":
            if not rest.clientes:
                print("Registre un cliente primero\n")
                continue
            cli = rest.clientes[-1]
            for tp in tipos_pedido:
                print(tp)
            t = input("Tipo: ")
            print()
            if t == "1": ped = PedidoLocal(cli, int(input("Mesa (1-15): ")))
            elif t == "2": ped = PedidoParaLlevar(cli)
            elif t == "3": ped = PedidoDelivery(cli, input("Zona (Cercado/Quillacollo/Sacaba/Vinto): "), datetime.now() + timedelta(minutes=60))
            else: raise ValueError("Tipo de pedido invalido")
            print()
            while True:
                for idx, p in enumerate(rest.productos, 1):
                    print(f"{idx}. {p.nombre} (Bs {p.calcular_precio():.2f})")
                sel = int(input("Producto num: "))
                if not (1 <= sel <= len(rest.productos)):
                    raise ValueError("Numero de producto invalido")
                cant = int(input("Cantidad (1-20): "))
                ped.agregar_item(rest.productos[sel - 1], cant)
                if input("Agregar otro producto? (s/n): ").lower() != "s":
                    break
            rest.registrar_pedido(ped)
            print(f"\nSubtotal: Bs {ped.calcular_subtotal():.2f} | Cargos: Bs {ped.calcular_cargos():.2f} | Total: Bs {ped.total():.2f}")
        elif op in ("5", "6", "7"):
            if not rest.pedidos:
                print("Registre un pedido primero\n")
                continue
            ped = rest.pedidos[-1]
            if op == "5":
                if not ped.items:
                    print("El pedido no tiene productos\n")
                    continue
                for idx, it in enumerate(ped.items, 1):
                    print(f"{idx}. {it.producto.nombre} x{it.cantidad}")
                sel = int(input("Numero de item a quitar: "))
                if not (1 <= sel <= len(ped.items)):
                    raise ValueError("Numero de item invalido")
                ped.quitar_item(ped.items[sel - 1].producto)
                print("Producto quitado del pedido")
            elif op == "6":
                est = input("Estado (EN_PREPARACION/LISTO/ENTREGADO/CANCELADO): ").upper()
                ped.cambiar_estado(EstadoPedido[est])
                print("Estado actualizado")
            elif op == "7":
                for mp_texto in metodos_pago:
                    print(mp_texto)
                mp = input("Pago: ")
                print()
                if mp == "1": pago = PagoEfectivo(float(input("Monto recibido: ")))
                elif mp == "2": pago = PagoQR(input("Codigo transaccion (10 digitos): "))
                elif mp == "3": pago = PagoTarjeta()
                else: raise ValueError("Metodo de pago invalido")
                print(ped.cobrar(pago))
        elif op == "8":
            tipos, top = rest.reporte_ventas()
            print("Ventas por tipo:", tipos)
            print("Top 3:", top)
        elif op == "0":
            break
        else:
            print("Opcion invalida")
    except Exception as e:
        print("Error:", e)
    print()