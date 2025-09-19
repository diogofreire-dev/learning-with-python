import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Passwords Seguras")
        self.root.geometry("890x700")
        self.root.configure(bg='#f8fafc')
        self.root.resizable(False, False)

        self.colors = {
            'primary': '#2563eb',
            'secondary': '#64748b',
            'success': '#10b981',
            'danger': '#ef4444',
            'warning': '#f59e0b',
            'background': '#f8fafc',
            'card': '#ffffff',
            'text': '#1e293b',
            'text_light': '#64748b'
        }
        
        # Variáveis
        self.password_length = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=False)
        
        self.setup_ui()
        
    def setup_ui(self):
        canvas = tk.Canvas(self.root, bg=self.colors['background'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['background'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        main_frame = tk.Frame(scrollable_frame, bg=self.colors['background'])
        main_frame.pack(fill='both', expand=True, padx=30, pady=20)

        self.create_header(main_frame)
        
        # Card principal
        card_frame = tk.Frame(main_frame, bg=self.colors['card'], 
                             relief='raised', bd=1)
        card_frame.pack(fill='both', expand=True, pady=20)

        content_frame = tk.Frame(card_frame, bg=self.colors['card'])
        content_frame.pack(fill='both', expand=True, padx=30, pady=30)

        self.create_length_section(content_frame)
        self.create_options_section(content_frame)
        self.create_strength_indicator(content_frame)
        self.create_generate_section(content_frame)
        self.create_result_section(content_frame)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind("<MouseWheel>", _on_mousewheel)
        self.root.bind("<MouseWheel>", _on_mousewheel)
        
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.colors['background'])
        header_frame.pack(fill='x', pady=(0, 10))

        title = tk.Label(header_frame, text="Gerador de Passwords",
                        font=("Segoe UI", 24, "bold"),
                        fg=self.colors['text'],
                        bg=self.colors['background'])
        title.pack()
        
        subtitle = tk.Label(header_frame, text="Crie passwords seguras e personalizadas",
                           font=("Segoe UI", 11),
                           fg=self.colors['text_light'],
                           bg=self.colors['background'])
        subtitle.pack(pady=(5, 0))
        
    def create_length_section(self, parent):
        length_frame = tk.Frame(parent, bg=self.colors['card'])
        length_frame.pack(fill='x', pady=(0, 25))

        tk.Label(length_frame, text="Comprimento da Password",
                font=("Segoe UI", 12, "bold"),
                fg=self.colors['text'],
                bg=self.colors['card']).pack(anchor='w')

        slider_container = tk.Frame(length_frame, bg=self.colors['card'])
        slider_container.pack(fill='x', pady=(10, 0))
        
        # Slider
        self.length_scale = tk.Scale(slider_container, 
                                    from_=4, to=50, 
                                    orient="horizontal", 
                                    variable=self.password_length,
                                    font=("Segoe UI", 10),
                                    bg=self.colors['card'],
                                    fg=self.colors['text'],
                                    activebackground=self.colors['primary'],
                                    highlightthickness=0,
                                    troughcolor='#e2e8f0',
                                    command=self.update_strength)
        self.length_scale.pack(side='left', fill='x', expand=True)

        self.length_label = tk.Label(slider_container, 
                                    text=f"{self.password_length.get()} caracteres",
                                    font=("Segoe UI", 10, "bold"),
                                    fg=self.colors['primary'],
                                    bg=self.colors['card'])
        self.length_label.pack(side='right', padx=(10, 0))

        self.length_scale.bind('<Motion>', self.update_length_label)
        self.length_scale.bind('<ButtonRelease-1>', self.update_length_label)
        
    def create_options_section(self, parent):
        # Seção opções
        options_frame = tk.Frame(parent, bg=self.colors['card'])
        options_frame.pack(fill='x', pady=(0, 25))
        
        tk.Label(options_frame, text="Tipos de Caracteres",
                font=("Segoe UI", 12, "bold"),
                fg=self.colors['text'],
                bg=self.colors['card']).pack(anchor='w')
        
        checkbox_frame = tk.Frame(options_frame, bg=self.colors['card'])
        checkbox_frame.pack(fill='x', pady=(15, 0))
        
        self.create_checkbox(checkbox_frame, "Maiúsculas (A-Z)", 
                           self.include_uppercase, 0)
        self.create_checkbox(checkbox_frame, "Minúsculas (a-z)", 
                           self.include_lowercase, 1)
        self.create_checkbox(checkbox_frame, "Números (0-9)", 
                           self.include_numbers, 2)
        self.create_checkbox(checkbox_frame, "Símbolos (!@#$)", 
                           self.include_symbols, 3)
        
    def create_checkbox(self, parent, text, variable, row):
        cb = tk.Checkbutton(parent, text=text,
                           variable=variable,
                           font=("Segoe UI", 11),
                           fg=self.colors['text'],
                           bg=self.colors['card'],
                           activebackground=self.colors['card'],
                           selectcolor=self.colors['card'],
                           command=self.update_strength)
        cb.pack(anchor='w', pady=5)
        
    def create_strength_indicator(self, parent):
        strength_frame = tk.Frame(parent, bg=self.colors['card'])
        strength_frame.pack(fill='x', pady=(0, 25))
        
        tk.Label(strength_frame, text="Força da Password",
                font=("Segoe UI", 12, "bold"),
                fg=self.colors['text'],
                bg=self.colors['card']).pack(anchor='w')
        
        bars_container = tk.Frame(strength_frame, bg=self.colors['card'])
        bars_container.pack(fill='x', pady=(10, 0))
        
        bars_frame = tk.Frame(bars_container, bg=self.colors['card'])
        bars_frame.pack(anchor='w')
        
        self.strength_bars = []
        for i in range(4):
            bar = tk.Frame(bars_frame, bg='#e2e8f0', height=8, width=80)
            bar.pack(side='left', padx=(0, 5))
            self.strength_bars.append(bar)
        
        self.strength_label = tk.Label(strength_frame, text="Média",
                                      font=("Segoe UI", 10, "bold"),
                                      fg=self.colors['warning'],
                                      bg=self.colors['card'])
        self.strength_label.pack(anchor='w', pady=(8, 0))
        
        self.update_strength()
        
    def create_generate_section(self, parent):
        # Botão gerar
        generate_frame = tk.Frame(parent, bg=self.colors['card'])
        generate_frame.pack(fill='x', pady=(0, 25))
        
        self.generate_btn = tk.Button(generate_frame, 
                                     text="Gerar Password Segura",
                                     command=self.generate_password,
                                     font=("Segoe UI", 12, "bold"),
                                     bg=self.colors['primary'],
                                     fg='white',
                                     activebackground='#1d4ed8',
                                     activeforeground='white',
                                     relief='flat',
                                     padx=30,
                                     pady=12,
                                     cursor='hand2')
        self.generate_btn.pack(fill='x')
        
        self.generate_btn.bind('<Enter>', lambda e: self.generate_btn.configure(bg='#1d4ed8'))
        self.generate_btn.bind('<Leave>', lambda e: self.generate_btn.configure(bg=self.colors['primary']))
        
    def create_result_section(self, parent):
        # Seção resultado
        result_frame = tk.Frame(parent, bg=self.colors['card'])
        result_frame.pack(fill='x')
        
        tk.Label(result_frame, text="Password Gerada",
                font=("Segoe UI", 12, "bold"),
                fg=self.colors['text'],
                bg=self.colors['card']).pack(anchor='w')
        
        text_container = tk.Frame(result_frame, bg='#f1f5f9', relief='solid', bd=1)
        text_container.pack(fill='x', pady=(10, 0))
        
        self.result_text = tk.Text(text_container, 
                                  height=3, 
                                  font=("Consolas", 12),
                                  bg='#f1f5f9',
                                  fg=self.colors['text'],
                                  relief='flat',
                                  padx=15,
                                  pady=10,
                                  wrap='word',
                                  selectbackground=self.colors['primary'])
        self.result_text.pack(fill='both', expand=True)
        
        # Botões de ação
        buttons_frame = tk.Frame(result_frame, bg=self.colors['card'])
        buttons_frame.pack(fill='x', pady=(15, 0))
        
        # Botão copiar
        copy_btn = tk.Button(buttons_frame, 
                            text="Copiar",
                            command=self.copy_password,
                            font=("Segoe UI", 10, "bold"),
                            bg=self.colors['success'],
                            fg='white',
                            activebackground='#059669',
                            relief='flat',
                            padx=20,
                            pady=8,
                            cursor='hand2')
        copy_btn.pack(side='left')
        
        # Botão limpar
        clear_btn = tk.Button(buttons_frame,
                             text="Limpar",
                             command=self.clear_password,
                             font=("Segoe UI", 10, "bold"),
                             bg=self.colors['secondary'],
                             fg='white',
                             activebackground='#475569',
                             relief='flat',
                             padx=20,
                             pady=8,
                             cursor='hand2')
        clear_btn.pack(side='left', padx=(10, 0))
        
        copy_btn.bind('<Enter>', lambda e: copy_btn.configure(bg='#059669'))
        copy_btn.bind('<Leave>', lambda e: copy_btn.configure(bg=self.colors['success']))
        clear_btn.bind('<Enter>', lambda e: clear_btn.configure(bg='#475569'))
        clear_btn.bind('<Leave>', lambda e: clear_btn.configure(bg=self.colors['secondary']))
        
    def update_length_label(self, event=None):
        self.length_label.configure(text=f"{self.password_length.get()} caracteres")
        
    def update_strength(self, event=None):
        # Calcular força da password
        score = 0
        length = self.password_length.get()
        
        if length >= 8: score += 1
        if length >= 12: score += 1
        if length >= 16: score += 1
        
        char_types = sum([
            self.include_uppercase.get(),
            self.include_lowercase.get(),
            self.include_numbers.get(),
            self.include_symbols.get()
        ])
        
        if char_types >= 2: score += 1
        if char_types >= 3: score += 1
        if char_types >= 4: score += 1
        
        colors = ['#e2e8f0', '#ef4444', '#f59e0b', '#10b981']
        labels = ['Muito Fraca', 'Fraca', 'Média', 'Forte', 'Muito Forte']
        label_colors = ['#64748b', '#ef4444', '#f59e0b', '#10b981', '#059669']
        
        for i, bar in enumerate(self.strength_bars):
            if i < min(score, 4):
                bar.configure(bg=colors[min(score, 3)])
            else:
                bar.configure(bg='#e2e8f0')
        
        self.strength_label.configure(
            text=labels[min(score, 4)],
            fg=label_colors[min(score, 4)]
        )
        
    def generate_password(self):
        try:
            # Verificar se pelo menos uma opção está selecionada
            if not any([self.include_uppercase.get(), self.include_lowercase.get(), 
                       self.include_numbers.get(), self.include_symbols.get()]):
                messagebox.showwarning("Aviso", 
                                     "Por favor, selecione pelo menos um tipo de caractere!")
                return
            
            # Construir conjunto de caracteres
            characters = ""
            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_lowercase.get():
                characters += string.ascii_lowercase
            if self.include_numbers.get():
                characters += string.digits
            if self.include_symbols.get():
                characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            # Gerar password
            length = self.password_length.get()
            password = ''.join(random.choice(characters) for _ in range(length))
            
            # Mostrar resultado
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, password)
            
            # Efeito visual no botão
            original_text = self.generate_btn.cget('text')
            self.generate_btn.configure(text='Password Gerada!', bg=self.colors['success'])
            self.root.after(1500, lambda: self.generate_btn.configure(text=original_text, bg=self.colors['primary']))
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar password: {str(e)}")
            
    def copy_password(self):
        try:
            password = self.result_text.get(1.0, tk.END).strip()
            if password:
                self.root.clipboard_clear()
                self.root.clipboard_append(password)
                messagebox.showinfo("Sucesso", "Password copiada para a área de transferência!")
            else:
                messagebox.showwarning("Aviso", "Gere uma password primeiro!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao copiar: {str(e)}")
            
    def clear_password(self):
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()