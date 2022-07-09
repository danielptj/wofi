class Pedido:
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def funcionario_id(self):
        return self._funcionario_id

    @funcionario_id.setter
    def funcionario_id(self, funcionario_id):
        self._funcionario_id = funcionario_id
    
    @property
    def cliente_id(self):
        return self._cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self._cliente_id = cliente_id
