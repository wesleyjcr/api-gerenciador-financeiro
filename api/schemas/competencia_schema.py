import datetime
from pydantic import BaseModel, validator


class CompetenciaBase(BaseModel):
    competencia: str
    descricao: str 
    data_inicio: datetime.date
    data_fim: datetime.date

    @validator('competencia')
    def year_is_good(cls, v):
        if len(v) != 4:
            raise ValueError('O ano deve estar no formato YYYY')
        return v.title()

class CompetenciaRequest(CompetenciaBase):
    ...


class CompetenciaResponse(CompetenciaBase):
    id: int

    class Config:
        orm_mode = True
