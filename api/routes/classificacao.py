from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from api.models import Classificacao
from api.schemas.classificacao_schema import ClassificacaoRequest, ClassificacaoResponse
from api.database import get_db
from api.repositories.classificacao_repository import ClassificacaoRepository

def init_routes(app):

    @app.post(
        "/api/classificacao",
        response_model=ClassificacaoResponse,
        status_code=status.HTTP_201_CREATED,
    )
    def create(request: ClassificacaoRequest, db: Session = Depends(get_db)):
        conta = ClassificacaoRepository.save(db, Classificacao(**request.dict()))
        return ClassificacaoResponse.from_orm(conta)


    @app.get("/api/classificacao", response_model=list[ClassificacaoResponse])
    def find_all(db: Session = Depends(get_db)):
        contas = ClassificacaoRepository.find_all(db)
        return [ClassificacaoResponse.from_orm(conta) for conta in contas]


    @app.get("/api/classificacao/{id}", response_model=ClassificacaoResponse)
    def find_by_id(id: int, db: Session = Depends(get_db)):
        conta = ClassificacaoRepository.find_by_id(db, id)
        if not conta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
            )
        return ClassificacaoResponse.from_orm(conta)


    @app.delete("/api/classificacao/{id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_by_id(id: int, db: Session = Depends(get_db)):
        if not ClassificacaoRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
            )
        ClassificacaoRepository.delete_by_id(db, id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


    @app.put("/api/classificacao/{id}", response_model=ClassificacaoResponse)
    def update(id: int, request: ClassificacaoRequest, db: Session = Depends(get_db)):
        if not ClassificacaoRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
            )
        conta = ClassificacaoRepository.save(db, Classificacao(id=id, **request.dict()))
        return ClassificacaoResponse.from_orm(conta)