from sqlalchemy.orm import Session

from api.models import Competencia


class CompetenciaRepository:
    @staticmethod
    def find_all(db: Session) -> list[Competencia]:
        return db.query(Competencia).all()

    @staticmethod
    def save(db: Session, competencia: Competencia) -> Competencia:
        if competencia.id:
            db.merge(competencia)
        else:
            db.add(competencia)
        db.commit()
        return competencia

    @staticmethod
    def find_by_id(db: Session, id: int) -> Competencia:
        return db.query(Competencia).filter(Competencia.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Competencia).filter(Competencia.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        competencia = db.query(Competencia).filter(Competencia.id == id).first()
        if competencia is not None:
            db.delete(competencia)
            db.commit()
