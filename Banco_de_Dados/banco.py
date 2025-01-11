import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('academia.db')
cursor = conn.cursor()

# Código SQL para criar a tabela Alunos
create_alunos_table = """
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    peso DECIMAL(5, 2),
    telefone TEXT,
    faixa TEXT,
    altura DECIMAL(5, 2)
);
"""

# Código SQL para criar a tabela Treinos
create_treinos_table = """
CREATE TABLE IF NOT EXISTS Treinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Adiciona uma coluna de ID
    dias TEXT NOT NULL,                   -- Armazena os dias em formato de texto
    horario TIME NOT NULL,                -- Horário do treino
    mensalidades DECIMAL(10, 2),          -- Valor da mensalidade
    status INTEGER NOT NULL DEFAULT 1,    -- Utiliza INTEGER (0 para inativo, 1 para ativo)
    vencimento DATE                       -- Data de vencimento
);
"""

# Código SQL para criar a tabela Campeonatos
create_campeonatos_table = """
CREATE TABLE IF NOT EXISTS Campeonatos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT
    nome TEXT PRIMARY KEY,
    inscritos INTEGER,
    datas DATE,
    medalhistas TEXT
);
"""


# Função para criar a tabela Medalhistas
import sqlite3

# Criação das tabelas
def create_campeonatos_table():
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Tabela Campeonatos
    create_campeonatos_table = '''
    CREATE TABLE IF NOT EXISTS Campeonatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        inscritos INTEGER NOT NULL,
        datas TEXT NOT NULL,
        medalhistas TEXT
    )
    '''
    cursor.execute(create_campeonatos_table)

    # Tabela Medalhistas
    create_medalhistas_table = '''
    CREATE TABLE IF NOT EXISTS Medalhistas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        campeonato_id INTEGER,
        medalha TEXT,
        FOREIGN KEY (campeonato_id) REFERENCES Campeonatos(id)
    )
    '''
    cursor.execute(create_medalhistas_table)

    # Outras tabelas (exemplo para Alunos)
    create_alunos_table = '''
    CREATE TABLE IF NOT EXISTS Alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    '''
    cursor.execute(create_alunos_table)

    conn.commit()
    conn.close()

# Executar criação
create_campeonatos_table()


# Executar os comandos para criar as tabelas
cursor.execute(create_alunos_table)
cursor.execute(create_treinos_table)
cursor.execute('''PRAGMA table_info(Campeonatos)''')
print(cursor.fetchall())


# Confirmar e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados e tabelas criados com sucesso.")


