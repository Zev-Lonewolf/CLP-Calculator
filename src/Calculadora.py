valores = []
operacoes = []

while True:
    try:
        valor = float(input('Valor: '))
        valores.append(valor)
    except ValueError:
        print('Valor Inválido! Insira um número válido.')
        continue

    operação = input('Operação ou OK para sair: ').strip().lower()

    if operação == 'ok':
        break
    elif operação in ['+', '-', '*', '/']:
        operacoes.append(operação)
    else:
        print('Operação inválida!')
        valores.pop()
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
    print({resultado})