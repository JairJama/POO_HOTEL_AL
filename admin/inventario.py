class Inventario:
    def __init__(self, productoID, nombreProducto, cantidadDisponible, categoria, proveedor):
        self._productoID = productoID
        self._nombreProducto = nombreProducto
        self._cantidadDisponible = cantidadDisponible
        self._categoria = categoria
        self._proveedor = proveedor
        self.listaProductos = [
            {"productoID": 1, "nombreProducto": "Toalla", "cantidadDisponible": 100, "categoria": "Baño", "proveedor": "TextilesHotel"},
            {"productoID": 2, "nombreProducto": "Almohada", "cantidadDisponible": 50, "categoria": "Habitación", "proveedor": "SueñosFelices"},
            {"productoID": 3, "nombreProducto": "Jabón", "cantidadDisponible": 200, "categoria": "Amenidades", "proveedor": "LimpiezaTotal"},
            {"productoID": 4, "nombreProducto": "Secador de pelo", "cantidadDisponible": 30, "categoria": "Electrónica", "proveedor": "ElectroHotel"},
            {"productoID": 5, "nombreProducto": "Minibar", "cantidadDisponible": 20, "categoria": "Alimentación", "proveedor": "BebidasFrescas"}
        ]
        self.reservas = []  # Agregación con Reservas
        self.eventos = []   # Agregación con Eventos
    #Getters

    def get_productoID(self):
        return self._productoID
    
    def get_nombreProducto(self):
        return self._nombreProducto
    
    def get_cantidadDisponible(self):
        return self._cantidadDisponible
    
    def get_categoria(self):
        return self._categoria
    
    def get_proveedor(self):
        return  self._proveedor

    #Setters
    
    def set_productoID(self, productoID):
        self._productoID = productoID
    
    def set_nombreProducto(self,nombreProducto):
        self._nombreProducto = nombreProducto
    
    def set_cantidadDisponible(self,cantidadDisponible):
        self._cantidadDisponible = cantidadDisponible
    
    def set_categoria(self,categoria):
        self._categoria = categoria
    
    def set_proveedor(self, proveedor):
        self._proveedor = proveedor

    def agregarProducto(self, productoID, nombreProducto, cantidadDisponible, categoria, proveedor):

        print(f"El producto agregado es {productoID}:{nombreProducto}, la cantidad es {cantidadDisponible}")
        self.listaProductos.append({
            "productoID": productoID,
            "nombreProducto": nombreProducto,
            "cantidadDisponible": cantidadDisponible,
            "categoria": categoria,
            "proveedor": proveedor
        })

    # Otros métodos quedan igual


    def actualizarStock(self, numero):
        print(f"El producto {self.productoID}:{self.nombreProducto} ha sido actualizado con la cantidad de {numero}")
        for producto in self.listaProductos:
            if producto["productoID"] == self.productoID:
                producto["cantidadDisponible"] = numero
                break

    def eliminarProducto(self):
        print(f"El producto eliminado es {self.productoID}:{self.nombreProducto}")
        self.listaProductos = [producto for producto in self.listaProductos if producto["productoID"] != self.productoID]

    def mostrar_inventario(self):
        if not self.listaProductos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for producto in self.listaProductos:
                print(f"ID: {producto['productoID']}, Producto: {producto['nombreProducto']}, Cantidad: {producto['cantidadDisponible']}, Categoría: {producto['categoria']}, Proveedor: {producto['proveedor']}")
