x=int(input("Quantos elementos tem as listas?"))
lista1=[0]*x
lista2=[0]*x
lista3=[0]*x
print("Lendo a primeira lista")
for i in range (x):
    lista1[i]=int(input(f"Digite o valor do {i+1} elemento"))
print("Lendo a segunda lista")
for i in range (x):
    lista2[i]=int(input(f"Diginte o valor do {i+1} elemento"))
print("Calculando a soma dos elementos")
for i in range (x):
    lista3[i]=lista1[i]+lista2[i]

print(lista3)
