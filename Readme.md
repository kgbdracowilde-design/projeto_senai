# Visão Geral do Projeto 
# O objetivo deste projeto é desenvolver um sistema simples em linhas de comando (CLI) para gerenciar o cadastro, leitura, atualização e exclusão (CRUD) de [itens]. O sistema deve permitir que o usuário mantenha um controle atualizado do seu catalogo de forma interativa e intuitiva.

# estrutura de dados ( o que vamos guardar)

cada [item] gerenciado pelo sistema deve conter obrigatoriamente as seguintes informações:
nome: Verificar o nome do paciente.
Tipo de exame: Exame a ser realizado ex: Raios x de Torax.
Valor do exame: Preço de cada exame em Reais ou Dolar.
Data do exame: Registro do dia do exame realizado.
Hora do exame: Horario do exame realizado
Resultado do exame: Diagnostico identificado pelo médico ex: Pneumotorax: é o acúmulo de ar entre as duas camadas da parede torácica pulmonar.
valor: um numero (inteiro ou decimal) que representa o preço unitario do produto.

# Requisitos Funcionais (o que o sistema FAZ)

- São ações que o usuário pode executar dentro do programa.
1. RF01 - Cadastrar: O sistema deve permitir a inserção de um novo [item] informando seu nome e valor númerico.

2. RF02 - Listar: O sistema deve exibir todos os [itens] cadastrados, mostrando su ID (posição na lista), nome e valor.

3. RF03 - Editar: O sistema deve permitir que o usuário altere o valor númerico de [item] especifico atraves do seu ID.

4. RF04 - Excluir: O sistema deve permitir a remoção definitiva de um [item] atraves do seu ID.

5. RF05 - Menu interativo: O sistema deve exibir um menu de opções e rodar continuamente até que o usuário escolha a opção "SAIR".

# Requisitos Não Funcionais (Como o sistema É)
- RNF01 - Interface: A interação com o usuário será inteiramente via Terminal (linha de
comando).
- RNF02 - Armazenamento: Os dados serão salvos temporariamente na memória RAM
usando Listas e Dicionários do Python (não haverá banco de dados nesta versão).
# Regras de Negócio (Restrições)
Condições que o código PRECISA respeitar para não quebrar ou gerar dados inválidos.

- RN01: Ao tentar editar ou excluir um [item], o sistema deve verificar se o ID digitado
realmente existe na lista. Se não existir, deve exibir uma mensagem de erro (&quot;Item não
encontrado&quot;).
- RN02: Todo novo [item] cadastrado deve entrar no sistema com o Status padrão como
&quot;Verdadeira&quot; (Ex: Ativo)
