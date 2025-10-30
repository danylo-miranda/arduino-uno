from fastapi import FastAPI, Response
import pandas as pd
import os

ARQUIVO_SAIDA = "dados_serial.csv"

app = FastAPI(title="API de Dados do Arduino")

@app.get("/")
def root():
    return {"status": "API online", "fonte": "Arduino via Serial"}

@app.get("/dados")
def get_dados():
    if not os.path.exists(ARQUIVO_SAIDA):
        return {"erro": "Arquivo de dados ainda não existe."}
    
    try:
        df = pd.read_csv(ARQUIVO_SAIDA)
        # Retorna os 100 registros mais recentes
        dados = df.tail(100).to_dict(orient="records")
        return {"total": len(dados), "dados": dados}
    except Exception as e:
        return {"erro": str(e)}

@app.get("/dados/csv")
def get_dados_csv():
    """Retorna o arquivo CSV completo"""
    if not os.path.exists(ARQUIVO_SAIDA):
        return {"erro": "Arquivo não encontrado."}
    
    with open(ARQUIVO_SAIDA, "rb") as f:
        conteudo = f.read()
    return Response(conteudo, media_type="text/csv")
