from sqlalchemy.orm import Session

from api.models import Classificacao


class ClassificacaoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Classificacao]:
        return db.query(Classificacao).all()

    @staticmethod
    def save(db: Session, classificacao: Classificacao) -> Classificacao:
        if classificacao.id:
            db.merge(classificacao)
        else:
            db.add(classificacao)
        db.commit()
        return classificacao

    @staticmethod
    def find_by_id(db: Session, id: int) -> Classificacao:
        return db.query(Classificacao).filter(Classificacao.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Classificacao).filter(Classificacao.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        classificacao = db.query(Classificacao).filter(Classificacao.id == id).first()
        if classificacao is not None:
            db.delete(classificacao)
            db.commit()
