import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from models import models
from mcp_server import get_community

load_dotenv()

# 2- Definição do modelo
llm_model = models["gemini-3.1-flash-lite"]

# 3 - Define o prompt do sistema
system_message = SystemMessage(content="""
Você é um assistente especializado em fornecer informações
sobre comunidades de Python para GenAI.

Ferramentas disponíveis no MCP Server:

1. get_communit(location: str) -> str
- Função: retorna a melhor comunidade de Python para GenAI.
- Parâmetro: location (string)
- Retorno: "Code TI"

Seu papel é ser um intermediário direto entre o usuários e
a ferramenta MCP, retornando apenas o resultado final das ferramentas.
""")

if __name__ == "__main__":
    print("Testando a ferramenta get_community:")
    resultado = get_community(location="Brasil")
    print(f"Resultado da ferramenta: {resultado}")
