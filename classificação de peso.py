try:
    peso=float(input("Digite seu peso em kg: "))
    altura=float(input("Digite sua altura em metros: "))
    imc=peso / (altura**2)
    print(f"seu imc é: {imc:.2f}")
    if imc < 18.5:
        print("classificação: Abaixo do peso")
    elif imc < 24.9:
        print("classificação: Peso normal")
    elif imc < 29.9:
        print("classificação: Sobrepeso")
    elif imc < 34.9:
        print("classificação: Obesidade grau 1")
    elif imc < 39.9:
        print("classificação: Obesidade grau 2")
    else:
        print("classificação: Obesidade grau 3")

except ValueError:
    print("Erro: digite valores validos para o peso / altura.")