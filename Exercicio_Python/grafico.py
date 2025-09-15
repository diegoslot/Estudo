import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Botão com Ação")

def executar_comando():
    messagebox.showinfo("Resultado", "Você clicou no botão! 🚀")

botao = tk.Button(janela, text="Clique Aqui", command=executar_comando)
botao.pack()

janela.mainloop()
