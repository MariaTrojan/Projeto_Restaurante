from .Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, historico = "Sem histórico" ):
        super().__init__(nome, cpf)
        self.historico = historico


    @property
    def historico(self):
        return self.__historico
    
    @historico.setter
    def historico(self, historico):
        self.__historico = historico.title()
    
    def adicionar_pedido(self, pedido):
        self.__historico.append(pedido)


    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print("Histórico de pedidos:")

        if not self.__historico:
            print("  (Nenhum pedido realizado ainda)")
        else:
            for p in self.__historico:
                print(f"  - {p}")
        