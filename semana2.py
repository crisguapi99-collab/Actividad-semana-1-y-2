class Producto:
    def __init__(self, nombre, precio, stock):
        # Atributos privados
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("El stock no puede ser negativo.")

    # Método para reducir stock
    def reducir_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        else:
            print("No hay suficiente stock.")
            return False

    # Mostrar información
    def mostrar_producto(self):
        print("Producto:", self.__nombre)
        print("Precio: $", self.__precio)
        print("Stock:", self.__stock)


# ==========================================
# HERENCIA: PRODUCTO PERECEDERO
# ==========================================

class ProductoPerecedero(Producto):

    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamamos al constructor de Producto
        super().__init__(nombre, precio, stock)

        self.__fecha_caducidad = fecha_caducidad

    def get_fecha_caducidad(self):
        return self.__fecha_caducidad

    def set_fecha_caducidad(self, fecha_caducidad):
        self.__fecha_caducidad = fecha_caducidad

    def mostrar_producto(self):
        super().mostrar_producto()
        print("Fecha de caducidad:", self.__fecha_caducidad)


# ==========================================
# HERENCIA: PRODUCTO NO PERECEDERO
# ==========================================

class ProductoNoPerecedero(Producto):

    def __init__(self, nombre, precio, stock, categoria):
        # Llamamos al constructor de Producto
        super().__init__(nombre, precio, stock)

        self.__categoria = categoria

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def mostrar_producto(self):
        super().mostrar_producto()
        print("Categoría:", self.__categoria)


# ==========================================
# CLASE CLIENTE
# ==========================================

class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula


# ==========================================
# CLASE DETALLE DE VENTA
# ==========================================

class DetalleVenta:

    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def calcular_subtotal(self):
        return self.__producto.get_precio() * self.__cantidad


# ==========================================
# COMPOSICIÓN: CLASE VENTA
# ==========================================

class Venta:

    def __init__(self, cliente):
        self.__cliente = cliente

        # La venta contiene detalles de venta
        self.__detalles = []

    def agregar_detalle(self, detalle):

        producto = detalle.get_producto()
        cantidad = detalle.get_cantidad()

        # Verificar y reducir stock
        if producto.reducir_stock(cantidad):
            self.__detalles.append(detalle)
            print("Producto agregado a la venta.")
        else:
            print("No se pudo agregar el producto.")

    def calcular_total(self):

        total = 0

        for detalle in self.__detalles:
            total += detalle.calcular_subtotal()

        return total

    def mostrar_factura(self):

        print("\n================================")
        print("        TIENDA DE ABASTOS")
        print("             FACTURA")
        print("================================")

        print("Cliente:", self.__cliente.get_nombre())
        print("Cédula:", self.__cliente.get_cedula())

        print("--------------------------------")

        for detalle in self.__detalles:

            producto = detalle.get_producto()
            cantidad = detalle.get_cantidad()
            subtotal = detalle.calcular_subtotal()

            print(
                producto.get_nombre(),
                "x",
                cantidad,
                "= $",
                round(subtotal, 2)
            )

        print("--------------------------------")
        print("TOTAL: $", round(self.calcular_total(), 2))
        print("================================")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

print("========================================")
print("       TIENDA DE ABASTOS")
print("         SEMANA 2 - POO")
print("========================================")


# Crear productos

arroz = ProductoNoPerecedero(
    "Arroz",
    1.50,
    20,
    "Granos"
)

azucar = ProductoNoPerecedero(
    "Azúcar",
    1.20,
    25,
    "Granos"
)

leche = ProductoPerecedero(
    "Leche",
    1.10,
    15,
    "30/08/2026"
)


# Mostrar productos

print("\n--- PRODUCTO NO PERECEDERO ---")
arroz.mostrar_producto()

print("\n--- PRODUCTO NO PERECEDERO ---")
azucar.mostrar_producto()

print("\n--- PRODUCTO PERECEDERO ---")
leche.mostrar_producto()


# Crear cliente

cliente = Cliente(
    "Juan Pérez",
    "0102030405"
)


# Crear venta

venta = Venta(cliente)


# Crear detalles

detalle_arroz = DetalleVenta(arroz, 2)

detalle_leche = DetalleVenta(leche, 3)

detalle_azucar = DetalleVenta(azucar, 1)


# Agregar productos a la venta

print("\n--- REGISTRANDO VENTA ---")

venta.agregar_detalle(detalle_arroz)

venta.agregar_detalle(detalle_leche)

venta.agregar_detalle(detalle_azucar)


# Mostrar factura

venta.mostrar_factura()


# Mostrar stock después de la venta

print("\n--- STOCK DESPUÉS DE LA VENTA ---")

print(
    arroz.get_nombre(),
    ":",
    arroz.get_stock(),
    "unidades"
)

print(
    leche.get_nombre(),
    ":",
    leche.get_stock(),
    "unidades"
)

print(
    azucar.get_nombre(),
    ":",
    azucar.get_stock(),
    "unidades"
)