from tkinter import Menu


nomes = []
notas1= []
notas2= []

def cadastrar ():
    nome =  input ("Nome do estudante: ")
    nota1 = float (input ("Nota 1: ")) # casting (to cast)
    nota2 = float (input ("Nota 2: "))

    nomes.append(nomes)
    notas1.append(notas1)
    notas2.append(notas2)
    print("Estudante cadastrado!")

def calcular_media(indice):
    return (notas1[indice] + notas2[indice]) / 2

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Reprovado"

def listar():
    if len(nomes) == 0:
        print ("Nenhum estudante cadastro. ")
        return

    print(f"\n{'NOME': <16}{'N1': <7}{'N2': <7}{'MÉDIA': <8}{'SITUAÇÃO': <14}")

    for i in range (len(nomes)):
        print (f" {nomes[i]: <16} {notas1[i]: <7} {notas2[i]: <7} "f" {calcular_media(i): <8.1f} {situacao(i): <14} ")

def mediaTurma():
    if len(nomes) == 0:
        print("Nenhum estudante cadastro.")
        return

        soma = 0 
        for i in (len(nomes)): 
            soma = soma + calcularmedia(i)
        print(f"\nMédia da turma: {soma/len(nomes):.2f}")

    def menu():
        while True:
            print("\n1 - Cadrastrar estudantes")
            print("2 - Lista estudantes")
            print("3 - Média da turma")
            print("0 - Sair")

            opcao = input("Opção: ")

            if opcao == "1":
                cadastrar()
            elif opcao == "2":
                listar()
            elif opcao == "3":
                mediaTurma()
            elif opcao == "0":
                break
            else:
                print("Opcao Inválida.")

Menu()


