import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Defina GEMINI_API_KEY no .env ou nos secrets do Streamlit")

genai.configure(api_key=API_KEY)


def get_best_model() -> str:
    """
    Lista os modelos disponíveis e retorna o melhor candidato.
    Preferência: gemini-pro > gemini-flash > qualquer outro.
    """
    models = list(genai.list_models())
    names = [m.name for m in models if "generateContent" in m.supported_generation_methods]

    
    for candidate in ["models/gemini-flash-latest"]:
        if candidate in names:
            return candidate

    
    return names[0] if names else None

MODEL_NAME = get_best_model()
if not MODEL_NAME:
    raise RuntimeError("Nenhum modelo Gemini válido encontrado na sua conta.")

def ask_gemini(prompt: str, context: str = "") -> str:
    """
    Envia uma pergunta para o modelo Gemini e retorna a resposta em texto.
    :param prompt: Texto da pergunta ou instrução
    :param context: Contexto adicional (ex: memória, vetor store)
    """
    try:
        full_prompt = f"{context}\n{prompt}" if context else prompt
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Erro ao consultar Gemini: {e}"


