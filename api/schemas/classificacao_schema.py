from pydantic import BaseModel


class ClassificacaoBase(BaseModel):
    descricao: str


class ClassificacaoRequest(ClassificacaoBase):
    ...


class ClassificacaoResponse(ClassificacaoBase):
    id: int

    class Config:
        orm_mode = True
