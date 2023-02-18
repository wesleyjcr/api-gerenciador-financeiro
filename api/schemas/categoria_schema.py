from pydantic import BaseModel


class CategoriaBase(BaseModel):
    categoria: str
    tipo: str


class CategoriaRequest(CategoriaBase):
    ...


class CategoriaResponse(CategoriaBase):
    id: int

    class Config:
        orm_mode = True
