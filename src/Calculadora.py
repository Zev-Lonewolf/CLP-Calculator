while True:
    print('\n---------------------')
    valores = []
    operacoes = []

    try:
        valor = input('Valor ou "SAIR" para encerrar: ').strip().lower()
        if valor == 'sair':
            print('Calculadora encerrada...')
            break
        valores.append(float(valor))
    except ValueError:
        print("Valor inválido!")
        continue

    while True:
        operacao = input('Operação ou "OK" para calcular: ').strip().lower()
        
        if operacao == 'ok':
            break
        elif operacao in ['+', '-', '*', '/']:
            operacoes.append(operacao)
        else:
            print('Operação inválida!')
            continue

        try:
            valor = float(input('Valor: '))
            valores.append(valor)
        except ValueError:
            print('Valor inválido!')
            operacoes.pop()
            continue

    resultado = valores[0]
    for i in range(len(operacoes)):
        op = operacoes[i]
        prox_valor = valores[i + 1]

        if op == '+':
            resultado += prox_valor
        elif op == '-':
            resultado -= prox_valor
        elif op == '*':
            resultado *= prox_valor
        elif op == '/':
            if prox_valor != 0:
                resultado /= prox_valor
            else:
                print('Erro! Divisão por zero!')
                resultado = None
                break

    if resultado is not None:
        print(f'\n{resultado}')

#BASE DA CALCULADORA TERMINADA EM 14/07/2025! by Zev Lonewolf.