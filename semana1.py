class Producto:
    def __init__(self, nombre, precio, stock):
        # Atributos privados
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getter del nombre
    def get_nombre(self):
        return self.__nombre

    # Setter del nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter del precio
    def get_precio(self):
        return self.__precio

    # Setter del precio
    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    # Getter del stock
    def get_stock(self):
        return self.__stock

    # Setter del stock
    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("El stock no puede ser negativo.")

    # Método para mostrar información
    def mostrar_producto(self):
        print("Producto:", self.__nombre)
        print("Precio: $", self.__precio)
        print("Stock:", self.__stock)


class Cliente:
    def __init__(self, nombre, cedula):
        # Atributos privados
        self.__nombre = nombre
        self.__cedula = cedula

    # Getter del nombre
    def get_nombre(self):
        return self.__nombre

    # Setter del nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter de la cédula
    def get_cedula(self):
        return self.__cedula

    # Setter de la cédula
    def set_cedula(self, cedula):
        self.__cedula = cedula

    # Método para mostrar información
    def mostrar_cliente(self):
        print("Nombre:", self.__nombre)
        print("Cédula:", self.__cedula)


# ============================
# PROGRAMA PRINCIPAL
# ============================

print("================================")
print("     TIENDA DE ABASTOS")
print("       SEMANA 1 - POO")
print("================================")

# Crear objetos de la clase Producto
arroz = Producto("Arroz", 1.50, 20)
leche = Producto("Leche", 1.10, 15)

print("\n--- PRODUCTO 1 ---")
arroz.mostrar_producto()

print("\n--- PRODUCTO 2 ---")
leche.mostrar_producto()

# Utilizar getters
print("\nNombre del producto:", arroz.get_nombre())
print("Precio del producto:", arroz.get_precio())

# Utilizar setters
arroz.set_precio(1.60)
arroz.set_stock(25)

print("\nDespués de modificar los datos:")
arroz.mostrar_producto()

# Crear objeto Cliente
cliente = Cliente("Juan Pérez", "0102030405")

print("\n--- CLIENTE ---")
cliente.mostrar_cliente()