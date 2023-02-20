import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from api.database import Base


class Competencia(Base):
    __tablename__ = "competencia"

    id: int = Column(Integer, primary_key=True)
    competencia: str = Column(String(7))
    descricao: str = Column(String(140))
    data_inicio: str = Column(DateTime)
    data_fim: str = Column(DateTime)
    criado_em: datetime.datetime = Column(
        DateTime, default=datetime.datetime.now(datetime.timezone.utc)
    )
    alterado_em: datetime.datetime = Column(
        DateTime, default=datetime.datetime.now(datetime.timezone.utc)
    )


class Conta(Base):
    __tablename__ = "conta"

    id: int = Column(Integer, primary_key=True)
    descricao: str = Column(String(140))
    saldo_inicial: float = Column(Float)


class Categoria(Base):
    __tablename__ = "categoria"

    id: int = Column(Integer, primary_key=True)
    categoria: str = Column(String(140))
    tipo: str = Column(String(50))


class Classificacao(Base):
    __tablename__ = "classificacao"

    id: int = Column(Integer, primary_key=True)
    descricao: str = Column(String(140))


class Lancamento(Base):
    __tablename__ = "lancamento"

    id: int = Column(Integer, primary_key=True)
    data: str = Column(DateTime)
    descricao: str = Column(String(140))
    movimentacao: str = Column(String(1))
    data_vencimento: str = Column(DateTime)
    valor: float = Column(Float)
    id_conta: int = Column(Integer, ForeignKey("conta.id"), nullable=False)
    id_categoria: int = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    id_classificacao: int = Column(Integer, ForeignKey("classificacao.id"), nullable=False)
    id_competencia: int = Column(Integer, ForeignKey("competencia.id"), nullable=False)
