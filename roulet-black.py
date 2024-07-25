import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox

# Configurações de cor para o modo escuro
BACKGROUND_COLOR = '#2e2e2e'
FOREGROUND_COLOR = '#ffffff'
BUTTON_COLOR = '#444444'
ENTRY_COLOR = '#333333'
ENTRY_TEXT_COLOR = '#ffffff'

def selecionar_pasta():
    caminho_pasta = filedialog.askdirectory()
    entrada_pasta.delete(0, tk.END)
    entrada_pasta.insert(0, caminho_pasta)

def animar_roleta(contador=0, numero_sorteado=None):
    numero_atual = (contador % 6) + 1
    label_animacao.config(text=str(numero_atual))
    
    if contador < 20:  # Número de iterações para a animação
        janela.after(100, animar_roleta, contador + 1, numero_sorteado)
    else:
        # Mostra o número sorteado após a animação
        if numero_sorteado is not None:
            label_animacao.config(text=str(numero_sorteado))  # Mostra o número sorteado
            roleta_russa(numero_sorteado)

def roleta_russa(numero_sorteado):
    caminho_pasta = entrada_pasta.get()
    numero_selecionado = entrada_numero.get()
    
    print(f"Caminho da Pasta: {caminho_pasta}")
    print(f"Número Selecionado: {numero_selecionado}")
    print(f"Número Sorteado: {numero_sorteado}")

    # Verifica se o número selecionado é válido
    if not numero_selecionado.isdigit() or not (1 <= int(numero_selecionado) <= 6):
        messagebox.showerror("Erro", "Por favor, insira um número entre 1 e 6.")
        return
    
    numero_selecionado = int(numero_selecionado)
    
    # Verifica se o caminho é uma pasta válida
    if not os.path.isdir(caminho_pasta):
        messagebox.showerror("Erro", f"O caminho {caminho_pasta} não é uma pasta válida.")
        return
    
    # Lista os arquivos da pasta
    arquivos = os.listdir(caminho_pasta)
    
    # Verifica se a pasta não está vazia
    if not arquivos:
        messagebox.showinfo("Informação", "A pasta está vazia.")
        return
    
    # Simula a roleta russa
    if numero_selecionado == numero_sorteado:
        arquivo_selecionado = random.choice(arquivos)
        caminho_arquivo_selecionado = os.path.join(caminho_pasta, arquivo_selecionado)
        try:
            os.remove(caminho_arquivo_selecionado)
            messagebox.showinfo("Resultado", f"Você perdeu! O arquivo {arquivo_selecionado} foi excluído.")
        except PermissionError:
            messagebox.showerror("Erro", f"Não foi possível excluir o arquivo {arquivo_selecionado} devido a um erro de permissão.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao excluir o arquivo {arquivo_selecionado}: {e}")
    else:
        messagebox.showinfo("Resultado", "Você ganhou! Nenhum arquivo foi excluído.")

def iniciar_roleta():
    numero_selecionado = entrada_numero.get()
    
    # Verifica se o número selecionado é válido
    if not numero_selecionado.isdigit() or not (1 <= int(numero_selecionado) <= 6):
        messagebox.showerror("Erro", "Por favor, insira um número entre 1 e 6.")
        return
    
    numero_sorteado = random.randint(1, 6)
    animar_roleta(numero_sorteado=numero_sorteado)

# Cria a janela principal
janela = tk.Tk()
janela.title("Roleta Russa de Arquivos")

# Configura o tema escuro
janela.config(bg=BACKGROUND_COLOR)

# Cria e posiciona os widgets
tk.Label(janela, text="Caminho da Pasta:", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR).grid(row=0, column=0, padx=10, pady=10)
entrada_pasta = tk.Entry(janela, width=50, bg=ENTRY_COLOR, fg=ENTRY_TEXT_COLOR)
entrada_pasta.grid(row=0, column=1, padx=10, pady=10)
btn_selecionar_pasta = tk.Button(janela, text="Selecionar Pasta", bg=BUTTON_COLOR, fg=FOREGROUND_COLOR, command=selecionar_pasta)
btn_selecionar_pasta.grid(row=0, column=2, padx=10, pady=10)

tk.Label(janela, text="Digite um número (1 a 6):", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR).grid(row=1, column=0, padx=10, pady=10)
entrada_numero = tk.Entry(janela, width=10, bg=ENTRY_COLOR, fg=ENTRY_TEXT_COLOR)
entrada_numero.grid(row=1, column=1, padx=10, pady=10)

btn_roleta_russa = tk.Button(janela, text="Rodar Roleta Russa", bg=BUTTON_COLOR, fg=FOREGROUND_COLOR, command=iniciar_roleta)
btn_roleta_russa.grid(row=2, columnspan=3, pady=20)

label_animacao = tk.Label(janela, text="", font=("Helvetica", 32), bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
label_animacao.grid(row=3, columnspan=3, pady=20)

# Inicia o loop principal da interface gráfica
janela.mainloop()
