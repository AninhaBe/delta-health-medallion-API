# api/app.py
from fastapi import FastAPI
import random
import uuid
from datetime import datetime

app = FastAPI()

@app.get("/reembolsos")
def get_reembolsos():
    dados = []
    for _ in range(random.randint(5, 15)):
        dados.append({
            "id_transacao": str(uuid.uuid4()),
            "data_solicitacao": datetime.now().isoformat(),
            "cpf_beneficiario": f"{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}",
            "nome_paciente": random.choice(["Ana Silva", "Bruno Costa", "Maria Santos", "João Oliveira"]),
            "codigo_procedimento": random.choice(["1010", "2020", "3030"]),
            "valor_reembolso": round(random.uniform(50.0, 1000.0), 2),
            "status": random.choice(["PENDENTE", "PAGO", "NEGADO"])
        })
    return dados