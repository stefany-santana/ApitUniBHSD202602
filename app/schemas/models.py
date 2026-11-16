from pydantic import BaseModel

class RegistroModel(BaseModel):
    titulo: str
    descricao: str = None