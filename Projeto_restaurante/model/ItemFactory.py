from model.Prato import Prato
from model.Bebida import Bebida
from model.Sobremesa import Sobremesa

#SIGLETON
class ItemFactory:
    _instance = None  # Armazena a única instância da classe

    def __new__(cls):
        # Verifica se ainda não existe uma instância da classe
        # _instance é um atributo estático da classe, começa como None
        if cls._instance is None:
            # Cria a instância usando o método __new__ da classe pai (object)
            cls._instance = super(ItemFactory, cls).__new__(cls)
        # Retorna a única instância existente
        return cls._instance

    
    def criar_item(self, tipo_item: str, **args):

        if tipo_item == "prato":
            return Prato(
                nome=args.get("nome"),
                preco=args.get("preco")
            )

        elif tipo_item == "bebida":
            return Bebida(
                nome=args.get("nome"),
                preco=args.get("preco")
            )

        elif tipo_item == "sobremesa":
            return Sobremesa(
                nome=args.get("nome"),
                preco=args.get("preco")
            )

        else:

            raise ValueError(f"Tipo '{tipo_item}' não reconhecido.")
