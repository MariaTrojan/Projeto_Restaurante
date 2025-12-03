from .Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

        