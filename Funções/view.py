import sqlite3


#conectar o banco de dados
def conectar():
    con = sqlite3.connect('academia.db')
    return con

# Função para inserir um aluno
def inserir_aluno(nome, idade, peso, altura, telefone, faixa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Alunos (Nome, Idade, Peso, Altura, Telefone, Faixa)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, idade, peso, altura, telefone, faixa))
    conn.commit()
    conn.close()

# Função para remover um aluno pelo ID
def remover_aluno(id_aluno):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Alunos WHERE Id = ?", (id_aluno,))
    conn.commit()
    conn.close()

# Função para editar as informações de um aluno pelo ID
def editar_aluno(id_aluno, nome=None, idade=None, peso=None, altura=None, telefone=None, faixa=None):
    conn = conectar()
    cursor = conn.cursor()
    # Atualiza apenas os campos fornecidos
    if nome:
        cursor.execute("UPDATE Alunos SET Nome = ? WHERE Id = ?", (nome, id_aluno))
    if idade:
        cursor.execute("UPDATE Alunos SET Idade = ? WHERE Id = ?", (idade, id_aluno))
    if peso:
        cursor.execute("UPDATE Alunos SET Peso = ? WHERE Id = ?", (peso, id_aluno))
    if altura:
        cursor.execute("UPDATE Alunos SET Altura = ? WHERE Id = ?", (altura, id_aluno))
    if telefone:
        cursor.execute("UPDATE Alunos SET Telefone = ? WHERE Id = ?", (telefone, id_aluno))
    if faixa:
        cursor.execute("UPDATE Alunos SET Faixa = ? WHERE Id = ?", (faixa, id_aluno))
    conn.commit()
    conn.close()


# Função para inserir um treino
def inserir_treino(dias, horario, mensalidades, status, vencimento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Treinos (dias, horario, mensalidades, status, vencimento)
        VALUES (?, ?, ?, ?, ?)
    """, (dias, horario, mensalidades, status, vencimento))
    conn.commit()
    conn.close()

# Função para remover um treino pelo nome
def remover_treino(nome_treino):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Treinos WHERE Nome = ?", (nome_treino,))
    conn.commit()
    conn.close()

# Função para editar informações de um treino pelo nome
def editar_treino(nome_treino, novo_nome=None, descricao=None, status=None):
    conn = conectar()
    cursor = conn.cursor()
    # Atualiza apenas os campos fornecidos
    if novo_nome:
        cursor.execute("UPDATE Treinos SET Nome = ? WHERE Nome = ?", (novo_nome, nome_treino))
    if descricao:
        cursor.execute("UPDATE Treinos SET Descricao = ? WHERE Nome = ?", (descricao, nome_treino))
    if status is not None:
        cursor.execute("UPDATE Treinos SET Status = ? WHERE Nome = ?", (status, nome_treino))
    conn.commit()
    conn.close()
    
    # Função para inserir um novo campeonato
# Função para inserir um campeonato
def inserir_campeonato(nome, inscritos, datas, medalhistas):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Campeonatos (nome, inscritos, datas, medalhistas)
        VALUES (?, ?, ?, ?)
    ''', (nome, inscritos, datas, medalhistas))
    conn.commit()
    conn.close()


# Função para editar um campeonato existente
def editar_campeonato(campeonato_id, nome=None, data=None, local=None, tipo=None):
    conn = conectar()
    cursor = conn.cursor()
    campos_para_atualizar = []
    valores = []

    if nome is not None:
        campos_para_atualizar.append('nome = ?')
        valores.append(nome)
    if data is not None:
        campos_para_atualizar.append('data = ?')
        valores.append(data)
    if local is not None:
        campos_para_atualizar.append('local = ?')
        valores.append(local)
    if tipo is not None:
        campos_para_atualizar.append('tipo = ?')
        valores.append(tipo)

    valores.append(campeonato_id)
    cursor.execute(f'''
        UPDATE Campeonatos
        SET {", ".join(campos_para_atualizar)}
        WHERE id = ?
    ''', valores)
    conn.commit()
    conn.close()

# Função para remover um campeonato
def remover_campeonato(campeonato_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Campeonatos WHERE id = ?', (campeonato_id,))
    conn.commit()
    conn.close()
    
# Função para inserir um novo medalhista
def inserir_medalhista(nome, categoria, campeonato_id, medalha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Medalhistas (nome, categoria, campeonato_id, medalha)
        VALUES (?, ?, ?, ?)
    ''', (nome, categoria, campeonato_id, medalha))
    conn.commit()
    conn.close()

# Função para editar um medalhista existente
def editar_medalhista(medalhista_id, nome=None, categoria=None, campeonato_id=None, medalha=None):
    conn = conectar()
    cursor = conn.cursor()
    campos_para_atualizar = []
    valores = []

    if nome is not None:
        campos_para_atualizar.append('nome = ?')
        valores.append(nome)
    if categoria is not None:
        campos_para_atualizar.append('categoria = ?')
        valores.append(categoria)
    if campeonato_id is not None:
        campos_para_atualizar.append('campeonato_id = ?')
        valores.append(campeonato_id)
    if medalha is not None:
        campos_para_atualizar.append('medalha = ?')
        valores.append(medalha)

    valores.append(medalhista_id)
    cursor.execute(f'''
        UPDATE Medalhistas
        SET {", ".join(campos_para_atualizar)}
        WHERE id = ?
    ''', valores)
    conn.commit()
    conn.close()

# Função para remover um medalhista
def remover_medalhista(medalhista_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Medalhistas WHERE id = ?', (medalhista_id,))
    conn.commit()
    conn.close()
    
    # Função para exibir todos os alunos
def exibir_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    conn.close()

    # Exibir os dados dos alunos
    for aluno in alunos:
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Idade: {aluno[2]}")
        print(f"Peso: {aluno[3]}")
        print(f"Telefone: {aluno[4]}")
        print(f"Faixa: {aluno[5]}")
        print(f"Altura: {aluno[6]}")
        print("-" * 20)



conn = sqlite3.connect('academia.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas no banco de dados:", cursor.fetchall())
conn.close()


# Função para exibir todos os treinos
def exibir_treinos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Treinos")
    treinos = cursor.fetchall()
    conn.close()

    # Exibir os dados dos treinos
    for treino in treinos:
        print(f"Dias: {treino[0]}")
        print(f"Horário: {treino[1]}")
        print(f"Mensalidades: {treino[2]}")
        print(f"Status: {'Ativo' if treino[3] else 'Inativo'}")
        print(f"Vencimento: {treino[4]}")
        print("-" * 20)

# Função para exibir os campeonatos
def exibir_campeonatos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Campeonatos")
    campeonatos = cursor.fetchall()

    if campeonatos:
        print("Campeonatos:")
        for campeonato in campeonatos:
            print(f"Nome: {campeonato[0]}, Inscritos: {campeonato[1]}, Datas: {campeonato[2]}, Medalhistas: {campeonato[3]}")
    else:
        print("Nenhum campeonato encontrado.")
    
    conn.close()
    
def exibir_medalhistas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medalhistas")
    medalhistas = cursor.fetchall()

    if medalhistas:
        print("Medalhistas:")
        for medalhista in medalhistas:
            print(f"ID: {medalhista[0]}, Nome: {medalhista[1]}, Categoria: {medalhista[2]}, Campeonato ID: {medalhista[3]}, Medalha: {medalhista[4]}")
    else:
        print("Nenhum medalhista encontrado.")

    conn.close()
    

# Chamar a função para exibir os alunos
exibir_alunos()