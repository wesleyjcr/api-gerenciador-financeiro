import datetime
from pydantic import BaseModel


class LancamentoBase(BaseModel):
    data: datetime.date
    descricao: str
    movimentacao: str
    data_vencimento: datetime.date
    valor: float
    id_conta: int
    id_categoria: int
    id_classificacao: int
    id_competencia: int


class LancamentoRequest(LancamentoBase):
    ...


class LancamentoResponse(LancamentoBase):
    id: int

    class Config:
        orm_mode = True
