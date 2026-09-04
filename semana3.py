from abc import ABC, abstractmethod

# CLASE ABSTRACTA CLIENTE

class Cliente(ABC):

    def __init__(self, id_cliente, nombre):
        self.__id_cliente = id_cliente
        self.__nombre = nombre

    # Getter
    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def nombre(self):
        return self.__nombre

    # Metodo abstracto
    @abstractmethod
    def calcularDescuento(self, subtotal):
        pass

    def mostrarInformacion(self):
        print(f"ID Cliente: {self.__id_cliente}")
        print(f"Nombre: {self.__nombre}")

# CLIENTE MAYORISTA

class ClienteMayorista(Cliente):

    def __init__(self, id_cliente, nombre, empresa):
        super().__init__(id_cliente, nombre)
        self.__empresa = empresa

    @property
    def empresa(self):
        return self.__empresa

    # Sobrescritura del metodo
    def calcularDescuento(self, subtotal):
        # Cliente mayorista recibe 15% de descuento
        descuento = subtotal * 0.15
        return descuento

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Empresa: {self.__empresa}")
        print("Tipo de cliente: Mayorista")

# CLIENTE MINORISTA

class ClienteMinorista(Cliente):

    def __init__(self, id_cliente, nombre):
        super().__init__(id_cliente, nombre)

    # Sobrescritura del metodo
    def calcularDescuento(self, subtotal):
        # Cliente minorista recibe 5% de descuento
        descuento = subtotal * 0.05
        return descuento

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print("Tipo de cliente: Minorista")

# PRODUCTO

class Producto:

    def __init__(self, codigo, nombre, precio, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def reducirStock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio:.2f}"

# DETALLE DE VENTA

class DetalleVenta:

    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad

    def calcularSubtotal(self):
        return self.__producto.precio * self.__cantidad

    def mostrarDetalle(self):
        subtotal = self.calcularSubtotal()
        print(
            f"{self.__producto.nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Precio: ${self.__producto.precio:.2f} | "
            f"Subtotal: ${subtotal:.2f}"
        )

# VENTA

class Venta:

    def __init__(self, cliente):
        self.__cliente = cliente
        self.__detalles = []

    def agregarDetalle(self, detalle):
        self.__detalles.append(detalle)

    def calcularSubtotal(self):
        subtotal = 0

        for detalle in self.__detalles:
            subtotal += detalle.calcularSubtotal()

        return subtotal

    def calcularDescuento(self):
        subtotal = self.calcularSubtotal()

        # POLIMORFISMO

        return self.__cliente.calcularDescuento(subtotal)

    def calcularTotal(self):
        subtotal = self.calcularSubtotal()
        descuento = self.calcularDescuento()

        return subtotal - descuento

    def mostrarFactura(self):
        print("\n==========================================")
        print("           TIENDA DE ABASTOS")
        print("==========================================")

        self.__cliente.mostrarInformacion()

        print("\n-------------- PRODUCTOS -----------------")

        for detalle in self.__detalles:
            detalle.mostrarDetalle()

        subtotal = self.calcularSubtotal()
        descuento = self.calcularDescuento()
        total = self.calcularTotal()

        print("------------------------------------------")
        print(f"Subtotal:   ${subtotal:.2f}")
        print(f"Descuento:  ${descuento:.2f}")
        print(f"TOTAL:      ${total:.2f}")
        print("==========================================")

# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    # Crear productos de la tienda de abastos
    arroz = Producto("P001", "Arroz", 1.50, 50)
    aceite = Producto("P002", "Aceite", 3.50, 30)
    azucar = Producto("P003", "Azúcar", 1.25, 40)

    # CASO 1: CLIENTE MAYORISTA

    cliente_mayorista = ClienteMayorista(
        "C001",
        "Daniel Perez",
        "Distribuidora Perez"
    )

    venta_mayorista = Venta(cliente_mayorista)

    venta_mayorista.agregarDetalle(
        DetalleVenta(arroz, 10)
    )

    venta_mayorista.agregarDetalle(
        DetalleVenta(aceite, 5)
    )

    venta_mayorista.agregarDetalle(
        DetalleVenta(azucar, 10)
    )

    print("\n\n******** CASO 1 ********")
    venta_mayorista.mostrarFactura()

    # CASO 2: CLIENTE MINORISTA

    cliente_minorista = ClienteMinorista(
        "C002",
        "Maria cedeño"
    )

    venta_minorista = Venta(cliente_minorista)

    venta_minorista.agregarDetalle(
        DetalleVenta(arroz, 2)
    )

    venta_minorista.agregarDetalle(
        DetalleVenta(aceite, 1)
    )

    venta_minorista.agregarDetalle(
        DetalleVenta(azucar, 2)
    )

    print("\n\n******** CASO 2 ********")
    venta_minorista.mostrarFactura()

    # DEMOSTRACIÓN DIRECTA DE POLIMORFISMO

    print("\n\n******** DEMOSTRACION DE POLIMORFISMO ********")

    clientes = [
        ClienteMayorista("C003", "Pedro Castro", "Comercial Castro"),
        ClienteMinorista("C004", "Ana Mendoza")
    ]

    subtotal = 100

    for cliente in clientes:

        descuento = cliente.calcularDescuento(subtotal)

        print(
            f"{cliente.nombre} | "
            f"Tipo: {cliente.__class__.__name__} | "
            f"Subtotal: ${subtotal:.2f} | "
            f"Descuento: ${descuento:.2f} | "
            f"Total: ${subtotal - descuento:.2f}"
        )
