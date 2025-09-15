import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess

# Criar janela
janela = tk.Tk()
janela.title("Gerenciador Linux")
janela.geometry("600x400")

# Caixa de saída (para mostrar resultados)
saida = scrolledtext.ScrolledText(janela, width=70, height=15)
saida.pack(pady=10)

# Funções
def atualizar_ubuntu():
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        messagebox.showinfo("Sucesso", "Sistema atualizado com sucesso 🚀")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha na atualização: {e}")

def verificar_disco():
    try:
        resultado = subprocess.check_output(["df", "-h"], text=True)
        saida.delete(1.0, tk.END)
        saida.insert(tk.END, resultado)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao verificar disco: {e}")

def verificar_processos():
    try:
        resultado = subprocess.check_output("ps -e | head -n 20", shell=True, text=True)
        saida.delete(1.0, tk.END)
        saida.insert(tk.END, resultado)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao verificar processos: {e}")

# Botões
btn_update = tk.Button(janela, text="Atualizar Ubuntu", width=20, command=atualizar_ubuntu)
btn_update.pack(pady=5)

btn_disco = tk.Button(janela, text="Verificar Espaço em Disco", width=20, command=verificar_disco)
btn_disco.pack(pady=5)

btn_proc = tk.Button(janela, text="Verificar Processos", width=20, command=verificar_processos)
btn_proc.pack(pady=5)

janela.mainloop()
