from client import Client

class Pedido:
    def __init__(self, preco_total, status, cliente: Client):
        self._preco_total = preco_total
        self._status = status
        self.cliente = cliente

