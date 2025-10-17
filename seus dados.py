nome=input("Prezado usuário digite seu nome: ")
curso=input("Olá novamente, digite qual seu curso: ")
print(f"\n Seja bem vindo (a), {nome}! \n Desejamos muito sucesso no curso de {curso}!")

print("\n")
print("*"*20)
print("\nDados de contato\n")
print("*"*20)

email=input("Digite seu e-mail: ")
tel=input("Digite seu telefone ")
idade=int(input("Digite sua idade: "))
renda=float(input("Digite sua renda: "))

print("\n")
print("*"*20)
print("\nRelatório de dado\n")
print("*"*20)
print(f"nome: {nome}\n email: {email}\n telefone: {tel}\n idade: {idade}\n renda de R$: {renda:.2f}")