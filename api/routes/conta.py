from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from api.models import Conta
from api.schemas.conta_schema import ContaRequest, ContaResponse
from api.database import get_db
from api.repositories.conta_repository import ContaRepository

def init_routes(app):

    @app.post(
        "/api/conta",
        response_model=ContaResponse,
        status_code=status.HTTP_201_CREATED,
    )
    def create(request: ContaRequest, db: Session = Depends(get_db)):
        conta = ContaRepository.save(db, Conta(**request.dict()))
        return ContaResponse.from_orm(conta)


    @app.get("/api/conta", response_model=list[ContaResponse])
    def find_all(db: Session = Depends(get_db)):
        contas = ContaRepository.find_all(db)
        return [ContaResponse.from_orm(conta) for conta in contas]


    @app.get("/api/conta/{id}", response_model=ContaResponse)
    def find_by_id(id: int, db: Session = Depends(get_db)):
        conta = ContaRepository.find_by_id(db, id)
        if not conta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
            )
        return ContaResponse.from_orm(conta)


    @app.delete("/api/conta/{id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_by_id(id: int, db: Session = Depends(get_db)):
        if not ContaRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
            )
        ContaRepository.delete_by_id(db, id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


    @app.put("/api/conta/{id}", response_model=ContaResponse)
    def update(id: int, request: ContaRequest, db: Session = Depends(get_db)):
        if not ContaRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
            )
        conta = ContaRepository.save(db, Conta(id=id, **request.dict()))
        return ContaResponse.from_orm(conta)