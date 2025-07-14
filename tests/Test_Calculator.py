valores: []
operacoes: []

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
        
    try:
        valor2 = float(input('Valor: '))
    except ValueError:
        print('Valor Inválido! Insira um número válido.')
        continue

    if operação == '+':
        resultado = valor1 + valor2
    elif operação == '-':
        resultado = valor1 - valor2
    elif operação == '*':
        resultado = valor1 * valor2
    elif operação == '/':
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            print('Não é possivel dividir por zero!')
            continue
    else:
        print('Operação inválida!')
        continue

    print(f'{resultado}')
    valor1 = resultado      