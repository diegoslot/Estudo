import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import subprocess



# Criar janela principal
janela = tk.Tk()
janela.title("Painel de Comandos Linux")
janela.geometry("900x500")

# Frame lateral para os botões
menu_lateral = tk.Frame(janela, bg="#2c3e50", width=250)
menu_lateral.pack(side="left", fill="y")

# Área de saída à direita
saida = scrolledtext.ScrolledText(janela, width=90, height=30, bg="black", fg="lime", font=("Courier", 10))
saida.pack(side="right", fill="both", expand=True, padx=5, pady=5)

# Função auxiliar para rodar comandos e mostrar resultado
def executar_comando(comando, shell=False):
    try:
        resultado = subprocess.check_output(comando, shell=shell, text=True, stderr=subprocess.STDOUT)
        saida.delete(1.0, tk.END)
        saida.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        saida.delete(1.0, tk.END)
        saida.insert(tk.END, f"Erro:\n{e.output}")

# Funções para os botões
def atualizar_ubuntu():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])
    messagebox.showinfo("Sucesso", "Sistema atualizado com sucesso 🚀")

def verificar_disco():
    executar_comando(["df", "-h"])

def verificar_processos():
    executar_comando("ps -e | head -n 20", shell=True)

def compactar_tar():
    arquivo = simpledialog.askstring("Compactar Arquivo", "Digite o nome do arquivo ou pasta:")
    if arquivo:
        nome_tar = simpledialog.askstring("Nome do .tar", "Digite o nome do arquivo .tar:")
        if nome_tar:
            executar_comando(["tar", "-cvf", nome_tar, arquivo])

def abrir_nano():
    arquivo = simpledialog.askstring("Abrir Nano", "Digite o nome do arquivo para editar:")
    if arquivo:
        subprocess.run(["nano", arquivo])  # abre no terminal

def comparar_diff():
    arq1 = simpledialog.askstring("diff", "Digite o primeiro arquivo:")
    arq2 = simpledialog.askstring("diff", "Digite o segundo arquivo:")
    if arq1 and arq2:
        executar_comando(["diff", arq1, arq2])

def localizar_arquivo():
    termo = simpledialog.askstring("locate", "Digite o nome do arquivo para localizar:")
    if termo:
        executar_comando(["locate", termo])

def procurar_find():
    pasta = simpledialog.askstring("find", "Digite o diretório (ex: /home):")
    nome = simpledialog.askstring("find", "Digite o nome do arquivo:")
    if pasta and nome:
        executar_comando(["find", pasta, "-name", nome])

def mudar_permissao():
    arquivo = simpledialog.askstring("chmod", "Digite o arquivo:")
    permissao = simpledialog.askstring("chmod", "Digite a permissão (ex: 755):")
    if arquivo and permissao:
        executar_comando(["chmod", permissao, arquivo])
        messagebox.showinfo("Sucesso", f"Permissão {permissao} aplicada em {arquivo}")

# 🔴 Função para sair
def sair():
    janela.destroy()

# Criar botões no menu lateral
botoes = [
    ("Atualizar Ubuntu", atualizar_ubuntu),
    ("Espaço em Disco", verificar_disco),
    ("Ver Processos", verificar_processos),
    ("Compactar (tar)", compactar_tar),
    ("Abrir Nano", abrir_nano),
    ("Comparar Arquivos (diff)", comparar_diff),
    ("Localizar Arquivo (locate)", localizar_arquivo),
    ("Procurar Arquivo (find)", procurar_find),
    ("Alterar Permissão (chmod)", mudar_permissao),
    ("❌ Sair", sair),  # <-- botão de sair
]

for texto, comando in botoes:
    btn = tk.Button(menu_lateral, text=texto, width=25, command=comando, bg="#34495e", fg="white", relief="flat")
    btn.pack(pady=5, padx=10)

janela.mainloop()
