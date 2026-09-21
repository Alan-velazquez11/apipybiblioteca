class Editorial:
    def __init__(self, idEd: int, nombre: str, pais: str):
        self._idEd = idEd
        self._nombre = nombre
        self._pais = pais

    def get_idEd(self) -> int: return self._idEd
    def get_nombre(self) -> str: return self._nombre
    def get_pais(self) -> str: return self._pais

    def set_idEd(self, idEd: int): self._idEd = idEd
    def set_nombre(self, nombre: str): self._nombre = nombre
    def set_pais(self, pais: str): self._pais = pais

    def to_dict(self) -> dict:
        return {"idEd": self._idEd, "nombre": self._nombre, "pais": self._pais}


class Libro:
    def __init__(self, ISBN: str, titulo: str, autor: str, precio: float):
        self._ISBN = ISBN
        self._titulo = titulo
        self._autor = autor
        self._precio = precio

    def get_ISBN(self) -> str: return self._ISBN
    def get_titulo(self) -> str: return self._titulo
    def get_autor(self) -> str: return self._autor
    def get_precio(self) -> float: return self._precio

    def set_ISBN(self, ISBN: str): self._ISBN = ISBN
    def set_titulo(self, titulo: str): self._titulo = titulo
    def set_autor(self, autor: str): self._autor = autor
    def set_precio(self, precio: float): self._precio = precio

    def to_dict(self) -> dict:
        return {"ISBN": self._ISBN, "titulo": self._titulo, "autor": self._autor, "precio": self._precio}