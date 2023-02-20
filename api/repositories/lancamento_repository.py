from sqlalchemy.orm import Session

from api.models import Lancamento


class LancamentoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Lancamento]:
        return db.query(Lancamento).all()

    @staticmethod
    def save(db: Session, lancamento: Lancamento) -> Lancamento:
        if lancamento.id:
            db.merge(lancamento)
        else:
            db.add(lancamento)
        db.commit()
        return lancamento

    @staticmethod
    def find_by_id(db: Session, id: int) -> Lancamento:
        return db.query(Lancamento).filter(Lancamento.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Lancamento).filter(Lancamento.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        lancamento = db.query(Lancamento).filter(Lancamento.id == id).first()
        if lancamento is not None:
            db.delete(lancamento)
            db.commit()
