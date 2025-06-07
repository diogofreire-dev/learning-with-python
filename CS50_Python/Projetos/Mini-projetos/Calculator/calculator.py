import tkinter as tk
from tkinter import font

# Função para adicionar o texto do botão no display
def adicionar_no_display(texto):
    if entrada.get() == "Erro":
        entrada.delete(0, tk.END)
    entrada.insert(tk.END, texto)

# Função para calcular o resultado
def calcular():
    try:
        # Substituir símbolos visuais pelos operadores Python
        expressao = entrada.get().replace('×', '*').replace('÷', '/')
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        
        # Formatar resultado para não mostrar decimais desnecessários
        if resultado == int(resultado):
            entrada.insert(tk.END, str(int(resultado)))
        else:
            entrada.insert(tk.END, str(round(resultado, 8)))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para limpar o display
def limpar():
    entrada.delete(0, tk.END)

# Função para apagar último caractere
def apagar():
    texto_atual = entrada.get()
    if texto_atual and texto_atual != "Erro":
        entrada.delete(len(texto_atual)-1, tk.END)

# Função para efeito hover nos botões
def on_enter(button, cor_hover):
    button.configure(bg=cor_hover)

def on_leave(button, cor_original):
    button.configure(bg=cor_original)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.configure(bg="#2c3e50")
janela.geometry("400x550")
janela.resizable(False, False)

# Configurar grid responsivo
for i in range(7):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

# Definir fontes
fonte_display = font.Font(family="Segoe UI", size=28, weight="normal")
fonte_botoes = font.Font(family="Segoe UI", size=16, weight="bold")
fonte_botoes_pequenos = font.Font(family="Segoe UI", size=12, weight="bold")

# Campo de entrada
entrada = tk.Entry(janela, 
                  font=fonte_display, 
                  bd=0, 
                  justify="right",
                  bg="#34495e",
                  fg="white",
                  insertbackground="white",
                  highlightthickness=2,
                  highlightcolor="#3498db",
                  relief="flat")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=15, pady=15, ipady=20)

# Cores para diferentes tipos de botões
cores = {
    'numeros': '#34495e',
    'numeros_hover': '#4a6278',
    'operadores': '#e67e22',
    'operadores_hover': '#d35400',
    'igual': '#27ae60',
    'igual_hover': '#229954',
    'limpar': '#e74c3c',
    'limpar_hover': '#c0392b',
    'apagar': '#95a5a6',
    'apagar_hover': '#7f8c8d'
}

# Botão de apagar (backspace)
btn_apagar = tk.Button(janela, text="⌫", font=fonte_botoes_pequenos, 
                       bg=cores['apagar'], fg="white", bd=0, relief="flat",
                       command=apagar, cursor="hand2")
btn_apagar.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Botão de limpar
btn_limpar = tk.Button(janela, text="C", font=fonte_botoes, 
                       bg=cores['limpar'], fg="white", bd=0, relief="flat",
                       command=limpar, cursor="hand2")
btn_limpar.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

# Lista de botões (texto, linha, coluna, tipo)
botoes = [
    ("7", 2, 0, "numero"), ("8", 2, 1, "numero"), ("9", 2, 2, "numero"), ("÷", 2, 3, "operador"),
    ("4", 3, 0, "numero"), ("5", 3, 1, "numero"), ("6", 3, 2, "numero"), ("×", 3, 3, "operador"),
    ("1", 4, 0, "numero"), ("2", 4, 1, "numero"), ("3", 4, 2, "numero"), ("−", 4, 3, "operador"),
    ("0", 5, 0, "numero"), (".", 5, 1, "numero"), ("=", 5, 2, "igual"), ("+", 5, 3, "operador")
]

# Criar os botões
for (texto, linha, coluna, tipo) in botoes:
    if tipo == "numero":
        cor_bg = cores['numeros']
        cor_hover = cores['numeros_hover']
        cor_fg = "white"
    elif tipo == "operador":
        cor_bg = cores['operadores']
        cor_hover = cores['operadores_hover']
        cor_fg = "white"
    elif tipo == "igual":
        cor_bg = cores['igual']
        cor_hover = cores['igual_hover']
        cor_fg = "white"
    
    if texto == "=":
        btn = tk.Button(janela, text=texto, font=fonte_botoes, 
                       bg=cor_bg, fg=cor_fg, bd=0, relief="flat",
                       command=calcular, cursor="hand2")
    else:
        # Para operadores, usar símbolos visuais mas adicionar os corretos
        texto_display = texto
        if texto == "×":
            texto_adicionar = "*"
        elif texto == "÷":
            texto_adicionar = "/"
        elif texto == "−":
            texto_adicionar = "-"
        else:
            texto_adicionar = texto
            
        btn = tk.Button(janela, text=texto_display, font=fonte_botoes, 
                       bg=cor_bg, fg=cor_fg, bd=0, relief="flat",
                       command=lambda t=texto_adicionar: adicionar_no_display(t), 
                       cursor="hand2")
    
    btn.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)
    
    # Adicionar efeitos hover
    btn.bind("<Enter>", lambda e, b=btn, c=cor_hover: on_enter(b, c))
    btn.bind("<Leave>", lambda e, b=btn, c=cor_bg: on_leave(b, c))

# Adicionar efeitos hover aos botões especiais
btn_apagar.bind("<Enter>", lambda e: on_enter(btn_apagar, cores['apagar_hover']))
btn_apagar.bind("<Leave>", lambda e: on_leave(btn_apagar, cores['apagar']))

btn_limpar.bind("<Enter>", lambda e: on_enter(btn_limpar, cores['limpar_hover']))
btn_limpar.bind("<Leave>", lambda e: on_leave(btn_limpar, cores['limpar']))

# Suporte para teclado
def tecla_pressionada(event):
    tecla = event.char
    if tecla.isdigit() or tecla in "+-*/().":
        if tecla == "*":
            adicionar_no_display("×")
        elif tecla == "/":
            adicionar_no_display("÷")
        elif tecla == "-":
            adicionar_no_display("−")
        else:
            adicionar_no_display(tecla)
    elif event.keysym == "Return":
        calcular()
    elif event.keysym == "BackSpace":
        apagar()
    elif event.keysym == "Escape":
        limpar()

janela.bind('<KeyPress>', tecla_pressionada)
janela.focus_set()

# Iniciar o loop principal
janela.mainloop()