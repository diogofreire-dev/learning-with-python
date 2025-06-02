import tkinter as tk

# Função para adicionar o texto do botão no display
def adicionar_no_display(texto):
    entrada.insert(tk.END, texto)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para limpar o display
def limpar():
    entrada.delete(0, tk.END)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora Python")
janela.configure(bg="#f0f0f0")

# Configurar grid responsivo
for i in range(6):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Lista de botões (texto, linha, coluna)
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Criar os botões
for (texto, linha, coluna) in botoes:
    if texto == "=":
        btn = tk.Button(janela, text=texto, font=("Arial", 18), bg="#d0ffd0", command=calcular)
    else:
        btn = tk.Button(janela, text=texto, font=("Arial", 18), bg="#ffffff", command=lambda t=texto: adicionar_no_display(t))
    btn.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

# Botão de limpar
btn_limpar = tk.Button(janela, text="C", font=("Arial", 18), bg="#ffd0d0", command=limpar)
btn_limpar.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Iniciar o loop principal
janela.mainloop()