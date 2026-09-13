# Unidad 1: Entrevista y Diagrama Entidad-Relación

## Proyecto de curso

**Sistema de gestión de un negocio de comercio electrónico**

Proyecto realizado para la materia **Base de Datos 1** de la carrera de Ingeniería Informática de la Universidad Autónoma Gabriel René Moreno (UAGRM).

- **Materia:** Base de Datos 1
- **Registro:** 220000417
- **Autor:** Gabriel Romulo Arnez Joven
- **Docente:** Ing. Juan Carlos Peinado Pereira

## 1. Contexto del negocio

El negocio se dedica a la compra y venta de productos tecnológicos mediante una página web. Actualmente requiere una solución de base de datos que permita organizar sus productos, clientes, proveedores y entregas, con el objetivo de mejorar la administración y ampliar sus ventas a nivel nacional.

El negocio adquiere productos mediante empresas importadoras privadas. Dependiendo del tipo de importación, los productos pueden transportarse por peso, por unidad o por espacio dentro de un contenedor. Después, los productos se ofrecen a los clientes a través de páginas web y pueden entregarse mediante recojo o envío.

## 2. Objetivo de la base de datos

Diseñar una base de datos que permita:

- Registrar los productos disponibles y sus características.
- Mantener la información de los clientes y sus datos de contacto.
- Registrar las importadoras que proveen los productos.
- Identificar el tipo de servicio de importación utilizado.
- Gestionar las compras realizadas por los clientes.
- Registrar los datos del agente responsable de cada envío.
- Administrar la información de las páginas web utilizadas por el negocio.

## 3. Entidades y atributos

### Producto

Representa cada artículo tecnológico que el negocio compra y ofrece para la venta.

- **ID**: identificador del producto.
- **Nombre**: nombre o modelo del producto.
- **Características**: especificaciones principales del producto.
- **Nacionalidad**: país de procedencia o fabricación.

### Cliente

Representa a la persona que consulta y compra uno o varios productos.

- **C.I.**: documento de identidad del cliente.
- **Nombre del destinatario**: nombre de la persona que recibirá el pedido.
- **Teléfono**: número de contacto.

### Páginas Web

Representa el medio digital utilizado para publicar y ofrecer los productos.

- **Nombre**: nombre de la página o plataforma.
- **Marca**: marca comercial asociada.
- **NIT**: identificación tributaria.
- **Nacionalidad**: país asociado a la página o empresa.

### Importadora

Representa a la empresa privada que provee los productos al negocio.

La importación puede realizarse bajo las siguientes modalidades:

- **Minorista**: transporte de productos pequeños por peso o de productos medianos y grandes por unidad.
- **Mayorista**: contratación de un espacio dentro de un contenedor para transportar los productos.

### Agente

Representa a la persona encargada de realizar o gestionar la entrega de un pedido.

- **Número**: identificador del agente.
- **Nombre**: nombre del agente.
- **C.I.**: documento de identidad del agente.
- **Ciudad**: ciudad donde se realiza la entrega.
- **Calle/Barrio**: ubicación del domicilio o punto de entrega.

## 4. Relaciones

### Provee

Relaciona una `Importadora` con los `Productos` que suministra. Una importadora puede proveer varios productos y un producto puede ser provisto por varias importadoras, de acuerdo con la cardinalidad **N:M** del diagrama.

### Compra

Relaciona un `Cliente` con los `Productos` que adquiere. Un cliente puede comprar uno o varios productos y un producto puede ser comprado por varios clientes. Esta relación representa la operación principal de venta del negocio y tiene cardinalidad **N:M**.

### Envío

Relaciona al `Cliente` con el `Agente` que gestiona la entrega. Un cliente puede recibir envíos y un agente puede encargarse de envíos para varios clientes. La relación se representa con cardinalidad **N:M** en el diagrama.

## 5. Reglas del negocio

1. Cada producto debe contar con un identificador único.
2. Un cliente puede comprar uno o varios productos.
3. Una importadora puede proveer uno o varios productos.
4. La importación puede gestionarse bajo una modalidad minorista o mayorista.
5. Los pedidos pueden ser recogidos por el cliente o entregados mediante envío.
6. Para realizar un envío se deben registrar los datos del destinatario y la ubicación de entrega.
7. El agente debe identificarse mediante su número, nombre y documento de identidad.

## 6. Diagrama entidad-relación

El siguiente diagrama muestra las entidades, atributos, relaciones y cardinalidades identificadas durante el análisis del negocio:

![Diagrama entidad-relación](diagrama-er-github.svg)

El archivo editable original de diagrams.net se conserva en [Diagrama E-R.drawio.svg](Diagrama%20E-R.drawio.svg).

> **Observación:** en la versión actual del modelo, `Páginas Web` aparece como entidad con sus atributos, pero no tiene una relación visible con `Producto`. Si se desea registrar qué productos se publican en cada página, se puede agregar una relación entre ambas entidades.

## 7. Conclusión

El modelo entidad-relación organiza la información esencial del negocio de comercio electrónico y establece cómo se relacionan los productos, clientes, importadoras, páginas web y agentes de envío. Este diseño constituye la base para transformar el modelo conceptual en un modelo lógico y posteriormente implementarlo en un sistema gestor de bases de datos.

