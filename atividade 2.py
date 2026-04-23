while True:
    numero = int(input("Digite um numero positivo: "))
    
    if numero < 0:
        print("ERRO! O numero nao pode ser negativo.")
    else:
        print("Numero:", numero)
        break