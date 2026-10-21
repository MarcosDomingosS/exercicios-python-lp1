numeros = []

for n in range(4):
    nota = int(input(f"Digite a {n+1}° nota: "))
    numeros.append(nota)

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / 4

print(f"\nNotas digitadas: {numeros}")
print(f"A média das notas é: {media}")
print(f"A maior nota é: {maior}")
print(f"A menor nota é: {menor}")
