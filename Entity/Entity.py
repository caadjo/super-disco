class Entity:
    def __init__(self):
        self._id = None

    def get_id(self):
        return self._id

    def set_id(self, id_value):
        self._id = id_value
