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
