# 📚 Unidad 1: Entrevista, Diagrama E-R y Diagrama UML

## 🛒 Proyecto de curso

**Sistema de gestión de un negocio de comercio electrónico**

Proyecto realizado para la materia **Base de Datos 1** de la carrera de Ingeniería Informática de la Universidad Autónoma Gabriel René Moreno (UAGRM).

- **Materia:** Base de Datos 1
- **Registro:** 220000417
- **Autor:** Gabriel Romulo Arnez Joven
- **Docente:** Ing. Juan Carlos Peinado Pereira

## 1. 🏪 Descripción del negocio

Se desea diseñar una base de datos para la venta en línea de productos tecnológicos. El cliente necesita mejorar la administración de los productos que compra a través de páginas web y organizar la gestión de su negocio.

Desde la página web, los clientes podrán consultar un catálogo de productos disponibles y comprar uno o varios artículos. Los productos podrán ser recogidos por el cliente o entregados mediante un envío. El objetivo es permitir el crecimiento del negocio, pasando de vendedor minorista a mayorista y ofreciendo sus productos a nivel nacional.

El cliente depende de importadoras privadas para traer sus productos, por lo que la base de datos debe contemplar las modalidades de trabajo de cada importadora:

- **Minorista por peso:** productos pequeños transportados según su peso.
- **Minorista por unidad:** productos medianos, como laptops, o productos más grandes transportados por unidad.
- **Mayorista por espacio:** compra de un espacio dentro de un contenedor. En esta modalidad se puede traer todo lo que entre en el espacio contratado, sin tomar en cuenta la cantidad de productos.

## 2. 🎯 Objetivo de la base de datos

Diseñar una base de datos que permita:

- Registrar los productos disponibles y sus características.
- Organizar el catálogo de productos publicado en las páginas web.
- Mantener la información de los clientes y sus datos de contacto.
- Registrar las importadoras que proveen los productos.
- Identificar la modalidad de importación utilizada: peso, unidad o espacio dentro de un contenedor.
- Gestionar las compras realizadas por los clientes.
- Registrar los datos del agente responsable de cada envío.
- Monitorear el stock disponible de cada producto y su disponibilidad para la venta.

## 3. 🧩 Entidades y atributos

### 📦 Producto

Representa cada artículo tecnológico que el negocio compra y ofrece para la venta.

- **ID**: identificador del producto.
- **Nombre**: nombre o modelo del producto.
- **Características**: especificaciones principales del producto.
- **Nacionalidad**: país de procedencia o fabricación.
- **Stock**: cantidad disponible para la venta.

### 👤 Cliente

Representa a la persona que consulta y compra uno o varios productos.

- **C.I.**: documento de identidad del cliente.
- **Nombre del destinatario**: nombre de la persona que recibirá el pedido.
- **Teléfono**: número de contacto.

### 🌐 Páginas Web

Representa el medio digital utilizado para publicar y ofrecer los productos.

- **Nombre**: nombre de la página o plataforma.
- **Marca**: marca comercial asociada.
- **NIT**: identificación tributaria.
- **Nacionalidad**: país asociado a la página o empresa.

### 🚚 Importadora

Representa a la empresa privada que provee los productos al negocio.

La importación puede realizarse bajo las siguientes modalidades:

- **Minorista por peso**: transporte de productos pequeños según su peso.
- **Minorista por unidad**: transporte de productos medianos o grandes por unidad.
- **Mayorista por espacio**: contratación de un espacio dentro de un contenedor, sin considerar la cantidad de productos que entren en él.

### 🧑‍💼 Agente

Representa a la persona encargada de realizar o gestionar la entrega de un pedido.

- **Número**: identificador del agente.
- **Nombre**: nombre del agente.
- **C.I.**: documento de identidad del agente.
- **Ciudad**: ciudad donde se realiza la entrega.
- **Calle/Barrio**: ubicación del domicilio o punto de entrega.

### 📊 Inventario

Se considera una función de gestión del stock de los productos, no una entidad independiente del modelo. La disponibilidad se administra por tipo de producto, identificando cada artículo según su nombre o modelo, sin considerar nacionalidad ni otra clasificación como criterio principal.

### 🧾 Compra

Representa la compra de un producto realizada por un cliente e incluye la cantidad adquirida.

### 🚚 Envío

Representa la entrega solicitada por un cliente e incluye el código de seguimiento, el peso del paquete y el costo del envío.

## 4. 🔗 Relaciones

### 📥 Provee

Relaciona una `Importadora` con los `Productos` que suministra. Una importadora puede proveer varios productos y un producto puede ser provisto por varias importadoras, de acuerdo con la cardinalidad **N:M** del diagrama E-R. En el diagrama UML, `Minorista` y `Mayorista` especializan a `Importadora`.

### 🛍️ Compra

Relaciona un `Cliente` con los `Productos` que adquiere. Un cliente puede realizar varias compras y un producto puede formar parte de las compras de varios clientes. La clase `Compra` registra la cantidad adquirida y representa esta relación **N:M**.

### 📦 Envío

Relaciona al `Cliente` con el `Agente` que gestiona la entrega. Un cliente puede recibir varios envíos y un agente puede encargarse de envíos para varios clientes. La clase `Envio` registra los datos de seguimiento y la relación se representa con cardinalidad **N:M** en el diagrama E-R.

### 📊 Inventario

El `Inventario` consiste en la gestión del stock disponible de cada producto, identificado principalmente por su nombre o modelo. Las consultas se concentran en la disponibilidad del artículo y no en segmentaciones por nacionalidad ni en otros criterios ajenos al tipo de producto.

## 5. 📋 Reglas del negocio

1. Cada producto debe contar con un identificador único, un nombre o modelo y una cantidad disponible en stock.
2. Los productos deben publicarse en un catálogo accesible desde las páginas web del negocio.
3. Un cliente puede comprar uno o varios productos y cada compra debe registrar la cantidad adquirida.
4. Una importadora puede proveer uno o varios productos.
5. La importación puede gestionarse por peso, por unidad o por espacio dentro de un contenedor.
6. Los pedidos pueden ser recogidos por el cliente o entregados mediante envío.
7. Para realizar un envío se deben registrar los datos del destinatario, la ubicación de entrega y el código de seguimiento.
8. El agente debe identificarse mediante su número, nombre y documento de identidad.

## 6. 🗺️ Diagramas del sistema

### Diagrama entidad-relación

El diagrama E-R muestra las entidades, atributos, relaciones y cardinalidades identificadas durante el análisis del negocio:

![Diagrama entidad-relación](assets/Diagrama%20E-R.drawio.png)

### Diagrama UML

El diagrama UML representa las clases principales del sistema, sus atributos, operaciones y algunas relaciones de especialización y asociación:

![Diagrama UML](assets/Diagrama%20UML.drawio.png)

> **Observaciones del modelo:** `PaginaWeb` se interpreta como una entidad asociada al catálogo o publicación de productos, sin constituir una entidad fuerte del negocio por sí sola. El inventario se representa como una funcionalidad de gestión sobre el stock de `Producto`, en lugar de una entidad independiente. La relación entre `Producto` y `PaginaWeb` debe definirse como publicación de un catálogo o disponibilidad en una o varias plataformas.

## 7. ✅ Conclusión

El modelo entidad-relación organiza la información esencial del negocio de comercio electrónico y establece cómo se relacionan los productos, clientes, importadoras, páginas web y agentes de envío. El diagrama UML complementa este modelo al representar las clases, operaciones y especializaciones relacionadas con la compra, la entrega y la gestión del stock de los productos. Ambos diseños constituyen una base para transformar el modelo conceptual en un modelo lógico y posteriormente implementarlo en un sistema gestor de bases de datos.

