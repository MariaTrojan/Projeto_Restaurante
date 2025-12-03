from .Pessoa import Pessoa
from abc import ABC, abstractmethod

class Funcionarios(Pessoa, ABC):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("Salário não pode ser negativo")
        self._salario = valor


    @abstractmethod
    def calcula_salario(self):
        pass


    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário: R$ {self.salario:.2f}")
        