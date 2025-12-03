from .StatusPedido import StatusPedido

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente          
        self.itens = []                 
        self.valor_total = 0.0
        self.status = StatusPedido.EM_ABERTO


    def adicionar_item(self, item):
        self.itens.append(item)
        self.calcular_total()

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            self.calcular_total()

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.preco
        self.valor_total = total
        return total

    def exibir_dados(self):
        print(f"Cliente: {self.cliente.nome}")
        print(f"CPF: {self.cliente.cpf}")
        print("Itens do pedido:")
        
        for item in self.itens:
            print(f"- {item.nome} | R$ {item.preco:.2f}")
        
        print(f"Total: R$ {self.valor_total:.2f}")
        print(f"Status: {self.status.value}")