import random
import string
import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import pyperclip

# string.ascii_letters > letras
# string.digits > numeros
# string.punctuation > caractere especiais


def generate():
  try:
    size = int(input_entry.get())
    chars = ""

    if checkbox_letras.get():
        chars += string.ascii_letters
    if checkbox_numeros.get():
        chars += string.digits
    if checkbox_caracteres.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning('Alerta', 'Selecione ao menos uma opção para gerar a senha')
        return
    
    if size > 300:
        messagebox.showwarning('Alerta', 'O tamanho deve ser menor que 300')
        return
    
    password = ''.join(random.choice(chars) for _ in range(size))
    senha_label.config(text=password)
    copiar_senha_button.config(state=tk.NORMAL)
    pyperclip.copy(password)
  except:
    messagebox.showerror('Erro', 'Erro ao gerar senha')

def copy():
    senha = senha_label.cget("text")
    pyperclip.copy(senha)
    messagebox.showinfo("Senha Copiada", "A senha foi copiada para a área de transferência.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senha")

# Configuração dos widgets
checkbox_letras = tk.BooleanVar()
checkbox_numeros = tk.BooleanVar()
checkbox_caracteres = tk.BooleanVar()

input_entry = ttk.Entry(root, width=30)
checkbox_letras_cb = ttk.Checkbutton(root, text="Letras", variable=checkbox_letras)
checkbox_numeros_cb = ttk.Checkbutton(root, text="Números", variable=checkbox_numeros)
checkbox_caracteres_cb = ttk.Checkbutton(root, text="Caracteres Especiais", variable=checkbox_caracteres)
gerar_senha_button = ttk.Button(root, text="Gerar Senha", command=generate, cursor="arrow")
senha_label = ttk.Label(root, text="", font=tkfont.Font(size=12), wraplength=200)
copiar_senha_button = ttk.Button(root, text="Copiar Senha", state=tk.DISABLED, command=copy)

# Posicionamento dos widgets
input_entry.pack()
checkbox_letras_cb.pack()
checkbox_numeros_cb.pack()
checkbox_caracteres_cb.pack()
gerar_senha_button.pack()
senha_label.pack()
copiar_senha_button.pack()

# Configuração de tamanho fixo e bloqueio de tela cheia e redimensionamento
root.geometry("300x400")  # Definindo tamanho fixo da janela
root.resizable(False, False)  # Bloqueando o redimensionamento da janela
root.attributes("-fullscreen", False)  # Desabilitando a tela cheia

# Iniciar loop de eventos da interface
root.mainloop()
