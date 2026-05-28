lista de itens = [nome, tipo de exame, data do exame, valor do exame, resultado do exame]

while True:
    print("Bem-vindo ao sistema de gerenciamento de exames laboratoriais!")
    print("1. Cadastro de exames")
    print("2. Consulta de exames")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    match int(opcao):

        case "1":
            nome = input("Digite o nome do paciente: ")
            tipo_de_exame = input("Digite o tipo de exame: ")
            valor_do_exame = input("Digite o valor do exame: ")
            data_do_exame = input("Digite a data: dia/mes/ano")
            hora do exame = input("Digite a hora do exame: 00:00 am/pm")
            resultado_do_exame = input("Digite o resultado do exame: ")

            novo_item = {
             "nome": nome,
             "tipo_de_exame": tipo_de_exame,
             "valor_do_exame": valor_do_exame,
             "data_do_exame": data_do_exame,
             "hora_do_exame": hora_do_exame,
             "resultado_do_exame": resultado_do_exame
            }
            lista_itens.append(novo_item)
            print("Item cadastrado com sucesso")

        case 2:
            for item in lista_itens: # o que será mostrado na tela para o usuário

                print(f"Nome: {item["nome"]}")
                print(f"Exame: {item["tipo_de_exame"]}")
                print(f"Valor: {item["valor_do_exame"]}")
                print(f"Data: {item["data_do_exame"]}")
                print(f"Hora; {item["hora_do_exame"]}")
                print(f"Resultado: {item["resultado_do_exame"]}")
