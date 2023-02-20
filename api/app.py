from fastapi import FastAPI
from api.routes import categoria, competencia, conta, classificacao, lancamento

app = FastAPI()

categoria.init_routes(app)
competencia.init_routes(app)
conta.init_routes(app)
classificacao.init_routes(app)
lancamento.init_routes(app)
