import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("Defina GEMINI_API_KEY no .env ou nos secrets")

genai.configure(api_key=API_KEY)





def ask_gemini(prompt: str, context: str = "") -> str:
    try:
        full_prompt = f"{context}\n{prompt}" if context else prompt
        response = genai.generate_content(
            model="models/gemini-2.5-flash-preview-09-2025",
            contents=full_prompt
        )
        return response.text
    except Exception as e:
        return f"Erro ao consultar Gemini: {e}"
