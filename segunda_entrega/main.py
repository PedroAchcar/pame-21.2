from onibus import Onibus
from paradas import Parada
from pessoas import Fiscal, Motorista


def mostrarOnibus(onibus):
    if onibus == []:
        print('Nenhuma linha de onibus adicionada.')
        return -1
    else:
        for i in onibus:
            print(i)


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

# def selecionarFiscal(fiscais):
#     if fiscais == []:
#         print('Nenhuma fiscal adicionado.')
#     else:
#         for i in fiscais:
#             print(i)
#     if retorno == -1:
#         pass
#     else:
#         a = int(input('Qual fiscal deseja escolher? '))

#         for i in fiscais:
#             if a == i.codigo_fiscal:
#                 return i


def menuCriar():
    print('-'*40)
    print('1 - Criar onibus')
    print('2 - Criar ponto de parada')
    print('3 - Criar motorista')
    print('4 - Criar fiscal')


def menuMostrar():
    print('-'*40)
    print('1 - Mostrar onibus')
    print('2 - Mostrar rotas')
    print('3 - Mostrar motoristas')
    print('4 - Mostrar fiscais')


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
    print('5 - Alterar rota do ônibus')


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
    paradas = Parada([])
    motoristas = []
    fiscais = []

    while True:
        menuPrincipal()
        op_acao = input('Escolha uma acao: ')

        if op_acao == '1':
            menuCriar()
            op = input('O que deseja criar? ')

            if op == '1':
                linha = int(input('Digite o numero da linha: '))
                descricao = input(
                    'Digite o itinerario (Ex: Copacabana x Fundão): ')
                # if onibus == []:
                onibus.append(Onibus(linha, descricao))
# PROBLEMA ------------------------------------------------------

                # else:
                # if linha == i.codigo_onibus:
                #     print('Linha ja existente')
                # else:
                #   onibus.append(Onibus(linha))

# PROBLEMA ------------------------------------------------------
            elif op == '2':
                ponto = (input('Digite o nome do ponto de parada: '))
                paradas.criarParada(ponto)

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

            else:
                print('Opcao invalida!')

        elif op_acao == '2':
            menuMostrar()
            op = input('O que deseja mostrar? ')

            if op == '1':
                mostrarOnibus(onibus)

            elif op == '2':
                print('AINDA NÃO FIZ')
                pass

            elif op == '3':
                mostrarMotoristas(motoristas)

            elif op == '4':
                mostrarFiscais(fiscais)

            else:
                print('Opcao invalida!')

        elif op_acao == '3':
            menuAssignar()
            op = input('O que deseja assignar? ')

            if op == '1':
                bus = selecionarOnibus(onibus)
                moto = selecionarMotorista(motoristas)
                if bus == None or moto == None:
                    print('Alguma informacao faltando')
                else:
                    bus.assignarMotorista(moto)
                    moto.assignarOnibus(bus)

            elif op == '2':
                bus = selecionarOnibus(onibus)
                fiscal = selecionarFiscal(fiscais)
                if bus == None or fiscal == None:
                    print('Alguma informacao faltando')
                else:
                    bus.assignarFiscal(fiscal)
                    fiscal.assignarOnibus(bus)

            elif op == '3':
                print('AINDA NÃO FIZ')
                pass

            else:
                print('Opcao invalida!')

        elif op_acao == '4':
            menuAlterar()
            op = input('O que deseja alterar? ')

            if op == '1':
                bus = selecionarOnibus(onibus)
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
                # ponto = selecionarParada(paradas)
                # dado = input('Digite o novo valor para a parada: ')
                # parada = dado
                print('AINDA NÃO FIZ')
                pass

            if op == '3':
                moto = selecionarMotorista(motoristas)
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
                fisc = selecionarFiscal(fiscais)
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

            if op == '5':
                # fisc = selecionarFiscal(fiscais)
                # print('1 - Nome do fiscal')
                # print('2 - Codigo do fiscal')
                # op_dado = input('Qual dado deseja alterar? ')
                # dado = input('Digite o novo dado: ')

                # if op_dado == '1':
                #     fisc.nome = dado
                # elif op_dado == '2':
                #     fisc.codigo_fiscal = dado
                # else:
                #     print('Selecione uma opcao valida')
                print('AINDA NÃO FIZ')
                pass

        elif op_acao == '5':
            menuDeletar()
            op = input('O que deseja deletar? ')

            if op == '1':
                bus = selecionarOnibus(onibus)

        elif op_acao == '0':
            break

        else:
            print('Opcao invalida')


if __name__ == '__main__':
    main()
