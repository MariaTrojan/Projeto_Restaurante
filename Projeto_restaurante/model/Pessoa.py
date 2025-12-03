from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
       
         
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()
    

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf.title()


    @abstractmethod
    def exibir_dados(self):
        pass