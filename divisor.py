try:
    num1=int(input("Digite o numero que você que dividir: "))
    num2=int(input("Digite o numero divisor: "))

    if num2==0:
        print("Erro: não e possivel dividir por zero.")
    else:
        resultado = num1/num2
        print(f"Resultado da divisão:{resultado}")
except ValueError:
    print("Erro: você deve digitar apenas números inteiros.")