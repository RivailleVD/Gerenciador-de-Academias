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
    nome TEXT PRIMARY KEY,
    inscritos INTEGER,
    datas DATE,
    medalhistas TEXT
);
"""


# Função para criar a tabela Medalhistas
def criar_tabela_medalhistas():
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medalhistas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            campeonato_id INTEGER,
            medalha TEXT,
            FOREIGN KEY (campeonato_id) REFERENCES Campeonatos(id)
        )
    ''')
    conn.commit()
    conn.close()

# Executa a criação da tabela
criar_tabela_medalhistas()

# Executar os comandos para criar as tabelas
cursor.execute(create_alunos_table)
cursor.execute(create_treinos_table)
cursor.execute(create_campeonatos_table)

# Confirmar e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados e tabelas criados com sucesso.")


