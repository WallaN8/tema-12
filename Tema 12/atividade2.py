#• Peça ao usuário 5 nomes usando um loop for

#• Armazene todos os nomes em uma lista

#• Depois, exiba cada nome em letras maiúsculas

#Exemplo de execução:

#Digite o 1º nome: ana

#Digite o 2º nome: bruno

#Digite o 3º nome: carla

#Digite o 4º nome: daniel

#Digite o 5º nome: elisa

#Nomes em maiúsculo:

#ANA

#BRUNO

#CARLA

#DANIEL

#ELISA

#💡 Dicas

#• Crie uma lista vazia: nomes = []

#• Use for i in range(5) para repetir 5 vezes

#• Use .append() para guardar os nomes

#• Use .upper() para converter para maiúsculo


nomes = []

Y = 5

for i in range(1, 6):

    nomes = str(input("digite o nome de 5 alunos:"))  
    Y = Y - 1
    print("faltam: ", Y)  
    nomes_formatados = nomes.upper()
    print(nomes_formatados)
    i = i + 1

print("fim da contagem de alunos!")