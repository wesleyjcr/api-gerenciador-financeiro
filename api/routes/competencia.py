from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from api.models import Competencia
from api.schemas.competencia_schema import CompetenciaRequest, CompetenciaResponse
from api.database import get_db
from api.repositories.competencia_repository import CompetenciaRepository

def init_routes(app):

    @app.post(
        "/api/competencia",
        response_model=CompetenciaResponse,
        status_code=status.HTTP_201_CREATED,
    )
    def create(request: CompetenciaRequest, db: Session = Depends(get_db)):
        competencia = CompetenciaRepository.save(db, Competencia(**request.dict()))
        return CompetenciaResponse.from_orm(competencia)


    @app.get("/api/competencia", response_model=list[CompetenciaResponse])
    def find_all(db: Session = Depends(get_db)):
        competencias = CompetenciaRepository.find_all(db)
        return [CompetenciaResponse.from_orm(competencia) for competencia in competencias]


    @app.get("/api/competencia/{id}", response_model=CompetenciaResponse)
    def find_by_id(id: int, db: Session = Depends(get_db)):
        competencia = CompetenciaRepository.find_by_id(db, id)
        if not competencia:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Competência não encontrada"
            )
        return CompetenciaResponse.from_orm(competencia)


    @app.delete("/api/competencia/{id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_by_id(id: int, db: Session = Depends(get_db)):
        if not CompetenciaRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Competencia não encontrada"
            )
        CompetenciaRepository.delete_by_id(db, id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


    @app.put("/api/competencia/{id}", response_model=CompetenciaResponse)
    def update(id: int, request: CompetenciaRequest, db: Session = Depends(get_db)):
        if not CompetenciaRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Competencia não encontrada"
            )
        competencia = CompetenciaRepository.save(db, Competencia(id=id, **request.dict()))
        return CompetenciaResponse.from_orm(competencia)