from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from api.models import Categoria
from api.database import engine, Base, get_db
from api.repositories.categoria_repository import CategoriaRepository
from api.schemas.categoria_schema import CategoriaRequest, CategoriaResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post(
    "/api/categoria",
    response_model=CategoriaResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(request: CategoriaRequest, db: Session = Depends(get_db)):
    categoria = CategoriaRepository.save(db, Categoria(**request.dict()))
    return CategoriaResponse.from_orm(categoria)


@app.get("/api/categoria", response_model=list[CategoriaResponse])
def find_all(db: Session = Depends(get_db)):
    categorias = CategoriaRepository.find_all(db)
    return [CategoriaResponse.from_orm(categoria) for categoria in categorias]


@app.get("/api/categoria/{id}", response_model=CategoriaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    categoria = CategoriaRepository.find_by_id(db, id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    return CategoriaResponse.from_orm(categoria)


@app.delete("/api/categoria/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CategoriaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    CategoriaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/api/categoria/{id}", response_model=CategoriaResponse)
def update(id: int, request: CategoriaRequest, db: Session = Depends(get_db)):
    if not CategoriaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )
    categoria = CategoriaRepository.save(db, Categoria(id=id, **request.dict()))
    return CategoriaResponse.from_orm(categoria)
