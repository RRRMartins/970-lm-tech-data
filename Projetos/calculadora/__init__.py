from funcoes import soma
from funcoes import subtracao
from funcoes import multiplicacao
from funcoes import divisao

a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))

operacao = input('Informe a operação desejada (soma, subtracao, divisao, multiplicacao, +, -, /, *): ').lower()

if operacao == 'soma' or operacao == '+':
    print(f'O resultado da sua operação de soma: {soma(a, b)}')

elif operacao == 'subtracao' or operacao == '-':
    print(f'O resultado da sua subtração:  {subtracao(a, b)}')

elif operacao == 'multiplicacao' or operacao == '*':
    print(f'O resultado da sua multiplicação: {multiplicacao(a, b)}')

elif operacao == 'divisao' or operacao == '/':
    print(f'O resultado da sua divisão: {divisao(a, b)}')

else:
    print(f'Operação desejada inválida!')