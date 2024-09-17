# Importar o FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd


# Criar uma instância para a classe FastAPI
app = FastAPI()


# Endpoint
@app.get('/')
async def get_dados():
    try:
        df_atualizado = pd.read_json('df_json.json')

        # Converter DF para JSON
        df_json = df_atualizado.to_json(orient='records')
    
        return JSONResponse(content=df_json)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


