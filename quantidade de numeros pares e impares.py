n=int(input("Quantos elementos terá a lista?"))

lista=[0]*n
for i in range(n):
    lista[i]=int(input(f"Digite o {i+1} número:"))

pares=0
impares=0

for num in lista:
    if num%2==0:
        pares+=1
    else:
        impares+=1
print("\nLista digitada:", lista)
print(f"Quantidade de números pares: {pares}")
print("Quantidade de números impares:", impares)