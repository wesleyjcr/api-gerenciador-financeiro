from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from api.models import Lancamento
from api.schemas.lancamento_schema import LancamentoRequest, LancamentoResponse
from api.database import get_db
from api.repositories.lancamento_repository import LancamentoRepository

def init_routes(app):

    @app.post(
        "/api/lancamento",
        response_model=LancamentoResponse,
        status_code=status.HTTP_201_CREATED,
    )
    def create(request: LancamentoRequest, db: Session = Depends(get_db)):
        lancamento = LancamentoRepository.save(db, Lancamento(**request.dict()))
        return LancamentoResponse.from_orm(lancamento)


    @app.get("/api/lancamento", response_model=list[LancamentoResponse])
    def find_all(db: Session = Depends(get_db)):
        lancamentos = LancamentoRepository.find_all(db)
        return [LancamentoResponse.from_orm(lancamento) for lancamento in lancamentos]


    @app.get("/api/lancamento/{id}", response_model=LancamentoResponse)
    def find_by_id(id: int, db: Session = Depends(get_db)):
        lancamento = LancamentoRepository.find_by_id(db, id)
        if not lancamento:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Lancamento não encontrada"
            )
        return LancamentoResponse.from_orm(lancamento)


    @app.delete("/api/lancamento/{id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_by_id(id: int, db: Session = Depends(get_db)):
        if not LancamentoRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Lancamento não encontrada"
            )
        LancamentoRepository.delete_by_id(db, id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


    @app.put("/api/lancamento/{id}", response_model=LancamentoResponse)
    def update(id: int, request: LancamentoRequest, db: Session = Depends(get_db)):
        if not LancamentoRepository.exists_by_id(db, id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Lancamento não encontrada"
            )
        lancamento = LancamentoRepository.save(db, Lancamento(id=id, **request.dict()))
        return LancamentoResponse.from_orm(lancamento)