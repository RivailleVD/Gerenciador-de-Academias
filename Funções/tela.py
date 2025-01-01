from tkinter import messagebox
from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk


from view import *
# cores
c00 = "#2e2d2b"   # Preta
c01 = "#ffffff"   # branca
c03 = "#38576b"   # valor
c04 = "#a03d3d"   # letra
c05 = "#e06636"   # - profit
c06 = "#9ea178"   
c08 = "#263238"   
c12 = "#ff0000"   # vermelho


#criando janela--------------------------
janela = Tk()
janela.title("Associação de Karatê Combate")
janela.geometry('1365x768')
janela.configure(background=c00)
janela.resizable(width=True, height=True)

style = Style(janela)
style.theme_use("clam")

#Frames ----------------------------------

frameacima = Frame(janela, width=1365, height=50, bg=c12, relief="flat")
frameacima.grid(row = 0, column=0, columnspan=2, sticky = NSEW)
app_= Label(frameacima, width=1000, compound=CENTER, padx=5, anchor=NW, font=('Verdana 25 bold'),bg=c12 ,fg=c01)
app_.place(x=50, y=0)

frameesquerda = Frame(janela, width=200, height=768, bg=c00, relief="solid")
frameesquerda.grid(row = 1, column=0, sticky = NSEW)


framedireito = Frame(janela, width=1200, height=768, bg=c01, relief="raised")
framedireito.grid(row = 1, column=1, sticky = NSEW)





def visualizar():
    def carregar_alunos():
        # Conecta ao banco de dados e obtém os dados
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Alunos")
        alunos = cursor.fetchall()
        conn.close()

        # Limpa os dados antigos do Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Insere os dados na Treeview
        for aluno in alunos:
            tree.insert("", "end", values=aluno)

    # Cabeçalho
    app_ = Label(framedireito, text="Visualizar Alunos", width=50, compound=CENTER, padx=5, pady=10,
                 font=('Verdana 12'), bg=c01, fg=c04)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(framedireito, width=1200, height=1, anchor=NW, font=('Verdana 1'), bg=c03, fg=c01)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    # Criando a tabela (Treeview)
    colunas = ["ID", "Nome", "Idade", "Peso", "Telefone", "Faixa", "Altura"]
    tree = Treeview(framedireito, columns=colunas, show="headings", height=20)
    tree.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=NSEW)

    # Configurando os cabeçalhos
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)

    # Botão para carregar os dados
    btn_carregar = Button(framedireito, text="Carregar Alunos", bg=c03, fg=c01, font=('Ivy 10 bold'),
                          command=carregar_alunos)
    btn_carregar.grid(row=3, column=0, columnspan=4, pady=10)

    # Carrega os alunos automaticamente na primeira execução
    carregar_alunos()





def novo_aluno():
    
    
    def add_aluno():
        name = app_nome_e.get()
        age = app_idade_e.get()
        weight = app_peso_e.get()
        height = app_altura_e.get()
        tel = app_telefone_e.get()
        obi = app_faixa_e.get()
        
        lista = [name, age, weight, height, tel, obi]
        
        #verificando valores vazios
        for i in lista:
            if i == '':
                messagebox.showerror('ERRO' , 'Preencha todos os campos')            
                return    
        inserir_aluno(name, age, weight, height, tel, obi)    
        messagebox.showinfo('Sucesso!' , 'Usuário inserido com Sucesso')
        #limpando os campos de entrada    
        app_nome_e.delete(0,END) 
        app_idade_e.delete(0,END) 
        app_peso_e.delete(0,END) 
        app_altura_e.delete(0,END) 
        app_altura_e.delete(0,END) 
        app_telefone_e.delete(0,END) 
        app_faixa_e.delete(0,END) 
            
            
    #nome, idade, peso, altura, telefone, faixa
    #cabeçalho
    app_ = Label(framedireito, text="Inserir Novo Aluno", width = 50, compound=CENTER, padx=5, pady=10, font=('Verdana 12'), bg=c01 , fg=c04)
    app_.grid(row=0, column=0 , columnspan=4, sticky=NSEW)
    app_linha= Label(framedireito, width=1200, height=1 , anchor=NW, font=('Verdana 1'),bg=c03,fg=c01)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    #nome
    app_nome= Label(framedireito, text='Nome Completo*', height=1 , anchor=NW, font=('Ivy 10'),bg=c01 ,fg=c04)
    app_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    app_nome_e = Entry(framedireito, width=5, justify= 'left', relief='solid')
    app_nome_e.grid(row = 2, column=1, padx=5, pady=5, sticky=NSEW)
    #idade
    app_idade= Label(framedireito, text='Idade*', height=1 , anchor=NW, font=('Ivy 10'),bg=c01 ,fg=c04)
    app_idade.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    app_idade_e = Entry(framedireito, width=15, justify= 'left', relief='solid')
    app_idade_e.grid(row = 3, column=1, padx=5, pady=5, sticky=NSEW)
    #peso
    app_peso= Label(framedireito, text='Peso*', height=1 , anchor=NW, font=('Ivy 10'),bg=c01 ,fg=c04)
    app_peso.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    app_peso_e = Entry(framedireito, width=15, justify= 'left', relief='solid')
    app_peso_e.grid(row = 4, column=1, padx=5, pady=5, sticky=NSEW)
    #altura
    app_altura= Label(framedireito, text='Altura*', height=1 , anchor=NW, font=('Ivy 10'),bg=c01 ,fg=c04)
    app_altura.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    app_altura_e = Entry(framedireito, width=15, justify= 'left', relief='solid')
    app_altura_e.grid(row = 5, column=1, padx=5, pady=5, sticky=NSEW)
    #telefone
    app_telefone= Label(framedireito, text='Telefone*', height=1 , anchor=NW, font=('Ivy 10'),bg=c01 ,fg=c04)
    app_telefone.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    app_telefone_e = Entry(framedireito, width=15, justify= 'left', relief='solid')
    app_telefone_e.grid(row = 6, column=1, padx=5, pady=5, sticky=NSEW)
    #faixa
    app_faixa= Label(framedireito, text='Faixa*', height=1 , anchor=NW, font=('Ivy 10'),bg=c01 ,fg=c04)
    app_faixa.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
    app_faixa_e = Entry(framedireito, width=15, justify= 'left', relief='solid')
    app_faixa_e.grid(row = 7, column=1, padx=5, pady=5, sticky=NSEW)
    
    #Botão Salvar
    img_save = Image.open("/home/levs/Documentos/Gestor de Academia/icons/save.png").resize((25, 25))
    img_save_tk = ImageTk.PhotoImage(img_save)

    b_save = Button(framedireito, image=img_save_tk, text='Salvar', compound="right", bg=c01, fg=c04, font=('Ivy 11'), relief=GROOVE, command=add_aluno)  # Substitua por sua função de salvar
    b_save.image = img_save_tk  # Prevenir descarte da imagem
    b_save.grid(row=9, column=1, pady=10)

#Função para controlar o Menu
def control(i):
    
    #novo aluno
    if i == 'novo_aluno':
        for widget in framedireito.winfo_children():
            widget.destroy()
            
        novo_aluno()
        
    #novo aluno
    if i == 'Visualizar':
        for widget in framedireito.winfo_children():
            widget.destroy()
            
        visualizar()
            
    
  
#Botões ----------------------------------
#Botão alunos-----------------------------
img_alunos = Image.open("/home/levs/Documentos/Gestor de Academia/icons/user_5519366.png")
img_alunos_resized = img_alunos.resize((50, 50))
img_alunos_tk = ImageTk.PhotoImage(img_alunos_resized)

b_alunos = Button(frameesquerda,command=lambda:control('Visualizar'), image=img_alunos_tk, compound=LEFT, anchor=NW, text= 'Alunos' ,bg=c00, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_alunos.grid(row = 0, column=0, sticky=NSEW, padx = 5, pady=6)

#Botão adicionar alunos
img_add = Image.open("/home/levs/Documentos/Gestor de Academia/icons/addresizible.png")
img_add_resized = img_add.resize((50, 50))
img_add_tk = ImageTk.PhotoImage(img_add_resized)

b_addalunos = Button(frameesquerda, command=lambda:control('novo_aluno'), image=img_add_tk, compound=LEFT, anchor=NW, text= 'Adicionar' ,bg=c00, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_addalunos.grid(row = 1, column=0, sticky=NSEW, padx = 5, pady=6)


#Botão campeonatos
img_trofel = Image.open("/home/levs/Documentos/Gestor de Academia/icons/trophyresizible.png")
img_trofel_resized = img_trofel.resize((50, 50))
img_trofel_tk = ImageTk.PhotoImage(img_trofel_resized)

b_campeonatos = Button(frameesquerda, image=img_trofel_tk, compound=LEFT, anchor=NE, text= 'Campeonatos' ,bg=c00, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_campeonatos.grid(row = 2, column=0, sticky=NSEW, padx = 5, pady=6)




janela.mainloop()