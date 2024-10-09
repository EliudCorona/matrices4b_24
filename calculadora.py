# calculadora.py
def suma(a, b):
    return a + b

def es_numero_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

