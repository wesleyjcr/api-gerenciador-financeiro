from sqlalchemy.orm import Session

from api.models import Conta


class ContaRepository:
    @staticmethod
    def find_all(db: Session) -> list[Conta]:
        return db.query(Conta).all()

    @staticmethod
    def save(db: Session, conta: Conta) -> Conta:
        if conta.id:
            db.merge(conta)
        else:
            db.add(conta)
        db.commit()
        return conta

    @staticmethod
    def find_by_id(db: Session, id: int) -> Conta:
        return db.query(Conta).filter(Conta.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Conta).filter(Conta.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        conta = db.query(Conta).filter(Conta.id == id).first()
        if conta is not None:
            db.delete(conta)
            db.commit()
