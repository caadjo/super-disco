# pesquisa.py
from Entity import Entity


class Pesquisa(Entity):
    def __init__(self, nome=None):
        super().__init__()  # Chama o construtor da classe Entity
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f"Pesquisa{{nome={self._nome}}}"
