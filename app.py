import customtkinter as ctk
#import mysql.connector as mysql



#leo para rodar o login ai na sua máquina a versão do python tem que ser:  Python 3.13 :)


# Configuração aparência
ctk.set_appearance_mode('dark')


#Criação das funções de funcinalidades e talvez para testar o banco de dadoa
def validar_login():
    usuario= campo_usuario.get()
    senha = campo_senha.get()



    #pode ser verificado no banco de dados ou em outro lugar
    #Vericação do login 
    if usuario == 'admin' and senha == '123':
        resultado_login.configure(text= 'Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')
 
#Criação da janela princial
app= ctk.CTk()
app.title('Sistema de login')
app.geometry('300x300')
#Criação dos campos 
#Label
label_usuario=ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

#Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite o seu usuário')
campo_usuario.pack(pady = 10)

#Label

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

#Entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite a sua senha', show='*')
campo_senha.pack(pady = 10)
#Button
botao_login=ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)
#campo feedback de login 
resultado_login =ctk.CTkLabel(app, text= '')
resultado_login.pack(pady=10)



# Inicia o loop da aplicação
app.mainloop()


