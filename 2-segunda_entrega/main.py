from onibus import Onibus
from paradas import Parada, Rota
from pessoas import Fiscal, Motorista


def mostrarOnibus(onibus):
    if onibus == []:
        print('Nenhuma linha de onibus adicionada.')
        return -1
    else:
        for i in onibus:
            print(f'{i} - {i.descricao}')


def selecionarOnibus(onibus):
    retorno = mostrarOnibus(onibus)
    if retorno == -1:
        pass
    else:
        a = int(input('Qual onibus deseja escolher? '))

        for i in onibus:
            if a == i.codigo_onibus:
                return i, onibus.index(i)


def mostrarMotoristas(motoristas):
    if motoristas == []:
        print('Nenhum motorista adicionado.')
        return -1
    else:
        for i in motoristas:
            print(f'{i.codigo_motorista} - {i.nome}')


def selecionarMotorista(motoristas):
    retorno = mostrarMotoristas(motoristas)
    if retorno == -1:
        pass
    else:
        a = int(input('Qual motorista deseja escolher? '))

        for i in motoristas:
            if a == i.codigo_motorista:
                return i, motoristas.index(i)


def mostrarFiscais(fiscais):
    if fiscais == []:
        print('Nenhuma fiscal adicionado.')
        return -1
    else:
        for i in fiscais:
            print(i)


def selecionarFiscal(fiscais):
    retorno = mostrarFiscais(fiscais)
    if retorno == -1:
        pass
    else:
        a = int(input('Qual fiscal deseja escolher? '))

        for i in fiscais:
            if a == i.codigo_fiscal:
                return i, fiscais.index(i)


def mostrarParadas(paradas):
    if paradas == []:
        print('Nenhuma parada adicionada.')
        return -1
    else:
        for i in paradas:
            print(i)


def selecionarParada(paradas):
    retorno = mostrarParadas(paradas)
    if retorno == -1:
        pass
    else:
        a = int(input('Qual parada deseja escolher? '))

        for i in paradas:
            if a == i.codigo_parada:
                return i, paradas.index(i)


def mostrarRotas(rotas):
    if rotas == []:
        print('Nenhuma rota adicionada.')
        return -1
    else:
        for i in range(len(rotas)):
            print(rotas[i][0])


def selecionarRota(rotas):
    retorno = mostrarRotas(rotas)
    if retorno == -1:
        pass
    else:
        a = int(input('Qual rota deseja escolher? '))

        for i in rotas:
            if a == i[0].codigo_rota:
                return i, rotas.index(i)


def menuCriar():
    print('-'*40)
    print('1 - Criar onibus')
    print('2 - Criar ponto de parada')
    print('3 - Criar motorista')
    print('4 - Criar fiscal')
    print('5 - Criar rota')


def menuMostrar():
    print('-'*40)
    print('1 - Mostrar onibus')
    print('2 - Mostrar paradas')
    print('3 - Mostrar motoristas')
    print('4 - Mostrar fiscais')
    print('5 - Mostrar rotas')


def menuAssignar():
    print('-'*40)
    print('1 - Assignar motorista ao onibus')
    print('2 - Assignar fiscal ao ônibus')
    print('3 - Adicionar ponto de parada ao ônibus')


def menuAlterar():
    print('-'*40)
    print('1 - Alterar dados do onibus')
    print('2 - Alterar dados da parada')
    print('3 - Alterar dados do motorista')
    print('4 - Alterar dados do fiscal')


def menuDeletar():
    print('-'*40)
    print('1 - Deletar onibus')
    print('2 - Deletar ponto de parada')
    print('3 - Deletar motorista')
    print('4 - Deletar fiscal')


def menuPrincipal():
    print('-'*40)
    print('1 - Criar')
    print('2 - Mostrar')
    print('3 - Assignar')
    print('4 - Alterar')
    print('5 - Deletar')
    print('0 - Sair do programa')


def main():
    onibus = []
    paradas = []
    motoristas = []
    fiscais = []
    rotas = []

    while True:
        menuPrincipal()
        op_acao = input('Escolha uma acao: ')

        if op_acao == '1':
            menuCriar()
            op = input('O que deseja criar? ')

            if op == '1':
                linha = int(
                    input('Digite o numero da linha (somente numeros): '))
                descricao = input(
                    'Digite o itinerario (Ex: Copacabana x Fundão): ')
                onibus.append(Onibus(linha, descricao))

            elif op == '2':
                codigo_parada = int(
                    input('Codigo da parada (somente numeros): '))
                nome_parada = input('Digite o nome do ponto de parada: ')
                paradas.append(Parada(codigo_parada, nome_parada))

            elif op == '3':
                nome_mot = input('Nome do motorista: ')
                codigo_mot = int(
                    input('Codigo do motorista (somente numeros): '))
                motorista = Motorista(nome_mot, codigo_mot)
                motoristas.append(motorista)

            elif op == '4':
                nome_fis = input('Nome do fiscal: ')
                codigo_fis = int(input('Codigo do fiscal (somente numeros): '))
                fiscal = Fiscal(nome_fis, codigo_fis)
                fiscais.append(fiscal)

            elif op == '5':
                rota = []
                try:
                    while True:
                        parada, parada_index = selecionarParada(paradas)
                        rota.append(parada)
                        op = input('Parar de adicionar pontos a rota (s/n)? ')
                        if op == 's':
                            break
                    codigo_rota = int(
                        input('Codigo da rota (somente numeros): '))
                    rotas.append([Rota(rota, codigo_rota)])
                except:
                    print('Nenhuma parada adicionada')

            else:
                print('Opcao invalida!')

        elif op_acao == '2':
            menuMostrar()
            op = input('O que deseja mostrar? ')

            if op == '1':
                mostrarOnibus(onibus)

            elif op == '2':
                mostrarParadas(paradas)

            elif op == '3':
                mostrarMotoristas(motoristas)

            elif op == '4':
                mostrarFiscais(fiscais)

            elif op == '5':
                mostrarRotas(rotas)

            else:
                print('Opcao invalida!')

        elif op_acao == '3':
            menuAssignar()
            op = input('O que deseja assignar? ')

            try:
                if op == '1':
                    bus, bus_index = selecionarOnibus(onibus)
                    moto, moto_index = selecionarMotorista(motoristas)
                    if bus == None or moto == None:
                        print('Alguma informacao faltando')
                    else:
                        bus.assignarMotorista(moto)
                        moto.assignarOnibus(bus)

                elif op == '2':
                    bus, bus_index = selecionarOnibus(onibus)
                    fiscal, fisc_index = selecionarFiscal(fiscais)
                    if bus == None or fiscal == None:
                        print('Alguma informacao faltando')
                    else:
                        bus.assignarFiscal(fiscal)
                        fiscal.assignarOnibus(bus)

                elif op == '3':
                    rota, rota_index = selecionarRota(rotas)
                    bus, bus_index = selecionarOnibus(onibus)
                    if bus == None or rota == None:
                        print('Alguma informacao faltando')
                    else:
                        bus.assignarRota(rota)
                else:
                    print('Opcao invalida!')
            except:
                print('Onibus, motorista, fiscal ou rota não cadastrado ainda.')

        elif op_acao == '4':
            menuAlterar()
            op = input('O que deseja alterar? ')

            if op == '1':
                bus, bus_index = selecionarOnibus(onibus)
                print('1 - Codigo do onibus')
                print('2 - Descricao do onibus')
                op_dado = input('Qual dado deseja alterar? ')
                dado = input('Digite o novo dado: ')

                if op_dado == '1':
                    bus.codigo_onibus = dado
                elif op_dado == '2':
                    bus.descricao = dado
                else:
                    print('Selecione uma opcao valida')

            if op == '2':
                parada, parada_index = selecionarParada(paradas)
                print('1 - Codigo do ponto de parada')
                print('2 - Nome do ponto de parada')
                op_dado = input('Qual dado deseja alterar? ')
                dado = input('Digite o novo dado: ')

                if op_dado == '1':
                    parada.codigo_parada = dado
                elif op_dado == '2':
                    parada.nome = dado
                else:
                    print('Selecione uma opcao valida')

            if op == '3':
                moto, moto_index = selecionarMotorista(motoristas)
                print('1 - Nome do motorista')
                print('2 - Codigo do motorista')
                op_dado = input('Qual dado deseja alterar? ')
                dado = input('Digite o novo dado: ')

                if op_dado == '1':
                    moto.nome = dado
                elif op_dado == '2':
                    moto.codigo_motorista = dado
                else:
                    print('Selecione uma opcao valida')

            if op == '4':
                fisc, fisc_index = selecionarFiscal(fiscais)
                print('1 - Nome do fiscal')
                print('2 - Codigo do fiscal')
                op_dado = input('Qual dado deseja alterar? ')
                dado = input('Digite o novo dado: ')

                if op_dado == '1':
                    fisc.nome = dado
                elif op_dado == '2':
                    fisc.codigo_fiscal = dado
                else:
                    print('Selecione uma opcao valida')

        elif op_acao == '5':
            menuDeletar()
            op = input('O que deseja deletar? ')

            try:
                if op == '1':
                    bus, bus_index = selecionarOnibus(onibus)
                    onibus.pop(bus_index)

                elif op == '2':
                    parada, parada_index = selecionarParada(paradas)
                    paradas.pop(parada_index)

                elif op == '3':
                    moto, moto_index = selecionarMotorista(motoristas)
                    motoristas.pop(moto_index)

                elif op == '4':
                    fisc, fisc_index = selecionarFiscal(fiscais)
                    fiscais.pop(fisc_index)

                else:
                    print('Opcao invalida')

            except:
                print('Onibus, motorista, fiscal ou rota não cadastrado ainda.')

        elif op_acao == '0':
            break

        else:
            print('Opcao invalida')


if __name__ == '__main__':
    main()
