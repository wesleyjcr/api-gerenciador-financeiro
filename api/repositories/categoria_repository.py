from sqlalchemy.orm import Session

from api.models import Categoria

class CategoriaRepository:
    @staticmethod
    def find_all(db: Session) -> list[Categoria]:
        return db.query(Categoria).all()

    @staticmethod
    def save(db: Session, categoria: Categoria) -> Categoria:
        if categoria.id:
            db.merge(categoria)
        else:
            db.add(categoria)
        db.commit()
        return categoria

    @staticmethod
    def find_by_id(db: Session, id: int) -> Categoria:
        return db.query(Categoria).filter(Categoria.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Categoria).filter(Categoria.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        categoria = db.query(Categoria).filter(Categoria.id == id).first()
        if categoria is not None:
            db.delete(categoria)
            db.commit()