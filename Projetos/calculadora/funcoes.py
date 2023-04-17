def soma(a,b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError(f'O input fornecido deve ser um número.')

def subtracao(a, b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b