from model.ItemFactory import ItemFactory
from model.Prato import Prato
from model.Bebida import Bebida
from model.Sobremesa import Sobremesa

factory = ItemFactory()  # Pega a instância única (Singleton)

item1 = factory.criar_item(tipo_item="prato",
                           nome="Lasanha",
                           preco=32.50)

item2 = factory.criar_item(tipo_item="bebida",
                           nome="Coca-Cola",
                           preco=8.00)

item3 = factory.criar_item(tipo_item="sobremesa",
                           nome="Pudim",
                           preco=12.00)

print(item1.exibir_dados())
print(item2.exibir_dados())
print(item3.exibir_dados())
