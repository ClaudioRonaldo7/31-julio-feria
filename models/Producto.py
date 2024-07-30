from config.db import connectToMySQL

class productos7:
    def __init__(self, data):
        self.idproducto = data["idproducto"]
        self.nombre = data["nombre"]
        self.precio = data["precio"]
        self.categoria = data["categoria"]
        self.imagen = data["imagen"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Producto;"
        results = connectToMySQL('only_football').query_db(query)
        productos = []
        for result in results:
            productos.append(cls(result))
        return productos

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM Producto WHERE nombre LIKE '%{search_term}%';"
        results = connectToMySQL('only_football').query_db(query)
        productos = []
        for result in results:
            productos.append(cls(result))
        return productos

    @classmethod
    def get_producto(cls, id):
        query = "SELECT * FROM Producto WHERE id = " + id + ";"
        results = connectToMySQL('only_football').query_db(query)
        productos = []
        for result in results:
            productos.append(cls(result))
        return productos