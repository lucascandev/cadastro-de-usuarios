from tkinter import *  # Importando todos os módulos do Tkinter para criação da interface gráfica
from tkinter import messagebox  # Importando messagebox do Tkinter para exibir mensagens de alerta

# Lista para armazenar os usuários cadastrados
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = entry_nome.get()  # Obtendo o valor do campo "Nome"
    email = entry_email.get()  # Obtendo o valor do campo "Email"
    telefone = entry_telefone.get()  # Obtendo o valor do campo "Telefone"
    senha = entry_senha.get()  # Obtendo o valor do campo "Senha"

    # Verificando se todos os campos foram preenchidos
    if nome and email and telefone and senha:
        # Adicionando os dados do usuário à lista de usuários
        usuarios.append({'nome': nome, 'email': email, 'telefone': telefone, 'senha': senha})
        # Exibindo mensagem de sucesso
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    else:
        # Exibindo mensagem de alerta caso algum campo não tenha sido preenchido
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

# Função para exibir os usuários cadastrados no console
def exibir_usuarios():
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Telefone: {usuario['telefone']}")

# Criando a interface gráfica com Tkinter
app = Tk()
app.title("Cadastro de Usuários")  # Definindo o título da janela

# Adicionando os campos de entrada e seus respectivos rótulos
Label(app, text="Nome:").grid(row=0, column=0)
entry_nome = Entry(app)  # Campo de entrada para o nome
entry_nome.grid(row=0, column=1)

Label(app, text="Email:").grid(row=1, column=0)
entry_email = Entry(app)  # Campo de entrada para o email
entry_email.grid(row=1, column=1)

Label(app, text="Telefone:").grid(row=2, column=0)
entry_telefone = Entry(app)  # Campo de entrada para o telefone
entry_telefone.grid(row=2, column=1)

Label(app, text="Senha:").grid(row=3, column=0)
entry_senha = Entry(app)  # Campo de entrada para a senha
entry_senha.grid(row=3, column=1)

# Botão para cadastrar o usuário, que chama a função 'cadastrar_usuario' ao ser clicado
Button(app, text="Cadastrar", command=cadastrar_usuario).grid(row=4, columnspan=2)
# Botão para exibir os usuários cadastrados no console, que chama a função 'exibir_usuarios' ao ser clicado
Button(app, text="Exibir Usuários", command=exibir_usuarios).grid(row=5, columnspan=2)

app.mainloop()  # Iniciando o loop principal da aplicação