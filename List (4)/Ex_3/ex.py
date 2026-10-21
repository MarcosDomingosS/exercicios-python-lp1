numeros = []

for n in range(4):
    numeros.append(int(input(f"digite a {n+1}° nota\n")))

soma = sum(numeros)
media = soma/4
print(f"a média das notas {numeros} é {soma}")

