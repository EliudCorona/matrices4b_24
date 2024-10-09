def sumatoria_recursiva(n):
    if n == 0:
        return 0
    else:
        return n*n + sumatoria_recursiva(n - 1)

n=4
print(f"La sumatoria de {n} es: {sumatoria_recursiva(n)}")