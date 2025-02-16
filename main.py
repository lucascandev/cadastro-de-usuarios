from tkinter import *
from tkinter import messagebox
import webbrowser
import re

# Lista para armazenar os usuários cadastrados
usuarios = []

# Função para validar o formato do e-mail
def validar_email(email):
    # Expressão regular para validar e-mails mais comuns
    padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao_email, email) is not None

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    senha = entry_senha.get()

    # Verificar se o e-mail é válido
    if not validar_email(email):
        messagebox.showwarning("Erro", "O e-mail inserido não é válido!")
        return

    # Verificar se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        messagebox.showwarning("Erro", "A senha deve ter pelo menos 8 caracteres!")
        return

    # Verificar se o e-mail já foi cadastrado
    for usuario in usuarios:
        if usuario['email'] == email:
            messagebox.showwarning("Erro", "Este e-mail já está cadastrado!")
            return

    if nome and email and telefone and senha:
        usuarios.append({'nome': nome, 'email': email, 'telefone': telefone, 'senha': senha})
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        atualizar_dashboard()
        limpar_entradas()  # Limpar as entradas após cadastro
        atualizar_contagem_senha()  # Resetar a contagem de caracteres da senha
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

    if not usuarios:  # Se não houver cadastros
        label = Label(dashboard_frame, text="Não há usuários cadastrados.", bg='#f0f0f0', fg='#333')
        label.pack(anchor=W, padx=5, pady=10)
        return

    for usuario in usuarios:
        label = Label(dashboard_frame, text=usuario['email'], bg='#f0f0f0', fg='#333')
        label.pack(anchor=W, padx=5, pady=2)
        label.bind("<Button-1>", lambda event, usuario=usuario: selecionar_email(event, usuario))

# Função para selecionar visualmente um e-mail
def selecionar_email(event, usuario):
    # Remover destaque de todos os e-mails
    for widget in dashboard_frame.winfo_children():
        widget.config(bg='#f0f0f0')

    # Destacar o e-mail selecionado
    event.widget.config(bg='#e0e0e0')
    preencher_entradas(usuario)

# Função para preencher as entradas com os dados do usuário
def preencher_entradas(usuario):
    entry_nome.delete(0, END)
    entry_email.delete(0, END)
    entry_telefone.delete(0, END)
    entry_senha.delete(0, END)

    entry_nome.insert(0, usuario['nome'])
    entry_email.insert(0, usuario['email'])
    entry_telefone.insert(0, usuario['telefone'])
    entry_senha.insert(0, usuario['senha'])

    atualizar_contagem_senha()  # Atualiza a contagem de caracteres da senha

# Função para limpar as entradas de texto
def limpar_entradas():
    entry_nome.delete(0, END)
    entry_email.delete(0, END)
    entry_telefone.delete(0, END)
    entry_senha.delete(0, END)

    atualizar_contagem_senha()  # Resetar a contagem de caracteres da senha

# Função para editar um usuário cadastrado
def editar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    senha = entry_senha.get()

    # Verificar se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        messagebox.showwarning("Erro", "A senha deve ter pelo menos 8 caracteres!")
        return

    for usuario in usuarios:
        if usuario['email'] == email:
            usuario['nome'] = nome
            usuario['telefone'] = telefone
            usuario['senha'] = senha
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            if dashboard_frame.winfo_ismapped():
                atualizar_dashboard()
            limpar_entradas()  # Limpar as entradas após editar
            atualizar_contagem_senha()  # Resetar a contagem de caracteres da senha
            return

    messagebox.showwarning("Erro", "Usuário não encontrado!")

# Função para excluir um usuário cadastrado
def excluir_usuario():
    email = entry_email.get()

    # Confirmar exclusão
    resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir este usuário?")
    if resposta:
        for usuario in usuarios:
            if usuario['email'] == email:
                usuarios.remove(usuario)
                messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
                if dashboard_frame.winfo_ismapped():
                    atualizar_dashboard()
                limpar_entradas()  # Limpar as entradas após excluir
                atualizar_contagem_senha()  # Resetar a contagem de caracteres da senha
                return

        messagebox.showwarning("Erro", "Usuário não encontrado!")

# Função para atualizar a contagem de caracteres da senha
def atualizar_contagem_senha(event=None):
    senha = entry_senha.get()
    label_contagem_senha.config(text=f"Caracteres: {len(senha)} / 8")
    if len(senha) >= 8:
        label_contagem_senha.config(fg='green')
    else:
        label_contagem_senha.config(fg='red')

# Função para abrir o link do GitHub
def abrir_github(event):
    webbrowser.open_new(r"https://github.com/lucascandev")

# Função para mostrar ou esconder os campos de cadastro
def alternar_entrada():
    if frame_entradas.winfo_ismapped():
        frame_entradas.pack_forget()  # Esconde os campos
        button_mostrar_entradas.config(text="Mostrar Entradas")
    else:
        frame_entradas.pack(pady=20, side=LEFT, padx=20)  # Exibe os campos
        button_mostrar_entradas.config(text="Ocultar Entradas")

# Função para visualizar um cadastro específico
def visualizar_usuario(event, usuario):
    # Cria uma nova janela de visualização
    janela_visualizacao = Toplevel(app)
    janela_visualizacao.title("Visualização de Cadastro")
    janela_visualizacao.geometry("400x300")
    janela_visualizacao.configure(bg='#f0f0f0')

    Label(janela_visualizacao, text="Nome: " + usuario['nome'], bg='#f0f0f0', fg='#333').pack(pady=10)
    Label(janela_visualizacao, text="Email: " + usuario['email'], bg='#f0f0f0', fg='#333').pack(pady=10)
    Label(janela_visualizacao, text="Telefone: " + usuario['telefone'], bg='#f0f0f0', fg='#333').pack(pady=10)
    Label(janela_visualizacao, text="Senha: " + usuario['senha'], bg='#f0f0f0', fg='#333').pack(pady=10)

    # Botão de retorno
    Button(janela_visualizacao, text="Voltar para Cadastros", command=janela_visualizacao.destroy, bg='#FF9800', fg='white').pack(pady=20)

# Criando a interface gráfica com Tkinter
app = Tk()
app.title("Sistema de Cadastro de Usuários")
app.geometry("1000x600")
app.configure(bg='#f0f0f0')

# Título
Label(app, text="Sistema de Cadastro de Usuários", font=("Helvetica", 18, "bold"), bg='#FF9800', fg='white').pack(pady=20, fill=X)

# Frame para as entradas (oculto inicialmente)
frame_entradas = Frame(app, bg='#f0f0f0')

Label(frame_entradas, text="Nome:", bg='#f0f0f0', fg='#333', font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
entry_nome = Entry(frame_entradas, width=40, font=("Helvetica", 12))
entry_nome.grid(row=0, column=1, padx=10, pady=5)

Label(frame_entradas, text="Email:", bg='#f0f0f0', fg='#333', font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
entry_email = Entry(frame_entradas, width=40, font=("Helvetica", 12))
entry_email.grid(row=1, column=1, padx=10, pady=5)

Label(frame_entradas, text="Telefone:", bg='#f0f0f0', fg='#333', font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5)
entry_telefone = Entry(frame_entradas, width=40, font=("Helvetica", 12))
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

Label(frame_entradas, text="Senha:", bg='#f0f0f0', fg='#333', font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5)
entry_senha = Entry(frame_entradas, width=40, font=("Helvetica", 12), show='*')
entry_senha.grid(row=3, column=1, padx=10, pady=5)

label_contagem_senha = Label(frame_entradas, text="Caracteres: 0 / 8", bg='#f0f0f0', fg='red', font=("Helvetica", 10))
label_contagem_senha.grid(row=4, column=1, padx=10, pady=5, sticky=W)

# Atualiza a contagem ao digitar
entry_senha.bind("<KeyRelease>", atualizar_contagem_senha)

# Botões
button_frame = Frame(app, bg='#f0f0f0')
button_frame.pack(pady=20, side=LEFT, padx=20, fill=Y)

Button(button_frame, text="Cadastrar", command=cadastrar_usuario, bg='#4CAF50', fg='white', width=20, height=2).grid(row=0, column=0, padx=10, pady=10)
Button(button_frame, text="Excluir", command=excluir_usuario, bg='#f44336', fg='white', width=20, height=2).grid(row=1, column=0, padx=10, pady=10)
Button(button_frame, text="Editar", command=editar_usuario, bg='#2196F3', fg='white', width=20, height=2).grid(row=2, column=0, padx=10, pady=10)

# Novo botão para mostrar ou esconder as entradas de cadastro
button_mostrar_entradas = Button(button_frame, text="Mostrar Entradas", command=alternar_entrada, bg='#FF9800', fg='white', width=20, height=2)
button_mostrar_entradas.grid(row=3, column=0, padx=10, pady=10)

# Botão para alternar a exibição do dashboard
button_ver_cadastros = Button(button_frame, text="Ver Cadastros", command=alternar_dashboard, bg='#FF9800', fg='white', width=20, height=2)
button_ver_cadastros.grid(row=4, column=0, padx=10, pady=10)

# Dashboard
dashboard_frame = Frame(app, bg='#f0f0f0', bd=2, relief="sunken", width=300, height=300)

# Créditos
creditos_frame = Frame(app, bg='#f0f0f0')
creditos_frame.pack(fill=X, side=BOTTOM, pady=10)

Label(creditos_frame, text="Criado por lucascandev", font=("Helvetica", 12), bg='#f0f0f0', fg='#333').pack(pady=5)
link_label = Label(creditos_frame, text="GitHub: https://github.com/lucascandev", font=("Helvetica", 12), bg='#f0f0f0', fg='blue', cursor="hand2")
link_label.pack(pady=5)
link_label.bind("<Button-1>", abrir_github)

app.mainloop()
