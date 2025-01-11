from tkinter import messagebox, simpledialog
from tkinter import ttk
from tkinter.tix import Tree
from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk

from tkinter import Button, LEFT, NSEW, NW
from PIL import Image, ImageTk
from networkx import tree_data, tree_graph


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


# Criando a janela principal
janela = Tk()
janela.title("Associação de Karatê Combate")
janela.geometry('1365x768')
janela.configure(background=c00)
janela.resizable(width=True, height=True)

style = Style(janela)
style.theme_use("clam")

# Criando os Frames ----------------------------------
frameacima = Frame(janela, relief="flat")
frameacima.grid(row=0, column=0, columnspan=2, sticky="nsew")
frameacima.grid_columnconfigure(1, weight=1)

# Adicionando o título na parte superior
app_ = Label(frameacima, width=1000, compound="center", padx=5, anchor="nw", font=('Verdana 25 bold'), bg=c12, fg=c01, text="Associação de Karatê Combate")
app_.place(x=50, y=0)

# Frame esquerdo
frameesquerda = Frame(janela, width=200, height=400, bg=c00)
frameesquerda.grid(row=1, column=0, sticky="nsew")  # Não se expande, mas ocupa o espaço necessário

# Frame direito
framedireito = Frame(janela, relief="raised", bg="lightgray")
framedireito.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Configurando as colunas e linhas para que o Frame Esquerdo não se expanda e o Frame Direito ocupe o restante do espaço
janela.grid_columnconfigure(0, weight=0)  # A coluna do frame esquerdo não se expande
janela.grid_columnconfigure(1, weight=1)  # A coluna do frame direito se expande para ocupar o restante do espaço
janela.grid_rowconfigure(1, weight=1)  # A linha 1 vai expandir para preencher a altura

# Centralizando o conteúdo dentro do Frame Direito com pack()
label_centralizado = Label(framedireito, text="Conteúdo Centralizado", bg="lightgreen", font=("Arial", 16))
label_centralizado.pack(expand=True, anchor="center", padx=20, pady=20)



#Botões laterais ----------------------------------
#Botão alunos-----------------------------
img_alunos = Image.open("/home/levs/Documentos/Gestor de Academia/icons/user_5519366.png")
img_alunos_resized = img_alunos.resize((50, 50))
img_alunos_tk = ImageTk.PhotoImage(img_alunos_resized)

b_alunos = Button(frameesquerda,command=lambda:control('Visualizar'), image=img_alunos_tk, compound=LEFT, anchor=NW, text= 'Alunos' ,bg=c00, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_alunos.grid(row = 0, column=0, sticky=NSEW, padx = 5, pady=6)

#Botão adicionar alunos
#mg_add = Image.open("/home/levs/Documentos/Gestor de Academia/icons/addresizible.png")
#img_add_resized = img_add.resize((50, 50))
#img_add_tk = ImageTk.PhotoImage(img_add_resized)

#b_addalunos = Button(frameesquerda, command=lambda:control('novo_aluno'), image=img_add_tk, compound=LEFT, anchor=NW, text= 'Adicionar' ,bg=c00, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
#b_addalunos.grid(row = 1, column=0, sticky=NSEW, padx = 5, pady=6)


# Carregar imagem
try:
    img_trofel = Image.open("/home/levs/Documentos/Gestor de Academia/icons/trophyresizible.png")
    img_trofel_resized = img_trofel.resize((50, 50))
    img_trofel_tk = ImageTk.PhotoImage(img_trofel_resized)
except Exception as e:
    print(f"Erro ao carregar imagem: {e}")
    img_trofel_tk = None

# Função para gerenciar campeonatos
def gerenciar_campeonatos():
    def carregar_campeonatos():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT ID, nome, inscritos, datas, medalhistas FROM Campeonatos")
            campeonatos = cursor.fetchall()
            conn.close()

            for item in tree.get_children():
                tree.delete(item)

            for campeonato in campeonatos:
                tree.insert("", "end", values=campeonato)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar campeonatos: {e}")

    def adicionar_campeonato():
        nome = entry_nome.get().strip()
        inscritos = entry_inscritos.get().strip()
        datas = entry_datas.get().strip()
        medalhistas = entry_medalhistas.get().strip()

        if not nome or not inscritos or not datas or not medalhistas:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        if not inscritos.isdigit():
            messagebox.showerror("Erro", "Inscritos deve ser um número válido!")
            return

        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Campeonatos (nome, inscritos, datas, medalhistas) VALUES (?, ?, ?, ?)",
                (nome, inscritos, datas, medalhistas),
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Campeonato adicionado com sucesso!")
            carregar_campeonatos()
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar campeonato: {e}")

    def editar_campeonato():
        selecionado = tree.selection()
        print("Selecionado:", selecionado)
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum campeonato selecionado!")
            return

        try:
            valores = tree.item(selecionado[0])["values"]
            print("Valores recuperados:", valores)
            if not valores:
                messagebox.showerror("Erro", "Erro ao recuperar os valores do campeonato!")
                return
        except IndexError:
            messagebox.showerror("Erro", "Nenhum item válido selecionado!")
            return

        id_camp = valores[0]
        nome = entry_nome.get().strip()
        inscritos = entry_inscritos.get().strip()
        datas = entry_datas.get().strip()
        medalhistas = entry_medalhistas.get().strip()

        print("Campos preenchidos:")
        print("Nome:", nome)
        print("Inscritos:", inscritos)
        print("Datas:", datas)
        print("Medalhistas:", medalhistas)

        if not nome or not inscritos or not datas or not medalhistas:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        if not inscritos.isdigit():
            messagebox.showerror("Erro", "Inscritos deve ser um número válido!")
            return
        try:
            conn = conectar()
            cursor = conn.cursor()
            print(f"Atualizando ID: {id_camp}, Nome: {nome}, Inscritos: {inscritos}, Datas: {datas}, Medalhistas: {medalhistas}")
            cursor.execute(
                "UPDATE Campeonatos SET nome = ?, inscritos = ?, datas = ?, medalhistas = ? WHERE ID = ?",
                (nome, inscritos, datas, medalhistas, id_camp),
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Campeonato atualizado com sucesso!")
            carregar_campeonatos()
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar campeonato: {e}")


    def excluir_campeonato():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum campeonato selecionado!")
            return

        valores = tree.item(selecionado)["values"]
        id_camp = valores[0]

        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Campeonatos WHERE id = ?", (id_camp,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Campeonato excluído com sucesso!")
            carregar_campeonatos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir campeonato: {e}")

    def limpar_campos():
        entry_nome.delete(0, END)
        entry_inscritos.delete(0, END)
        entry_datas.delete(0, END)
        entry_medalhistas.delete(0, END)

    # Interface do Frame Direito
    for widget in framedireito.winfo_children():
        widget.destroy()

    app_ = Label(framedireito, text="Gerenciar Campeonatos", font=("Verdana", 12), bg=c01, fg=c04)
    app_.grid(row=0, column=1, columnspan=4, pady=5)

    # Campos para Adicionar Campeonato
    Label(framedireito, text="Nome", bg=c01, fg=c04).grid(row=1, column=0, padx=5, pady=5, sticky=W)
    entry_nome = Entry(framedireito, width=15, relief='solid')
    entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="e")

    Label(framedireito, text="Inscritos", bg=c01, fg=c04).grid(row=2, column=0, padx=5, pady=5, sticky=W)
    entry_inscritos = Entry(framedireito, width=15,  relief='solid')
    entry_inscritos.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    Label(framedireito, text="Datas", bg=c01, fg=c04).grid(row=3, column=0, padx=5, pady=5, sticky=W)
    entry_datas = Entry(framedireito, width=15,  relief='solid')
    entry_datas.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    Label(framedireito, text="Medalhistas", bg=c01, fg=c04).grid(row=4, column=0, padx=5, pady=5, sticky=W)
    entry_medalhistas = Entry(framedireito, width=15, relief='solid')
    entry_medalhistas.grid(row=4, column=1, padx=5, pady=5, sticky="e")

    Button(framedireito, text="Adicionar", bg=c03, fg=c01, command=adicionar_campeonato).grid(row=5, column=0, pady=5)
    Button(framedireito, text="Editar", bg=c04, fg=c01, command=editar_campeonato).grid(row=5, column=1, pady=5)
    Button(framedireito, text="Excluir", bg="red", fg="white", command=excluir_campeonato).grid(row=5, column=2, pady=5)

    # Tabela para Visualizar Campeonatos
    colunas = ["ID", "Nome", "Inscritos", "Datas", "Medalhistas"]
    tree = Treeview(framedireito, columns=colunas, show="headings", height=15)
    tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    carregar_campeonatos()

# Adicionar Botão Campeonatos
b_campeonatos = Button(
    frameesquerda,
    command=gerenciar_campeonatos,
    image=img_trofel_tk,
    compound=LEFT,
    text="Campeonatos",
    bg=c00,
    fg=c01,
    font=("Ivy", 11),
    relief=GROOVE,
)
b_campeonatos.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)





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



    # Carregar imagem para o botão "Adicionar Alunos"
    from PIL import Image, ImageTk

    img_add = Image.open("/home/levs/Documentos/Gestor de Academia/icons/addresizible.png")
    img_add_resized = img_add.resize((30, 30))  # Reduzindo o tamanho da imagem
    img_add_tk = ImageTk.PhotoImage(img_add_resized)

    # Botão para adicionar alunos
    b_addalunos = Button(
        framedireito,
        command=lambda: control('novo_aluno'),
        
        text='Adicionar',
        compound=LEFT,  # Combina texto e imagem
        anchor=W,  # Alinha o conteúdo à esquerda
        bg=c03,
        fg=c01,
        font=('Ivy 10 bold')
    )
    b_addalunos.image = img_add_tk  # Mantém a referência da imagem
    b_addalunos.grid(row=3, column=0, padx=10, pady=5)  # Botão na coluna 0
    #botão editar
    Button(
    framedireito,
    text="Editar", 
    bg=c04, 
    fg=c01,
    compound=LEFT,
    anchor=W,
    command=lambda: editar_aluno()
).grid(row=3, column=1, pady=5)

    # Botão para carregar aluno
    btn_carregar = Button(
        framedireito,
        text="Carregar Alunos",
        compound=LEFT,
        
        command=carregar_alunos,  # Certifique-se de passar a referência, sem parênteses
        bg=c04,
        fg=c01,
        font=('Ivy 10 bold'),
        anchor=W  # Alinha o texto à esquerda
    )
    btn_carregar.grid(row=3, column=2, padx=10, pady=5)  # Botão na coluna 1

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
    
    def editar_aluno():
        add_aluno()
        tree = ttk.Treeview(...)  # Definição do Treeview

        selecionado = tree.selection()  # Certifique-se de usar a variável correta para o Treeview
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum aluno selecionado!")
            return

        valores = tree.item(selecionado[0])["values"]
        if not valores:
            messagebox.showerror("Erro", "Erro ao recuperar os valores do aluno!")
            return

        id_aluno = valores[0]
        nome = valores[1]
        idade = valores[2]
        peso = valores[3]
        altura = valores[4]
        telefone = valores[5]
        faixa = valores[6]

        # Aqui você pode criar uma janela para editar os dados ou preencher campos de entrada existentes.
        # Exemplo simplificado:
        nome_editado = simpledialog.askstring("Editar Nome", "Nome:", initialvalue=nome)
        if not nome_editado:
            return  # Cancelado pelo usuário

        # Atualizar no banco de dados
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Alunos SET 
                nome = ?, 
                idade = ?, 
                peso = ?, 
                altura = ?, 
                telefone = ?, 
                faixa = ? 
                WHERE ID = ?
                """,
                (nome_editado, idade, peso, altura, telefone, faixa, id_aluno),
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
            carregar_alunos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar aluno: {e}")
            
        frame_edicao = Toplevel()
        frame_edicao.title("Editar Aluno")
        
        Label(frame_edicao, text="Nome").grid(row=0, column=0)
        entry_nome = Entry(frame_edicao)
        entry_nome.grid(row=0, column=1)
        entry_nome.insert(0, valores[1])

        Label(frame_edicao, text="Idade").grid(row=1, column=0)
        entry_idade = Entry(frame_edicao)
        entry_idade.grid(row=1, column=1)
        entry_idade.insert(0, valores[2])

        Label(frame_edicao, text="Peso").grid(row=2, column=0)
        entry_peso = Entry(frame_edicao)
        entry_peso.grid(row=2, column=1)
        entry_peso.insert(0, valores[3])

        Label(frame_edicao, text="Altura").grid(row=3, column=0)
        entry_altura = Entry(frame_edicao)
        entry_altura.grid(row=3, column=1)
        entry_altura.insert(0, valores[4])

        Label(frame_edicao, text="Telefone").grid(row=4, column=0)
        entry_telefone = Entry(frame_edicao)
        entry_telefone.grid(row=4, column=1)
        entry_telefone.insert(0, valores[5])

        Label(frame_edicao, text="Faixa").grid(row=5, column=0)
        entry_faixa = Entry(frame_edicao)
        entry_faixa.grid(row=5, column=1)
        entry_faixa.insert(0, valores[6])

        Button(frame_edicao, text="Salvar", command=salvar_edicao).grid(row=6, column=0, columnspan=2)


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
        
        
     #novo aluno
    if i == 'carregar_campeonatos':
        for widget in framedireito.winfo_children():
            widget.destroy()
            
        gerenciar_campeonatos()
        
    if i == 'Editar':
        for widget in framedireito.winfo_children():
            widget.destroy()
            
        editar_aluno()
            
            
    







janela.mainloop()