#• Pergunte quantas notas o usuário quer digitar
#• Use um loop for para ler cada nota
#• Calcule a média das notas
#• Exiba a média final com 2 casas decimais
#• Informe se o aluno está:
#• APROVADO (média ≥ 7)
#• REPROVADO (média < 7)
#Exemplo de execução:
#Quantas notas deseja digitar? 4
#Digite a nota 1: 8.5
#Digite a nota 2: 7.0
#Digite a nota 3: 9.0
#Digite a nota 4: 6.5
#Média final: 7.75
#APROVADO!

notasA = int(input("quantas notas a inserir :"))

#notas ja calcular:
#notasB
for i in range(1, notasA + 1):
    notasB = float((input("notas á calcular: ")))
    if notasB >= 7:
        print("aprovado com", notasB)
    else:
        print("reprovado com", notasB)
    i = i + 1
            
print("notas fechadas!")
    
