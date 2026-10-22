def tabuada(n1):
        for n2 in range(1,11):
            print(f"{n1} X {n2} = {n1*n2}")
        print("\n")
 
def fatorial(num):
    result = 1
    for n in range(num):
        result *= (n+1)
 
    print(f"{num}! = {result}")
 
def exibirMenu():
    resultado = False
    while not resultado:
        opcao = int(input("Selecione a opção:\n"
                           "1 - Tabuada\n"
                           "2 - Fatorial\n"
                           "3 - Sair\n"))
        if(opcao>0 and opcao<3):
            numero = int(input("Qual o numero: "))
            resultado = True
            match opcao:
                case 1:
                      tabuada(numero)
                case 2:
                      fatorial(numero)
        elif(opcao==3):
             break
        else:
             print("Opção inválida\n")
 
exibirMenu()