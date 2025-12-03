from enum import Enum

class StatusPedido(Enum):
    EM_ABERTO = "Em aberto"
    EM_PREPARO = "Em preparo"
    PRONTO = "Pronto"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"