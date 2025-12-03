# Projeto_Restaurante

# Tema e Objetivo do projeto
  O tema do projeto é um sistema simples para gerenciar pedidos de um restaurante. Ele permite cadastrar clientes, criar itens do cardápio (pratos, bebidas e sobremesas) e montar pedidos de forma organizada.
  O objetivo é oferecer um sistema prático e fácil de usar, que melhore o atendimento e ajude os funcionários a manterem o controle das informações do restaurante de maneira mais eficiente.

# Descrição de cada classe

# 1. Pessoa.py
# Descrição: 
Classe-base que representa qualquer pessoa do sistema (possui nome, CPF etc.).
# Pilares: 
Abstração: representa uma pessoa de forma genérica.

Herança: outras classes (Cliente, Funcionário, Garçom) herdam dela.

# 2. Cliente.py
# Descrição:
Representa o cliente do restaurante. Possui informações específicas (ex.: mesa).
# Pilares:
Herança: herda de Pessoa.

Polimorfismo: adiciona atributos e comportamentos próprios de um cliente.

# 3. Funcionarios.py
# Descrição:
Classe que representa funcionários gerais do restaurante.
# Pilares:
Herança: herda de Pessoa.

Polimorfismo: pode ter métodos sobrescritos por subclasses (como Garçom).

# 4. Garcom.py
# Descrição:
Classe que representa os garçons.
# Pilares:
Herança: herda de Funcionarios.

Polimorfismo: pode implementar ações específicas, como registrar pedidos.

# 5. ItemCardapio.py
# Descrição:
Classe-base para itens do cardápio. Define nome e preço.
# Pilares:
Abstração: é um item genérico.

Herança: Prato, Bebida e Sobremesa herdam dessa classe.

# 6. Prato.py
# Descrição:
Representa um prato do cardápio (ex.: lasanha, pizza).
# Pilares:
Herança: herda de ItemCardapio.

Polimorfismo: sobrescreve métodos como calcular_preco().

# 7. Bebida.py
# Descrição:
Representa uma bebida (ex.: refrigerante, suco).
# Pilares:

Herança: herda de ItemCardapio.

Polimorfismo: sobrescreve métodos como calcular_preco().

# 8. Sobremesa.py
# Descrição:
Representa sobremesas (ex.: pudim, sorvete).
# Pilares:

Herança: herda de ItemCardapio.

Polimorfismo: sobrescreve métodos como calcular_preco().

# 9. ItemFactory.py
# Descrição:
Classe responsável por criar itens do cardápio usando o padrão Factory + Singleton.
# Pilares:

Encapsulamento: controla a criação dos objetos.

Polimorfismo: cria diferentes tipos de itens usando o mesmo método.

Padrões de projeto: Factory e Singleton.

# 10. Pedido.py
# Descrição:
Representa um pedido do cliente. Armazena itens, cliente, valor total e status.
# Pilares:

Encapsulamento: manipula itens internamente (adicionar/remover).

Associação: se relaciona com Cliente, Itens e Status.

# 11. StatusPedido.py
# Descrição:
Enum ou classe com os possíveis status do pedido (ex.: Em preparo, Finalizado).
# Pilares:

Abstração: simplifica o controle do estado do pedido.

# 12. teste.py / teste_Factory.py
# Descrição:
Arquivos usados apenas para testar o funcionamento das classes.


# Explicação dos padrões de projeto

# FACTORY
No sistema, a classe ItemFactory é responsável por criar os itens do cardápio:

Prato

Bebida

Sobremesa

Em vez de criar diretamente:
```python
prato = Prato("Lasanha", 32.50)
````
O sistema usa:
```python
prato = factory.criar_item("prato", nome="Lasanha", preco=32.50)
````
# SINGLETON
A classe ItemFactory também implementa Singleton:
```python
factory = ItemFactory()
f2 = ItemFactory()
print(f1 is f2)  # True
````

# Isso significa que:

- Não importa quantas vezes o sistema chame ItemFactory()

- Sempre será retornada a mesma instância

# Por que isso é útil aqui?

- Garante que todos os itens são criados pelo mesmo mecanismo

- Evita múltiplas fábricas conflitantes

- Ajuda a manter o sistema organizado e consistente

- Simplifica testes e manutenção

# TESTES
# Cadastro e exibição de um cliente
```python
cliente1 = Cliente("   maria silva  ", "123.456.789-99")
lista_testes.append(cliente1)
print(cliente1.exibir_dados())
````

# Cadastro e exibição de um garçom
```python
garcom1 = Garcom("  joão almeida  ", "097.456.764-98", 2500)
lista_testes.append(garcom1)
print(garcom1.exibir_dados())
````

# Criação dos itens do cardápio usando a ItemFactory
```python
prato1 = factory.criar_item(tipo_item="prato", nome="lasanha", preco=32.50)
bebida1 = factory.criar_item(tipo_item="bebida", nome="coca-cola", preco=8.00)
sobremesa1 = factory.criar_item(tipo_item="sobremesa", nome="pudim", preco=12.00)
````

# Teste do Singleton
```python
f1 = ItemFactory()
f2 = ItemFactory()
print(f1 is f2)
````

# Criação de um pedido
```python
pedido1 = Pedido(cliente1)
pedido1.adicionar_item(prato1)
pedido1.adicionar_item(bebida1)
pedido1.adicionar_item(sobremesa1)
````

# Mudança de status do pedido
```python
pedido1.status = StatusPedido.EM_PREPARO
````

# Exibição completa do pedido
```python
pedido1.exibir_dados()
````


# SAÍDA
```text
---- CLIENTE ----
Nome:    maria silva
CPF: 123.456.789-99

---- GARÇOM ----
=== Dados do Garçom ===
Nome:   joão almeida
CPF: 097.456.764-98
Salário: R$ 2500.00

---- ITENS DO CARDÁPIO ----
Prato:   lasanha bolonhesa  | Preço: R$32.50
Bebida:  coca-cola lata  | Preço: R$8.00
Sobremesa:  pudim tradicional  | Preço: R$12.00
True

 ---- PEDIDO ----
Cliente:    maria silva
CPF: 123.456.789-99
Itens do pedido:
-   lasanha bolonhesa  | R$ 32.50
-  coca-cola lata  | R$ 8.00
-  pudim tradicional  | R$ 12.00
Total: R$ 52.50
Status: Em preparo
````

# Teste Factory com Singleton
Este teste demonstra como funciona a criação de itens do cardápio utilizando o padrão de projeto Factory combinado com Singleton.

Pegando a instância única da fábrica (Singleton)
```python
factory = ItemFactory()
```
O ItemFactory foi implementado com Singleton, então:

- Mesmo que você chame ItemFactory() várias vezes, sempre receberá a mesma instância.

- Isso garante que a criação de itens do cardápio seja centralizada.
