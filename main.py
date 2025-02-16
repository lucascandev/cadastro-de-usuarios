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

# Função para exibir o menu inicial
def exibir_menu():
    menu_janela = Toplevel(app)
    menu_janela.title("Menu")
    menu_janela.geometry("300x200")
    menu_janela.grid_rowconfigure(0, weight=1)
    menu_janela.grid_rowconfigure(5, weight=1)
    menu_janela.grid_columnconfigure(0, weight=1)
    menu_janela.grid_columnconfigure(1, weight=1)

    Label(menu_janela, text="Escolha uma opção:").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    Button(menu_janela, text="Criar Novo Cadastro", command=abrir_tela_cadastro).grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    Button(menu_janela, text="Excluir Cadastro", command=abrir_tela_exclusao).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    Button(menu_janela, text="Editar Cadastro", command=abrir_tela_edicao).grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    Button(menu_janela, text="Ver Lista de Cadastros", command=exibir_usuarios).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Função para abrir a tela de cadastro
def abrir_tela_cadastro():
    global entry_nome, entry_email, entry_telefone, entry_senha
    tela_cadastro = Toplevel(app)
    tela_cadastro.title("Cadastro de Usuários")
    tela_cadastro.geometry("400x300")
    tela_cadastro.grid_rowconfigure(0, weight=1)
    tela_cadastro.grid_rowconfigure(5, weight=1)
    tela_cadastro.grid_columnconfigure(0, weight=1)
    tela_cadastro.grid_columnconfigure(1, weight=1)

    Label(tela_cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = Entry(tela_cadastro)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    Label(tela_cadastro, text="Email:").grid(row=1, column=0, padx=10, pady=5)
    entry_email = Entry(tela_cadastro)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    Label(tela_cadastro, text="Telefone:").grid(row=2, column=0, padx=10, pady=5)
    entry_telefone = Entry(tela_cadastro)
    entry_telefone.grid(row=2, column=1, padx=10, pady=5)

    Label(tela_cadastro, text="Senha:").grid(row=3, column=0, padx=10, pady=5)
    entry_senha = Entry(tela_cadastro, show='*')
    entry_senha.grid(row=3, column=1, padx=10, pady=5)

    Button(tela_cadastro, text="Cadastrar", command=cadastrar_usuario).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Função para abrir a tela de exclusão
def abrir_tela_exclusao():
    global entry_email
    tela_exclusao = Toplevel(app)
    tela_exclusao.title("Excluir Cadastro")
    tela_exclusao.geometry("400x150")
    tela_exclusao.grid_rowconfigure(0, weight=1)
    tela_exclusao.grid_rowconfigure(2, weight=1)
    tela_exclusao.grid_columnconfigure(0, weight=1)
    tela_exclusao.grid_columnconfigure(1, weight=1)

    Label(tela_exclusao, text="Email do Usuário a Excluir:").grid(row=0, column=0, padx=10, pady=10)
    entry_email = Entry(tela_exclusao)
    entry_email.grid(row=0, column=1, padx=10, pady=10)

    Button(tela_exclusao, text="Excluir", command=excluir_usuario).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Função para abrir a tela de edição
def abrir_tela_edicao():
    global entry_nome, entry_email, entry_telefone, entry_senha
    tela_edicao = Toplevel(app)
    tela_edicao.title("Editar Cadastro")
    tela_edicao.geometry("400x300")
    tela_edicao.grid_rowconfigure(0, weight=1)
    tela_edicao.grid_rowconfigure(5, weight=1)
    tela_edicao.grid_columnconfigure(0, weight=1)
    tela_edicao.grid_columnconfigure(1, weight=1)

    Label(tela_edicao, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = Entry(tela_edicao)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    Label(tela_edicao, text="Email (para buscar):").grid(row=1, column=0, padx=10, pady=5)
    entry_email = Entry(tela_edicao)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    Label(tela_edicao, text="Telefone:").grid(row=2, column=0, padx=10, pady=5)
    entry_telefone = Entry(tela_edicao)
    entry_telefone.grid(row=2, column=1, padx=10, pady=5)

    Label(tela_edicao, text="Senha:").grid(row=3, column=0, padx=10, pady=5)
    entry_senha = Entry(tela_edicao, show='*')
    entry_senha.grid(row=3, column=1, padx=10, pady=5)

    Button(tela_edicao, text="Editar", command=editar_usuario).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Criando a interface gráfica com Tkinter
app = Tk()
app.title("Sistema de Cadastro de Usuários")
app.geometry("400x200")
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

Button(app, text="Menu Inicial", command=exibir_menu).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()  # Iniciando o loop principal da aplicação