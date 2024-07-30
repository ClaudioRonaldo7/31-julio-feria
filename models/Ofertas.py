from config.db import connectToMySQL

class ofertas:
    def __init__(self, data):
        self.idofertas = data["idofertas"]
        self.nombre = data["nombre"]
        self.precio = data["precio"]
        self.precio_descuento = data["precio_descuento"]
        self.imagen = data["imagen"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Ofertas;"
        results = connectToMySQL('only_football').query_db(query)
        ofertas = []
        for result in results:
            ofertas.append(cls(result))
        return ofertas

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM ofertas WHERE nombre LIKE '%{search_term}%';"
        results = connectToMySQL('only_football').query_db(query)
        ofertas = []
        for result in results:
            ofertas.append(cls(result))
        return ofertas

    @classmethod
    def get_oferta(cls, id):
        query = "SELECT * FROM ofertas WHERE id = " + id + ";"
        results = connectToMySQL('only_football').query_db(query)
        ofertas = []
        for result in results:
            ofertas.append(cls(result))
        return ofertas