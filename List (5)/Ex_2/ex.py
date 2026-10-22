def som (num1, num2):
    return num1 + num2

def sub (num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return float('inf')

def exibir_menu ():
    process = True
    while process:
        print(
            "==== CALCULADORA =====\n" \
            "1  -   Somar\n" \
            "2  -   Subtrair\n" \
            "3  -   Multiplicar\n" \
            "4  -   Dividir\n" \
            "0  -   Sair\n" \
        )

        opt = int(input("Escolha a operação: "))
        
        match opt:
            case 1:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print(som(num1, num2))
            case 2:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print(sub(num1, num2))
            case 3 :
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print(mult(num1, num2))
            case 4:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print(div(num1, num2))
            case 0:
                process = False
            case _:
                print("Opção invalida! Por favor, digite uma opção válida")


exibir_menu()