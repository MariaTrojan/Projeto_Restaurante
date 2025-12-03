from .Funcionarios import Funcionarios

class Garcom(Funcionarios):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def calcula_salario(self):
        return self.salario
    
    def exibir_dados(self):
        print("=== Dados do Garçom ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário: R$ {self.calcula_salario():.2f}")
        