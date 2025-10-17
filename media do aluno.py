nome=input("Digite o nome do aluno: ")
av1=float(input("Digite a nota do av1 do aluno: "))
av2=float(input("Digie a nota do av2 do aluno: "))
media=(av1+av2)/2
if(media>=6):
    print(f"o aluno {nome} está aprovado com media igual a {media:.2f}")
elif (media>=4.0):
    print(f"o aluno {nome} está exame final com media igual a {media:.2f}")
else:
    print(f"o aluno {nome} está reprovado com a media ingual a {media:.2f}")
    