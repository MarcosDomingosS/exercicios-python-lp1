numeros = []
soma = 0

for n in range(5):
    numeros.append(int(input(f"digite o {n+1}° número\n")))

soma=sum(numeros)
print(f"a soma de {numeros} é {soma}")

