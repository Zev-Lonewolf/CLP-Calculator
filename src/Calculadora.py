valor1 = float(input('Primeiro número: '))
operacao = str(input('operação: '))
valor2 = float(input('Segundo número: '))
resultado = 0

while True:
    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '-':
        resultado = valor1 - valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '/':
        resultado = valor1 / valor2
    else:
        print('Valor ou operação errada!!')
    break

print(resultado)