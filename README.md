# Projeto A4 - API com Arquitetura em Camadas, FastAPI e Nginx

## Integrante da Equipe
* [Stéfany Soares Santana]

---

## 📂 Arquitetura do Projeto
- `app/main.py`: Ponto de entrada, middlewares e registro de rotas.
- `app/core/`: Infraestrutura central e conexão SQLite (`database.py`)[cite: 3].
- `app/schemas/`: Contratos de dados e modelos Pydantic (`models.py`)[cite: 3].
- `app/repositories/`: Camada de acesso a dados (CRUD isolado)[cite: 3].
- `app/api/routes/`: Controladores modulares e endpoints (`@router`)[cite: 3].

---

## Como Executar a Aplicação (FastAPI)
1. Instale as dependências do projeto.
2. Inicie o servidor Uvicorn apontando para o módulo principal:
   ```bash
   uvicorn app.main:app --reload