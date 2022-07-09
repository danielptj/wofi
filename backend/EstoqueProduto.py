class EstoqueProduto:
    
    @property
    def estoque_id(self):
        return self._estoque_id

    @estoque_id.setter
    def estoque_id(self, estoque_id):
        self._estoque_id = estoque_id

    @property
    def produto_id(self):
        return self._produto_id

    @produto_id.setter
    def produto_id(self, produto_id):
        self._produto_id = produto_id

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade