#importando biblioteca de número aleatorio e criando apelido
import random as rd
#importando biblioteca grafica
# estudar python do gui
#import tkinter as tk
#janela =tk.Tk()
#janela.title("Meu primeiro Programa")
# Criar uma janela
#janela = tk.Tk()
#janela.title("Meu primeiro Programa")
# Adicionar um botão
#botao = tk.Button(janela, text="Clique Aqui", command="exibir_mensagem")
#botao.pack()
#informando que o numero é inteiro de 1 a 10
aleatorio=rd.randint(1,10)
while True:
    numero=int(input("Digite um número de 1 a 10: "))
    if numero==aleatorio:
        print("Acertou",aleatorio)
        break
    else:
        print("Tente novamente!")


"""
nome="Diego Luis de Oliveira Lima"
cpf="12345678910"
for i in nome:
    print(i,end="")
print()
for i in cpf:
    print(i,end="")
"""