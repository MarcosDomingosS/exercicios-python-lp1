numeros = []

for n in range(10):
    numeros.append(int(input(f"digite a {n+1}° nota\n")))

print("Números pares digitados:")
for n in numeros:
    if(n%2==0):
        print(f"{n}")