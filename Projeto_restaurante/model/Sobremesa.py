from .ItemCardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_preco(self):
        return self.preco
    
    def exibir_dados(self):
        return f"Sobremesa: {self.nome} | Preço: R${self.preco:.2f}"