def soma(a,b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError(f'O input fornecido deve ser um string, recebido {a}, tipo({type(a)}), {b} tipo ({type(b)}).')

def subtracao(a, b):
    return a - b

def multiplicacao(a,b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        raise TypeError(f'O input fornecido deve ser um string, recebido {a}, tipo({type(a)}), {b} tipo ({type(b)}).')

def divisao(a,b):
    if b != 0:
        return a / b
    else: 
        return 0
    