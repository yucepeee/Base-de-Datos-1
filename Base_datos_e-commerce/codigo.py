class PaginaWeb:
    def __init__(self, nombre, marca, nacionalidad, nit, rentabilidad_estimada, modelo, confiabilidad):
        self.nombre = nombre
        self.marca = marca
        self.nacionalidad = nacionalidad
        self.nit = nit
        self.rentabilidad_estimada = rentabilidad_estimada  # Atributo clave analizado por el cliente
        self.modelo = modelo
        self.confiabilidad = confiabilidad
        self.productos_origen = []  # Relación con Producto (1, N)


class Importadora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Relación Provee (1, M)


class Minorista(Importadora):
    def __init__(self, nombre, peso, unidad):
        super().__init__(nombre)
        self.peso = peso          # Para productos pequeños
        self.unidad = unidad      # Para productos medianos/grandes


class Mayorista(Importadora):
    def __init__(self, nombre, espacio):
        super().__init__(nombre)
        self.espacio = espacio    # Espacio en el container


class Producto:
    def __init__(self, id_producto, nombre, nacionalidad, caracteristicas, precio, importadora, pagina_web):
        self.id_producto = id_producto
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.caracteristicas = caracteristicas
        self.precio = precio
        self.importadora = importadora  # Relación Provee (1, N)
        self.pagina_web = pagina_web    # Relación _Se_origina_en_ (1, N)
        
        # Vinculación en ambas direcciones
        importadora.productos.append(self)
        pagina_web.productos_origen.append(self)
        self.compras = []


class Cliente:
    def __init__(self, ci, telefono, nombre_destinatario):
        self.ci = ci
        self.telefono = telefono
        self.nombre_destinatario = nombre_destinatario
        self.compras = []
        self.envios = []


class Compra:
    """Clase de asociación (n, M) entre Producto y Cliente"""
    def __init__(self, producto, cliente, cantidad):
        self.producto = producto
        self.cliente = cliente
        self.cantidad = cantidad
        
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
    """Clase de asociación (n, M) entre Cliente y Agente"""
    def __init__(self, cliente, agente, codigo_seguimiento):
        self.cliente = cliente
        self.agente = agente
        self.codigo_seguimiento = codigo_seguimiento
        
        cliente.envios.append(self)
        agente.envios.append(self)