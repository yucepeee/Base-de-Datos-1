# 📚 Unidad 1: Entrevista, Diagrama E-R y Diagrama UML

## 🛒 Proyecto de curso

**Sistema de gestión de un negocio de comercio electrónico**

Proyecto realizado para la materia **Base de Datos 1** de la carrera de Ingeniería Informática de la Universidad Autónoma Gabriel René Moreno (UAGRM).

* **Materia:** Base de Datos 1

* **Registro:** 220000417

* **Autor:** Gabriel Romulo Arnez Joven

* **Docente:** Ing. Juan Carlos Peinado Pereira

## 1. 🏪 Descripción del negocio

Se desea diseñar una base de datos para la venta en línea de productos tecnológicos. El cliente necesita mejorar la administración de los productos que compra a través de páginas web y organizar la gestión de su negocio.

Desde la página web, los clientes podrán consultar un catálogo de productos disponibles y comprar uno o varios artículos. Los productos podrán ser recogidos por el cliente o entregados mediante un envío. El objetivo es permitir el crecimiento del negocio, pasando de vendedor minorista a mayorista y ofreciendo sus productos a nivel nacional.

El cliente depende de importadoras privadas para traer sus productos, por lo que la base de datos debe contemplar las modalidades de trabajo de cada importadora:

* **Minorista por peso:** productos pequeños transportados según su peso.

* **Minorista por unidad:** productos medianos, como laptops, o productos más grandes transportados por unidad.

* **Mayorista por espacio:** compra de un espacio dentro de un contenedor. En esta modalidad se puede traer todo lo que entre en el espacio contratado, sin tomar en cuenta la cantidad de productos.

## 2. 🎯 Objetivo de la base de datos

Diseñar una base de datos que permita:

* Registrar los productos disponibles y sus características.

* Organizar el catálogo de productos publicado en las páginas web.

* Mantener la información de los clientes y sus datos de contacto.

* Registrar las importadoras que proveen los productos.

* Identificar la modalidad de importación utilizada: peso, unidad o espacio dentro de un contenedor.

* Gestionar las compras realizadas por los clientes.

* Registrar los datos del agente responsable de cada envío.

* Monitorear el stock disponible de cada producto y su disponibilidad para la venta.

## 3. 🧩 Entidades y atributos

### 📦 Producto

Representa cada artículo tecnológico que el negocio compra y ofrece para la venta.

* **ID**: identificador del producto.

* **Nombre**: nombre o modelo del producto.

* **Precio**: precio unitario de venta.

* **Características**: especificaciones principales del producto.

* **Stock**: cantidad disponible para la venta.

### 👤 Cliente

Representa a la persona que consulta y compra uno o varios productos.

* **C.I.**: documento de identidad del cliente.

* **Teléfono**: número de contacto.

* **Nombre del destinatario**: nombre de la persona que recibirá el pedido.

### 🌐 Páginas Web

Representa el medio digital utilizado para publicar y ofrecer los productos.

* **Marca**: marca comercial asociada.

* **Modelo**: modelo o variante de gestión en la web.

* **Rentabilidad Estimada**: porcentaje o valor de rentabilidad proyectada.

* **Confiabilidad**: índice de confiabilidad de la fuente.

### 🚚 Importadora

Representa a la empresa privada que provee los productos al negocio.

La importación puede realizarse bajo las siguientes modalidades:

* **Minorista por peso**: transporte de productos pequeños según su peso.

* **Minorista por unidad**: transporte de productos medianos o grandes por unidad.

* **Mayorista por espacio**: contratación de un espacio dentro de un contenedor, sin considerar la cantidad de productos que entren en él.

### 🧑‍💼 Agente

Representa a la persona encargada de realizar o gestionar la entrega de un pedido.

* **C.I.**: documento de identidad del agente.

* **Número**: identificador del agente.

* **Nombre**: nombre del agente.

* **Ciudad**: ciudad donde se realiza la entrega.

* **Calle/Barrio**: ubicación del domicilio o punto de entrega.

### 🧾 Compra

Representa la compra de un producto realizada por ekl cliente e incluye la cantidad adquirida.

### 🚚 Envío

Representa la entrega solicitada por un cliente e incluye el código de seguimiento.

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

![Diagrama entidad-relación](assets/Diagrama%20E-R-cortado.png)

### Diagrama UML

El diagrama UML representa las clases principales del sistema, sus atributos, operaciones y algunas relaciones de especialización y asociación:

![Diagrama UML](assets/Diagrama%20UML.drawio.png)

## 📐 FASE 2: Diseño Lógico y Normalización

### 1. Normalización de Tablas (1FN, 2FN, 3FN)

A continuación, se demuestra el proceso de normalización aplicado al esquema relacional derivado del diagrama E-R, garantizando la integridad de los datos y la eliminación de redundancias.

| Tabla | 1FN (Atomicidad) | 2FN (Dependencia Total) | 3FN (Sin Dependencia Transitiva) | Justificación de Normalización |
| :--- | :---: | :---: | :---: | :--- |
| **`paginas_web`** | ✔️ | ✔️ | ✔️ | Todos los atributos (marca, modelo) son atómicos. PK simple (`id_pagina`), por lo que no hay dependencias parciales. Ningún atributo no clave depende de otro no clave. |
| **`importadoras`** | ✔️ | ✔️ | ✔️ | Atributos atómicos. PK simple (`id_importadora`). La herencia (Minorista/Mayorista) se maneja sin redundancias estructurales. |
| **`productos`** | ✔️ | ✔️ | ✔️ | Se extrajeron los datos de importadoras y páginas web a sus propias tablas, vinculándolas mediante Claves Foráneas (FK). Esto elimina las dependencias transitivas. |
| **`clientes`** | ✔️ | ✔️ | ✔️ | No existen grupos repetitivos (un solo teléfono registrado por campo). Los atributos dependen funcionalmente de forma total y exclusiva del `ci`. |
| **`agentes`** | ✔️ | ✔️ | ✔️ | Datos de ubicación y contacto atómicos. Todas las columnas dependen únicamente de la clave primaria `ci`. |
| **`compras`** | ✔️ | ✔️ | ✔️ | Tabla asociativa. El atributo `cantidad` depende directamente de la transacción (la combinación de Cliente y Producto), cumpliendo la 2FN. |
| **`envios`** | ✔️ | ✔️ | ✔️ | Tabla asociativa. El `codigo_seguimiento` depende completamente de la generación del envío específico entre el Cliente y el Agente. |

### 2. Diccionario de Datos Técnico

| Tabla | Columna / Campo | Tipo de Dato Lógico | Restricción (Nulidad / Claves) | Descripción | 
| ----- | ----- | ----- | ----- | ----- | 
| **paginas_web** | `id_pagina` | INT / SERIAL | PK, NOT NULL | Identificador único de la plataforma de origen. | 
|  | `marca` | VARCHAR(100) | NOT NULL | Marca comercial de la página web de compra. | 
|  | `modelo` | VARCHAR(100) | NOT NULL | Modelo o variante de gestión en la web. | 
|  | `rentabilidad_estimada` | FLOAT | NOT NULL | Porcentaje o valor de rentabilidad proyectada. | 
|  | `confiabilidad` | FLOAT | NOT NULL | Índice de confiabilidad de la fuente. | 
| **importadoras** | `id_importadora` | INT / SERIAL | PK, NOT NULL | Identificador de la importadora proveedora. | 
|  | `nombre` | VARCHAR(100) | NOT NULL | Nombre comercial de la importadora. | 
|  | `peso` / `unidad` / `espacio` | VARCHAR(100) | NULLABLE | Atributos específicos según la modalidad (Minorista/Mayorista). | 
| **productos** | `id_producto` | VARCHAR(50) | PK, NOT NULL | Código o identificador único del artículo tecnológico. | 
|  | `nombre` | VARCHAR(150) | NOT NULL | Nombre o modelo comercial del producto. | 
|  | `precio` | FLOAT | NOT NULL | Precio unitario de venta. | 
|  | `caracteristicas` | TEXT | NULLABLE | Especificaciones técnicas del artículo. | 
|  | `stock` | INT | NOT NULL | Cantidad disponible en inventario. | 
|  | `id_importadora` | INT | FK, NOT NULL | Proveedor que suministra el producto. | 
|  | `id_pagina` | INT | FK, NOT NULL | Página web donde se origina el producto. | 
| **clientes** | `ci` | VARCHAR(20) | PK, NOT NULL | Cédula de identidad o documento del cliente. | 
|  | `telefono` | VARCHAR(20) | NOT NULL | Número de contacto telefónico. | 
|  | `nombre_destinatario` | VARCHAR(150) | NOT NULL | Nombre de la persona que recibirá el pedido. | 
| **agentes** | `ci` | VARCHAR(20) | PK, NOT NULL | Cédula de identidad del agente de entrega. | 
|  | `numero` | INT | NOT NULL | Número identificador interno del agente. | 
|  | `nombre` | VARCHAR(150) | NOT NULL | Nombre completo del agente. | 
|  | `ciudad` | VARCHAR(100) | NOT NULL | Ciudad donde opera el agente. | 
|  | `calle_barrio` | VARCHAR(150) | NOT NULL | Dirección física o zona de entrega. | 
| **compras** | `id_compra` | INT / SERIAL | PK, NOT NULL | Identificador de la transacción de compra. | 
|  | `id_producto` | VARCHAR(50) | FK, NOT NULL | Producto adquirido. | 
|  | `ci_cliente` | VARCHAR(20) | FK, NOT NULL | Cliente que efectúa la compra. | 
|  | `cantidad` | INT | NOT NULL | Cantidad de unidades compradas. | 
| **envios** | `id_envio` | INT / SERIAL | PK, NOT NULL | Identificador del registro de envío. | 
|  | `ci_cliente` | VARCHAR(20) | FK, NOT NULL | Cliente destinatario del envío. | 
|  | `ci_agente` | VARCHAR(20) | FK, NOT NULL | Agente asignado para la entrega. | 
|  | `codigo_seguimiento` | VARCHAR(100) | NOT NULL, UNIQUE | Código de rastreo del paquete. | 

