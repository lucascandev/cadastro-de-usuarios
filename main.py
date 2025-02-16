from tkinter import *
from tkinter import messagebox

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
    else:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

# Função para exibir os usuários cadastrados em uma nova janela
def exibir_usuarios():
    nova_janela = Toplevel(app)
    nova_janela.title("Usuários Cadastrados")
    nova_janela.geometry("600x400")

    for i, usuario in enumerate(usuarios):
        Label(nova_janela, text=f"Nome: {usuario['nome']}").grid(row=i, column=0, sticky=W, padx=10, pady=5)
        Label(nova_janela, text=f"Email: {usuario['email']}").grid(row=i, column=1, sticky=W, padx=10, pady=5)
        Label(nova_janela, text=f"Telefone: {usuario['telefone']}").grid(row=i, column=2, sticky=W, padx=10, pady=5)

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
            return

    messagebox.showwarning("Erro", "Usuário não encontrado!")

# Função para excluir um usuário cadastrado
def excluir_usuario():
    email = entry_email.get()

    for usuario in usuarios:
        if usuario['email'] == email:
            usuarios.remove(usuario)
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
            return

    messagebox.showwarning("Erro", "Usuário não encontrado!")

# Criando a interface gráfica com Tkinter
app = Tk()
app.title("Sistema de Cadastro de Usuários")
app.geometry("500x400")
app.configure(bg='#f0f0f0')

# Título
Label(app, text="Sistema de Cadastro de Usuários", font=("Helvetica", 16, "bold"), bg='#f0f0f0', fg='#333').pack(pady=10)

# Campos de entrada
frame = Frame(app, bg='#f0f0f0')
frame.pack(pady=20)

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
button_frame.pack(pady=20)

Button(button_frame, text="Cadastrar", command=cadastrar_usuario, bg='#4CAF50', fg='white', width=15).grid(row=0, column=0, padx=10)
Button(button_frame, text="Excluir", command=excluir_usuario, bg='#f44336', fg='white', width=15).grid(row=0, column=1, padx=10)
Button(button_frame, text="Editar", command=editar_usuario, bg='#2196F3', fg='white', width=15).grid(row=1, column=0, padx=10, pady=10)
Button(button_frame, text="Ver Cadastros", command=exibir_usuarios, bg='#FF9800', fg='white', width=15).grid(row=1, column=1, padx=10, pady=10)

# Créditos
Label(app, text="Criado por lucascandev", font=("Helvetica", 10), bg='#f0f0f0', fg='#333').pack(side=LEFT, padx=10, pady=10)
Label(app, text="GitHub: https://github.com/lucascandev", font=("Helvetica", 10), bg='#f0f0f0', fg='#333').pack(side=RIGHT, padx=10, pady=10)

app.mainloop()