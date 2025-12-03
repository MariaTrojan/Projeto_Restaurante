from model.Cliente import Cliente
from model.Garcom import Garcom
from model.ItemFactory import ItemFactory
from model.Pedido import Pedido
from model.StatusPedido import StatusPedido

# Pegando a instância única da fábrica
factory = ItemFactory()

# Lista geral só como no outro projeto
lista_testes = []


# ======== CLIENTE ========
cliente1 = Cliente("   maria silva  ", "123.456.789-99")
lista_testes.append(cliente1)

print("\n---- CLIENTE ----")
cliente1.exibir_dados()


# ======== FUNCIONÁRIO ========
garcom1 = Garcom("  joão almeida  ", "097.456.764-98", 2500)
lista_testes.append(garcom1)

print("\n---- GARÇOM ----")
garcom1.exibir_dados()


# ======== ITENS VIA FACTORY ========
print("\n---- ITENS DO CARDÁPIO ----")

prato1 = factory.criar_item(
    tipo_item="prato",
    nome="  lasanha bolonhesa ",
    preco=32.50
)

bebida1 = factory.criar_item(
    tipo_item="bebida",
    nome=" coca-cola lata ",
    preco=8.00
)

sobremesa1 = factory.criar_item(
    tipo_item="sobremesa",
    nome=" pudim tradicional ",
    preco=12.00
)

lista_testes.extend([prato1, bebida1, sobremesa1])

print(prato1.exibir_dados())
print(bebida1.exibir_dados())
print(sobremesa1.exibir_dados())

f1 = ItemFactory()
f2 = ItemFactory()
print(f1 is f2)

# ======== PEDIDO ========
print("\n ---- PEDIDO ---- ")

pedido1 = Pedido(cliente1)
pedido1.adicionar_item(prato1)
pedido1.adicionar_item(bebida1)
pedido1.adicionar_item(sobremesa1)

pedido1.status = StatusPedido.EM_PREPARO

lista_testes.append(pedido1)

pedido1.exibir_dados()

