
from Entity import Entity


class Containers(Entity):
    def __init__(self, id_value=None, tamanho=0.0):
        super().__init__()
        self._id = id_value
        self._tamanho = tamanho

    def get_id(self):
        return self._id

    def set_id(self, id_value):
        self._id = id_value

    def get_tamanho(self):
        return self._tamanho

    def set_tamanho(self, tamanho):
        self._tamanho = tamanho

    def __str__(self):
        return f"Containers{{ID={self._id}, Tamanho={self._tamanho}}}"
