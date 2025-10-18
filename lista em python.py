n=int(input("Digite quantas elementos possui a lista:"))
lista=[0]*n 
for i in range(n):
    lista[i]=int(input(f"Digite um {i+1} valor:"))
print(lista)
