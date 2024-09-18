# residencia.py
from Container import Containers


class Residencia(Containers):
    def __init__(self, id_container=None, nome=None, banheiro=None, sigla=None, cama=False):
        super().__init__(id_value=id_container)
        self._id_container = id_container
        self._nome = nome
        self._banheiro = banheiro
        self._sigla = sigla
        self._cama = cama

    def get_id_container(self):
        return self._id_container

    def set_id_container(self, id_container):
        self._id_container = id_container

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_banheiro(self):
        return self._banheiro

    def set_banheiro(self, banheiro):
        self._banheiro = banheiro

    def get_sigla(self):
        return self._sigla

    def set_sigla(self, sigla):
        self._sigla = sigla

    def is_cama(self):
        return self._cama

    def set_cama(self, cama):
        self._cama = cama

    def __str__(self):
        return (f"Residencia{{ID_container={self._id_container}, nome={self._nome}, "
                f"banheiro={self._banheiro}, Sigla={self._sigla}, cama={self._cama}}}")
