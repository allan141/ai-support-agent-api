import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


def analyze_message(message: str):
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": "Você é um agente de suporte. Responda apenas JSON válido, sem markdown."
            },
            {
                "role": "user",
                "content": f"""
Analise a mensagem do cliente.

Retorne apenas este formato JSON:

{{
  "category": "logistica",
  "urgency": "alta",
  "response": "resposta profissional curta"
}}

Categorias possíveis:
logistica, financeiro, suporte_tecnico, cancelamento, reclamacao

Urgências possíveis:
baixa, normal, alta

Mensagem: {message}
"""
            }
        ],
        "temperature": 0.2,
        "max_tokens": 200
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    print("STATUS HF:", response.status_code)
    print("RESPOSTA HF:", response.text)

    if response.status_code != 200:
        return {
            "category": "suporte_tecnico",
            "urgency": "normal",
            "response": f"Erro na API Hugging Face: {response.status_code} - {response.text}"
        }

    data = response.json()
    content = data["choices"][0]["message"]["content"]

    start = content.find("{")
    end = content.rfind("}") + 1

    try:
        return json.loads(content[start:end])
    except Exception:
        return {
            "category": "suporte_tecnico",
            "urgency": "normal",
            "response": content
        }