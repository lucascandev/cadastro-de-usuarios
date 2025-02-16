from tkinter import *
from tkinter import messagebox
import webbrowser

# Lista para armazenar os usuários cadastrados
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    senha = entry_senha.get()

    if nome and email and telefone and senha:
        usuarios.append({'nome': nome, 'email': email, 'telefone': telefone, 'senha': senha})
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        atualizar_dashboard()
    else:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

# Função para exibir/ocultar o painel de usuários cadastrados
def alternar_dashboard():
    if dashboard_frame.winfo_ismapped():
        dashboard_frame.pack_forget()
        button_ver_cadastros.config(text="Ver Cadastros")
    else:
        dashboard_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
        atualizar_dashboard()
        button_ver_cadastros.config(text="Fechar Cadastros")

# Função para atualizar o dashboard com a lista de e-mails
def atualizar_dashboard():
    for widget in dashboard_frame.winfo_children():
        widget.destroy()

    for usuario in usuarios:
        Label(dashboard_frame, text=usuario['email'], bg='#f0f0f0', fg='#333').pack(anchor=W, padx=5, pady=2)

# Função para editar um usuário cadastrado
def editar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    senha = entry_senha.get()

    for usuario in usuarios:
        if usuario['email'] == email:
            usuario['nome'] = nome
            usuario['telefone'] = telefone
            usuario['senha'] = senha
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            if dashboard_frame.winfo_ismapped():
                atualizar_dashboard()
            return

    messagebox.showwarning("Erro", "Usuário não encontrado!")

# Função para excluir um usuário cadastrado
def excluir_usuario():
    email = entry_email.get()

    for usuario in usuarios:
        if usuario['email'] == email:
            usuarios.remove(usuario)
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
            if dashboard_frame.winfo_ismapped():
                atualizar_dashboard()
            return

    messagebox.showwarning("Erro", "Usuário não encontrado!")

# Função para abrir o link do GitHub
def abrir_github(event):
    webbrowser.open_new(r"https://github.com/lucascandev")

# Criando a interface gráfica com Tkinter
app = Tk()
app.title("Sistema de Cadastro de Usuários")
app.geometry("900x500")
app.configure(bg='#f0f0f0')

# Título
Label(app, text="Sistema de Cadastro de Usuários", font=("Helvetica", 16, "bold"), bg='#f0f0f0', fg='#333').pack(pady=10)

# Campos de entrada
frame = Frame(app, bg='#f0f0f0')
frame.pack(pady=20, side=LEFT, padx=20)

Label(frame, text="Nome:", bg='#f0f0f0', fg='#333').grid(row=0, column=0, padx=10, pady=5)
entry_nome = Entry(frame, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

Label(frame, text="Email:", bg='#f0f0f0', fg='#333').grid(row=1, column=0, padx=10, pady=5)
entry_email = Entry(frame, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

Label(frame, text="Telefone:", bg='#f0f0f0', fg='#333').grid(row=2, column=0, padx=10, pady=5)
entry_telefone = Entry(frame, width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

Label(frame, text="Senha:", bg='#f0f0f0', fg='#333').grid(row=3, column=0, padx=10, pady=5)
entry_senha = Entry(frame, width=30, show='*')
entry_senha.grid(row=3, column=1, padx=10, pady=5)

# Botões
button_frame = Frame(app, bg='#f0f0f0')
button_frame.pack(pady=20, side=LEFT, padx=20)

Button(button_frame, text="Cadastrar", command=cadastrar_usuario, bg='#4CAF50', fg='white', width=15).grid(row=0, column=0, padx=10)
Button(button_frame, text="Excluir", command=excluir_usuario, bg='#f44336', fg='white', width=15).grid(row=0, column=1, padx=10)
Button(button_frame, text="Editar", command=editar_usuario, bg='#2196F3', fg='white', width=15).grid(row=1, column=0, padx=10, pady=10)
button_ver_cadastros = Button(button_frame, text="Ver Cadastros", command=alternar_dashboard, bg='#FF9800', fg='white', width=15)
button_ver_cadastros.grid(row=1, column=1, padx=10, pady=10)

# Dashboard
dashboard_frame = Frame(app, bg='#f0f0f0', bd=2, relief="sunken", width=300, height=300)

# Créditos
creditos_frame = Frame(app, bg='#f0f0f0')
creditos_frame.pack(fill=X, side=BOTTOM, pady=10)

Label(creditos_frame, text="Criado por lucascandev", font=("Helvetica", 10), bg='#f0f0f0', fg='#333').pack(pady=5)
link_label = Label(creditos_frame, text="GitHub: https://github.com/lucascandev", font=("Helvetica", 10), bg='#f0f0f0', fg='blue', cursor="hand2")
link_label.pack(pady=5)
link_label.bind("<Button-1>", abrir_github)

app.mainloop()