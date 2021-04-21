import funcoes

continuar = 'Ss'
while continuar in 'Ss':
    funcoes.linha()
    n1 = float(input('Primeiro Nº: ')) #Primeiro valor
    n2 = float(input('Segundo Nº: ')) #Segundo valor
    funcoes.linha()
    print('''\033[0;32m
    ############# MENU ###############
    #ESCOLHA UMA DAS OPÇÕES A SEGUIR:#
    ##################################
    #[1] SOMAR
    #[2] MULTIPLICAÇÃO
    #[3] DIVISÃO
    #[4] SUBTRAÇÃO
    #[5] TROCAR NÚMEROS
    #[0] SAIR\033[m''')
    opc = int(input('Opção: '))
    if opc == 1:#Somar
        print(f'O resultado é: {funcoes.soma(n1, n2)}')
        continuar =  str(input('\033[1;33mDeseja continuar? S ou N?\033[m'))
    elif opc == 2:#Multiplicar
        print(f'O resultado é: {funcoes.multi(n1, n2)}')
        continuar =  str(input('\033[1;33mDeseja continuar? S ou N?\033[m'))
    elif opc == 3:#Divisão
        print(f'O resultado é: {funcoes.div(n1, n2)}')
        continuar =  str(input('\033[1;33mDeseja continuar? S ou N?\033[m'))
    elif opc == 4:#Subtração
        print(f'O resultado é: {funcoes.subtrair(n1, n2)}')
        continuar =  str(input('\033[1;33mDeseja continuar? S ou N?\033[m'))
    elif opc == 5:#Troca de valores
        n1 = int(input('Novo valor para primeiro: '))
        n2 = int(input('Novo valor para segundo: '))
    elif opc == 0:#Finalizar calculadora
        print('\033[1;34mAté outra hora! o/\033[m')
        break
    else:#Aviso de erro!
        print('\033[1;31mOpção errada, tente novamente!\033[m')
print('\033[1;33mFinzalizando...\033[m')