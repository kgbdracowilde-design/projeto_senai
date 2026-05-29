dev = True
if dev ==True:
    item1 = {
        "nome": "Ana",
        "tipo_de_exame": RxTorácia,
        "valor_do_exame": "R$50",
        "data_do_exame": "01/04/24",
        "hora_do_exame": "14:00hs",
        "resultado_do_exame": "Pneumotórax"
    }
else:
    lista_de_itens = []

while True:
    print("Bem-vindo ao sistema de gerenciamento de exames laboratoriais!")
    print("==============================================================")
    print("1. Cadastro de exames")
    print("2. Consulta de exames")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    match int(opcao):

        case "1":
            nome = input("Digite o nome do paciente: ")
            tipo_de_exame = input("Digite o tipo de exame: ")
            valor_do_exame = input("Digite o valor do exame: ")
            data_do_exame = input("Digite a data: ")
            hora_do_exame = input("Digite a hora do exame: ")
            resultado_do_exame = input("Digite o resultado do exame: ")

            novo_item = {
                "nome": nome,
                "tipo_de_exame": tipo_de_exame,
                "valor_do_exame": valor_do_exame,
                "data_do_exame": data_do_exame,
                "hora_do_exame": hora_do_exame,
                "resultado_do_exame": resultado_do_exame
            }
            lista_de_itens.append(novo_item)
            print("Item cadastrado com sucesso")

        case 2:
            print("-" * 20)
            for item in lista_de_itens: # o que será mostrado na tela para o usuário
                print("=" * 20)
                print(f"Nome: {item['nome']}")
                print(f"Exame: {item['tipo_de_exame']}")
                print(f"Valor: {item['valor_do_exame']}")
                print(f"Data: {item['data_do_exame']}")
                print(f"Hora; {item['hora_do_exame']}")
                print(f"Resultado: {item['resultado_do_exame']}")
                print("=" * 20) 
