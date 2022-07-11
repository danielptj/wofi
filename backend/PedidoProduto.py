class PedidoProduto:
    
    @property
    def pedido_id(self):
        return self._pedido_id

    @pedido_id.setter
    def pedido_id(self, pedido_id):
        self._pedido_id = pedido_id

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