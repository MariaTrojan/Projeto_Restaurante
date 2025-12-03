from model.Prato import Prato
from model.Bebida import Bebida
from model.Sobremesa import Sobremesa

#SIGLETON
class ItemFactory:
    _instance = None  # Armazena a única instância da classe

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ItemFactory, cls).__new__(cls)
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