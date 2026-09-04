# Actividad-semana-1-2-y-3
Examen: Presentación y explicacion del proyecto
Objetivo

# Tienda de Abastos - Proyecto POO

## Descripcion

Este proyecto consiste en desarrollar un pequeño sistema para una **tienda de abastos**, utilizando conceptos de **Programación Orientada a Objetos (POO)** en Python.

El proyecto se fue desarrollando durante tres semanas. En cada semana fui agregando nuevos conceptos y funcionalidades al programa.

La idea principal es manejar **productos, clientes y ventas** de una tienda de abastos.

---

## Semana 1 - Encapsulamiento

En la primera semana trabaje los conceptos basicos de Programacion Orientada a Objetos.

Las clases utilizadas fueron:

* `Producto`
* `Cliente`

La clase `Producto` contiene:

* Nombre
* Precio
* Stock

La clase `Cliente` contiene:

* Nombre
* Cédula

### Encapsulamiento

Utilice atributos privados colocando `__` antes del nombre del atributo:

```python
self.__nombre
self.__precio
self.__stock
```

Para acceder y modificar estos atributos utilice **getters y setters**.

Ejemplo:

```python
arroz.get_precio()
arroz.set_precio(1.60)
```

Tambien agregue validaciones para evitar valores negativos en el precio y el stock.

### Lo aprendido

* Clases
* Objetos
* Atributos
* Metodos
* Encapsulamiento
* Getters y setters
* Validaciones

---

## Semana 2 - Herencia y composicion

En la segunda semana continue con el mismo proyecto y agregue nuevos conceptos de POO.

A partir de la clase `Producto` cree:

```python
class ProductoPerecedero(Producto):
```

y:

```python
class ProductoNoPerecedero(Producto):
```

Estas clases utilizan **herencia**, ya que heredan las caracteristicas principales de `Producto`.

El producto perecedero tiene como dato adicional la fecha de caducidad y el producto no perecedero tiene una categoria.

Tambien agregue:

* `DetalleVenta`
* `Venta`

La clase `Venta` contiene varios objetos `DetalleVenta`, por lo que se aplica el concepto de **composicion**.

Tambien agregue el control de stock mediante:

```python
producto.reducir_stock(cantidad)
```

La venta permite calcular:

* Subtotal
* Total
* Stock restante
* Factura

### Lo aprendido

* Herencia
* `super()`
* Composicion
* Relacion entre clases
* Control de stock
* Calculo de ventas
* Generacion de facturas

---

## Semana 3 - Abstracción y polimorfismo

En la tercera semana continue trabajando sobre el mismo proyecto.

En esta parte trabaje con **clases abstractas y polimorfismo**.

La clase `Cliente` paso a ser una clase abstracta:

```python
class Cliente(ABC):
```

Tambien agregue un metodo abstracto:

```python
@abstractmethod
def calcularDescuento(self, subtotal):
    pass
```

Despues cree dos tipos de clientes:

```python
class ClienteMayorista(Cliente):
```

y:

```python
class ClienteMinorista(Cliente):
```

El cliente mayorista recibe un descuento del **15%**:

```python
descuento = subtotal * 0.15
```

Mientras que el cliente minorista recibe un descuento del **5%**:

```python
descuento = subtotal * 0.05
```

### Polimorfismo

El polimorfismo se puede observar cuando ambos tipos de clientes utilizan el mismo metodo:

```python
calcularDescuento()
```

pero cada clase realiza el calculo de una manera diferente.

En la clase `Venta` solamente se llama:

```python
self.__cliente.calcularDescuento(subtotal)
```

y dependiendo del tipo de cliente se aplica automáticamente el descuento correspondiente.

### Lo aprendido

* Clases abstractas
* `ABC`
* `@abstractmethod`
* Herencia
* Sobrescritura de metodos
* Polimorfismo

---

## Estructura del proyecto

```text
Tienda de Abastos
│
├── Producto
│   ├── ProductoPerecedero
│   └── ProductoNoPerecedero
│
├── Cliente
│   ├── ClienteMayorista
│   └── ClienteMinorista
│
├── DetalleVenta
│
└── Venta
```

---

## Funcionamiento

El programa funciona de la siguiente manera:

1. Se crean los productos de la tienda.
2. Se crean los clientes.
3. Se define el tipo de cliente.
4. Se crea una venta.
5. Se agregan productos.
6. Se calcula el subtotal.
7. Se aplica el descuento.
8. Se calcula el total.
9. Se muestra la factura.

---

## Tecnologias utilizadas

* Python
* Programacion Orientada a Objetos
* Visual Studio Code
* Git
* GitHub

---

## Objetivo

El objetivo de este proyecto fue aprender y aplicar los principales conceptos de **Programacion Orientada a Objetos** mediante un ejemplo sencillo de una tienda de abastos.

El proyecto fue creciendo durante las tres semanas. Primero trabaje con clases, objetos y encapsulamiento. Despues agregue herencia y composicion, y finalmente implemente abstraccion y polimorfismo.

Con esto pude entender mejor como organizar un programa utilizando diferentes conceptos de POO.

---

## Autor

**Cristhian Geovanny Guapi Yumailla**

Proyecto realizado como parte de las actividades de Programación Orientada a Objetos.
