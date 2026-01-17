import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") 
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY não encontrada no .env ou nos secrets")


genai.configure(api_key=API_KEY)

def ask_gemini(prompt: str, context: str = "") -> str:
    full_prompt = f"""
Você é um assistente inteligente e objetivo.

PROMPT ATUAL:
{prompt}

CONTEXTO DA VECTOR STORE:
{context}
"""
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash")  
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Erro ao consultar Gemini: {e}"
