from fastapi import FastAPI, HTTPException
from models import RegistroModel
from database import init_db, get_db_connection

app = FastAPI(
    title="Projeto A4 - Arquitetura em Camadas",
    version="2.0.0"
)

# Inicializa o banco de dados ao iniciar a aplicação
init_db()

@app.post("/registros", status_code=201)
def criar_registro(registro: RegistroModel):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO registros (titulo, descricao) VALUES (?, ?)",
        (registro.titulo, registro.descricao)
    )
    conn.commit()
    reg_id = cursor.lastrowid
    conn.close()
    return {
        "id": reg_id,
        "titulo": registro.titulo,
        "descricao": registro.descricao,
        "mensagem": "Registro criado com sucesso!"
    }

@app.get("/registros")
def listar_registros():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]