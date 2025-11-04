pacientes = []

def clinicavida():
    opcao = 0
    while opcao != 5:
        print('\n=== SISTEMA CLÍNICA VIDA+ ===\n')

        print('1. Cadastrar paciente')
        print('2. Ver estatísticas')
        print('3. Buscar paciente')
        print('4. Listar todos pacientes')
        print('5. Sair')

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Opção inválida, digite apenas números.')
            continue

        match opcao:
            case 1:
                cadastro()
            case 2:
                dados()
            case 3:
                buscar_paciente()
            case 4:
                listar_paciente()
            case 5:
                print('Saindo do sistema...')
            case _:
                print('Opção inválida, tente novamente.')

def cadastro():
    print('\n=== CADASTRAR PACIENTE ===\n')

    while True:
        nome = input('Nome do paciente: ').strip()
        if nome.replace(' ', '').isalpha():
            nome = nome.title()
            break
        print('Nome inválido! Digite apenas letras.\n')

    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Idade inválida! Digite um número.\n')

    while True:
        try:
            telefone = int(input('Telefone: '))
            break
        except ValueError:
            print('Telefone inválido! Digite apenas números.\n')

    paciente = {
        'Nome': nome,
        'Idade': idade,
        'Telefone': telefone
    }
    pacientes.append(paciente)
    print('\nPaciente cadastrado com sucesso!\n')

def listar_paciente():
    if pacientes:
        print('\n=== LISTA DE PACIENTES ===\n')
        pacientes_ordem = sorted(pacientes, key=lambda p: p['Nome'].lower())
        for i, paciente in enumerate(pacientes_ordem, start=1):
            print('{}. {}'.format(i, paciente['Nome']))

    else: print('\nNenhum paciente cadastrado ainda.\n')

def buscar_paciente():
    print('\n=== BUSCAR PACIENTE ===\n')
    nome_busca = input('Digite o nome ou parte do nome: ').strip().lower()

    resultados = []
    for paciente in pacientes:
        if nome_busca in paciente['Nome'].lower():
            resultados.append(paciente)

    if resultados:
        print('\nPacientes encontrados:\n')
        for p in resultados:
            print('Nome: {}'.format(p['Nome']))
            print('Idade: {}'.format(p['Idade']))
            print('Telefone: {}'.format(p['Telefone']))
            print('----------------------------------------')
    else:
        print('\nNenhum paciente encontrado!\n')

def dados():
    print('\n=== ESTATÍSTICAS ===\n')

    if not pacientes:
        print('Total de Pacientes: 0')
        print('Idade média: 0')
        print('Paciente mais novo: Nenhum')
        print('Paciente mais velho: Nenhum')
    else:
        total = len(pacientes)

        idades = [p["Idade"] for p in pacientes]

        idade_media = sum(idades) / total

        mais_novo = min(pacientes, key=lambda p: p["Idade"])
        mais_velho = max(pacientes, key=lambda p: p["Idade"])

        print('Total de Pacientes: {}'.format(total))
        print('Idade média: {:.2f}'.format(idade_media))
        print('Paciente mais novo: {} ({} anos)'.format(mais_novo['Nome'], mais_novo['Idade']))
        print('Paciente mais velho: {} ({} anos)'.format(mais_velho['Nome'], mais_velho['Idade']))

clinicavida()
