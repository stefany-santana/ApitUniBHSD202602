import sqlite3

DB_NAME = "banco_a3.db"

def get_db_connection():
    """Retorna uma conexão ativa com o banco de dados configurada com Row factory."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Cria a tabela inicial do banco de dados caso ela não exista."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT
        )
    """)
    conn.commit()
    conn.close()