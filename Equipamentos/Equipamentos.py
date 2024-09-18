# equipamentos.py
from Entity import Entity


class Equipamentos(Entity):
    def __init__(self, id_pesquisa=None, utilidade=None, quantideenergia=0.0, nome=None):
        super().__init__()  # Chama o construtor da classe base Entity
        self._id_pesquisa = id_pesquisa
        self._utilidade = utilidade
        self._quantideenergia = quantideenergia
        self._nome = nome

    def get_id_pesquisa(self):
        return self._id_pesquisa

    def set_id_pesquisa(self, id_pesquisa):
        self._id_pesquisa = id_pesquisa

    def get_utilidade(self):
        return self._utilidade

    def set_utilidade(self, utilidade):
        self._utilidade = utilidade

    def get_quantideenergia(self):
        return self._quantideenergia

    def set_quantideenergia(self, quantideenergia):
        self._quantideenergia = quantideenergia

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def __str__(self):
        return (f"Equipamentos{{id_pesquisa={self._id_pesquisa}, utilidade={self._utilidade}, "
                f"quantideenergia={self._quantideenergia}, nome={self._nome}}}")
