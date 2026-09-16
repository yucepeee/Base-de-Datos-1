class PaginaWeb:
    def __init__(self, nombre, marca, nacionalidad, nit):
        self.nombre = nombre
        self.marca = marca
        self.nacionalidad = nacionalidad
        self.nit = nit
        self.productos = []  # Relación con Producto (catalogo/publicación)


class Importadora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Relación Provee (1, N) hacia Producto


class Minorista(Importadora):
    def __init__(self, nombre, modalidad="peso/unidad"):
        super().__init__(nombre)
        self.modalidad = modalidad  # Ej.: peso o unidad


class Mayorista(Importadora):
    def __init__(self, nombre, modalidad="espacio"):
        super().__init__(nombre)
        self.modalidad = modalidad  # Espacio dentro del contenedor


class Producto:
    def __init__(self, id_producto, nombre, nacionalidad, caracteristicas, stock, importadora):
        self.id_producto = id_producto
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.caracteristicas = caracteristicas
        self.stock = stock
        self.importadora = importadora
        self.paginas_web = []
        self.compras = []
        importadora.productos.append(self)

    def publicar_en(self, pagina_web):
        if pagina_web not in self.paginas_web:
            self.paginas_web.append(pagina_web)
        if self not in pagina_web.productos:
            pagina_web.productos.append(self)


class Cliente:
    def __init__(self, ci, telefono, nombre_destinatario):
        self.ci = ci
        self.telefono = telefono
        self.nombre_destinatario = nombre_destinatario
        self.compras = []
        self.envios = []


class Compra:
    """Clase de asociación entre Producto y Cliente."""
    def __init__(self, producto, cliente, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > producto.stock:
            raise ValueError("No hay suficiente stock para realizar la compra.")

        self.producto = producto
        self.cliente = cliente
        self.cantidad = cantidad

        producto.stock -= cantidad
        producto.compras.append(self)
        cliente.compras.append(self)


class Agente:
    def __init__(self, ci, numero, nombre, ciudad, calle_barrio):
        self.ci = ci
        self.numero = numero
        self.nombre = nombre
        self.ciudad = ciudad
        self.calle_barrio = calle_barrio
        self.envios = []


class Envio:
    """Clase de asociación entre Cliente y Agente."""
    def __init__(self, cliente, agente, codigo_seguimiento, peso, costo):
        self.cliente = cliente
        self.agente = agente
        self.codigo_seguimiento = codigo_seguimiento
        self.peso = peso
        self.costo = costo

        cliente.envios.append(self)
        agente.envios.append(self)


class Inventario:
    """Gestión del stock de los productos por tipo o modelo."""
    def __init__(self, productos):
        self.productos = productos

    def listar_productos(self):
        return [producto.nombre for producto in self.productos]

    def filtrar_por_modelo(self, nombre_o_modelo):
        return [producto for producto in self.productos if producto.nombre == nombre_o_modelo]

    def productos_disponibles(self):
        return [producto for producto in self.productos if producto.stock > 0]