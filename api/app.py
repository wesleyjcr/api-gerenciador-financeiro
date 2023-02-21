from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import categoria, competencia, conta, classificacao, lancamento

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

categoria.init_routes(app)
competencia.init_routes(app)
conta.init_routes(app)
classificacao.init_routes(app)
lancamento.init_routes(app)

@app.get("/api/status")
def verifica_status():
     return {"status": "ok"}
