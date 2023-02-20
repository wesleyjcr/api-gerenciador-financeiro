from pydantic import BaseModel


class ContaBase(BaseModel):
    descricao: str
    saldo_inicial: float


class ContaRequest(ContaBase):
    ...


class ContaResponse(ContaBase):
    id: int

    class Config:
        orm_mode = True
