"""
Desarrollar un sistema básico de inventario con POO en Python para gestionar productos y realizar operaciones de inventario.

1. Crear una clase Producto con atributos para nombre, precio y cantidad
2. Implementar métodos para añadir, actualizar y mostrar información de productos
3. Desarrollar una clase Inventario que gestione una colección de productos
4. Implementar operaciones de inventario: añadir producto, buscar por nombre y calcular valor total
5. Manejar excepciones para entradas inválidas (cantidades negativas, nombres vacíos, etc.)
6. Crear un menú interactivo simple para probar las funcionalidades
7. Mostrar resultados de operaciones por consola de manera formateada
8.Validar que los datos ingresados sean del tipo correcto

"""


class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto: Producto):
        if producto.nombre in self.productos:
            raise ValueError("El producto ya existe en el inventario.")
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre: str):
        return self.productos.get(nombre, None)

    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos.values())
    
    def listar_productos(self):
        return list(self.productos.values())

    def mostrar_inventario(self):
        if not self.productos:
            return "El inventario está vacío."
        return "\n".join(producto.__str__() for producto in self.productos.values())



def menu_principal():
    inventario = Inventario()
    
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Buscar producto por nombre")
        print("3. Calcular valor total del inventario")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.añadir_producto(producto)
                print("Producto añadido exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto.__str__())
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            valor_total = inventario.calcular_valor_inventario()
            print(f"Valor total del inventario: ${valor_total:.2f}")

        elif opcion == "4":
            print(inventario.mostrar_inventario())

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu_principal()