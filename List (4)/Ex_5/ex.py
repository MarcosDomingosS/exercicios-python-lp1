numeros = []
positivo = 0
negativo = 0
zero = 0

for n in range(8):

    numeros.append(int(input(f"Digite a {n+1}ª nota: ")))


for n in numeros:
    if n < 0:
        negativo += 1
    elif n > 0:
        positivo += 1
    else:
        zero += 1

print(f"\nTotal de positivos: {positivo}")
print(f"Total de negativos: {negativo}")
print(f"Total de zeros: {zero}")